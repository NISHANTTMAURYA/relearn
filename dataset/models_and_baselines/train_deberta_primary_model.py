import os
os.environ["HF_HOME"] = r"d:\relearn\.cache\huggingface"
import sys
import torch
import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import classification_report, accuracy_score, f1_score
from transformers import AutoTokenizer, AutoModelForSequenceClassification, Trainer, TrainingArguments
from transformers import DataCollatorWithPadding

def main():
    print("=" * 60)
    print("RE:LEARN PRIMARY MODEL TRAINING PIPELINE (PyTorch CUDA + DeBERTa-v3)")
    print("=" * 60)

    device = "cuda" if torch.cuda.is_available() else "cpu"
    print(f"[GPU Status] PyTorch Version: {torch.__version__} | Device: {device}")
    if torch.cuda.is_available():
        print(f"[GPU Hardware] Device Name: {torch.cuda.get_device_name(0)}")

    base_dir = r"d:\relearn\dataset\individual_response_dataset"
    train_path = os.path.join(base_dir, "train.csv")
    val_path = os.path.join(base_dir, "val.csv")
    test_path = os.path.join(base_dir, "test.csv")

    if not os.path.exists(train_path):
        print(f"[Error] Training file not found at: {train_path}")
        sys.exit(1)

    print("\n[1/5] Loading leak-free stratified splits...")
    df_train = pd.read_csv(train_path)
    df_val = pd.read_csv(val_path)
    df_test = pd.read_csv(test_path)

    print(f"  * Train set: {len(df_train)} samples")
    print(f"  * Val set:   {len(df_val)} samples")
    print(f"  * Test set:  {len(df_test)} samples")

    # Construct input text feature: "Question: <stem> | Student Response: <response>"
    for df in [df_train, df_val, df_test]:
        df["text"] = "Question: " + df["question_text"].fillna("") + " | Student Response: " + df["student_response"].fillna("")

    label_encoder = LabelEncoder()
    df_train["label_idx"] = label_encoder.fit_transform(df_train["misconception_label"])
    df_val["label_idx"] = label_encoder.transform(df_val["misconception_label"])
    df_test["label_idx"] = label_encoder.transform(df_test["misconception_label"])

    num_classes = len(label_encoder.classes_)
    print(f"  * Total Misconception Classes: {num_classes}")

    # Model Base Selection: deberta-v3-small for fast lightweight CUDA training
    model_name = "microsoft/deberta-v3-small"
    print(f"\n[2/5] Initializing Tokenizer & Model ({model_name})...")
    
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModelForSequenceClassification.from_pretrained(
        model_name,
        num_labels=num_classes
    )

    class PhysicsDataset(torch.utils.data.Dataset):
        def __init__(self, texts, labels, tokenizer, max_length=256):
            self.encodings = tokenizer(texts, truncation=True, padding=False, max_length=max_length)
            self.labels = labels

        def __getitem__(self, idx):
            item = {key: torch.tensor(val[idx]) for key, val in self.encodings.items()}
            item['labels'] = torch.tensor(self.labels[idx], dtype=torch.long)
            return item

        def __len__(self):
            return len(self.labels)

    print("\n[3/5] Tokenizing dataset splits...")
    train_dataset = PhysicsDataset(df_train["text"].tolist(), df_train["label_idx"].tolist(), tokenizer)
    val_dataset = PhysicsDataset(df_val["text"].tolist(), df_val["label_idx"].tolist(), tokenizer)
    test_dataset = PhysicsDataset(df_test["text"].tolist(), df_test["label_idx"].tolist(), tokenizer)

    def compute_metrics(eval_pred):
        logits, labels = eval_pred
        preds = np.argmax(logits, axis=1)
        acc = accuracy_score(labels, preds)
        f1_macro = f1_score(labels, preds, average="macro")
        return {"accuracy": acc, "f1_macro": f1_macro}

    output_dir = r"d:\relearn\dataset\models_and_baselines\deberta_primary_model"
    os.makedirs(output_dir, exist_ok=True)

    training_args = TrainingArguments(
        output_dir=output_dir,
        num_train_epochs=5,
        learning_rate=3e-5,
        lr_scheduler_type="cosine",
        label_smoothing_factor=0.05,
        per_device_train_batch_size=16,
        per_device_eval_batch_size=32,
        warmup_ratio=0.1,
        weight_decay=0.01,
        logging_dir=os.path.join(output_dir, "logs"),
        logging_steps=50,
        eval_strategy="epoch",
        save_strategy="epoch",
        load_best_model_at_end=True,
        metric_for_best_model="accuracy",
        save_total_limit=2,
        fp16=torch.cuda.is_available(),
        report_to="none"
    )

    trainer = Trainer(
        model=model,
        args=training_args,
        train_dataset=train_dataset,
        eval_dataset=val_dataset,
        tokenizer=tokenizer,
        data_collator=DataCollatorWithPadding(tokenizer=tokenizer),
        compute_metrics=compute_metrics
    )

    print("\n[4/5] Starting PyTorch GPU fine-tuning (5 Epochs with Cosine Decay & Label Smoothing)...")
    trainer.train()

    print("\n[5/5] Evaluating Model on Held-Out Test Set (Disjoint Phrasing Templates)...")
    test_results = trainer.predict(test_dataset)
    test_preds = np.argmax(test_results.predictions, axis=1)
    test_acc = accuracy_score(df_test["label_idx"], test_preds)
    test_f1 = f1_score(df_test["label_idx"], test_preds, average="macro")
    
    print("\n" + "=" * 60)
    print(f"HELD-OUT TEST ACCURACY (Disjoint Templates): {test_acc * 100:.2f}% | Macro F1: {test_f1:.4f}")
    print("=" * 60)

    # Evaluate on Out-of-Distribution (OOD) Challenge Benchmark
    ood_path = os.path.join(base_dir, "ood_test.csv")
    if os.path.exists(ood_path):
        print("\n" + "=" * 60)
        print("EVALUATING ON REAL-WORLD OUT-OF-DISTRIBUTION (OOD) CHALLENGE BENCHMARK")
        print("=" * 60)
        df_ood = pd.read_csv(ood_path)
        df_ood["text"] = "Question: " + df_ood["question_text"].fillna("") + " | Student Response: " + df_ood["student_response"].fillna("")
        df_ood["label_idx"] = label_encoder.transform(df_ood["misconception_label"])
        ood_dataset = PhysicsDataset(df_ood["text"].tolist(), df_ood["label_idx"].tolist(), tokenizer)
        
        ood_results = trainer.predict(ood_dataset)
        ood_preds = np.argmax(ood_results.predictions, axis=1)
        ood_acc = accuracy_score(df_ood["label_idx"], ood_preds)
        ood_f1 = f1_score(df_ood["label_idx"], ood_preds, average="macro")
        print(f"OOD CHALLENGE BENCHMARK ACCURACY: {ood_acc * 100:.2f}% | Macro F1: {ood_f1:.4f}")

    # Qualitative Stress-Test on Authentic Messy Inquiries
    print("\n" + "=" * 60)
    print("QUALITATIVE REAL-WORLD STRESS-TEST ON MESSY STUDENT RESPONSES")
    print("=" * 60)
    qual_samples = [
        ("A student forms a sharp image of a lighted candle on a screen using a convex lens of focal length 15 cm. The lower half of the lens is covered with black paper.",
         "bro only bottom part shows up top part is cut off"),
        ("Two identical electric bulbs B1 and B2 are connected in series with a 6V battery. Compare current.",
         "current gets consumed by the first bulb so the second bulb gets less current"),
        ("Two metal balls, one of 5 kg and another of 0.5 kg, are dropped simultaneously from a 20 m tower.",
         "heavy ball drops faster coz gravity pulls heavier things harder"),
        ("A ray of light strikes a plane mirror along the normal. What is the angle of reflection?",
         "sir ray just stops at normal because angle is zero"),
        ("Calculate equivalent resistance of two 4-ohm resistors connected in parallel.",
         "idk forgot the formula skip please")
    ]

    model.eval()
    for q_stem, s_resp in qual_samples:
        inp_text = f"Question: {q_stem} | Student Response: {s_resp}"
        enc = tokenizer(inp_text, return_tensors="pt", truncation=True, max_length=256).to(device)
        with torch.no_grad():
            logits = model(**enc).logits
            probs = torch.softmax(logits, dim=-1).cpu().numpy()[0]
            pred_idx = np.argmax(probs)
            pred_label = label_encoder.classes_[pred_idx]
            conf = probs[pred_idx]
        print(f"\n[Test Prompt] \"{s_resp}\"")
        print(f"  -> Predicted Diagnosis: {pred_label} (Confidence: {conf:.3f})")

    # Save fine-tuned model and label encoder
    print(f"\n[Save] Saving fine-tuned primary model to: {output_dir}")
    trainer.save_model(output_dir)
    tokenizer.save_pretrained(output_dir)
    np.save(os.path.join(output_dir, "label_classes.npy"), label_encoder.classes_)
    
    print("SUCCESS: Primary DeBERTa-v3 misconception model trained and saved!")

if __name__ == "__main__":
    main()
