import os
os.environ["HF_HOME"] = r"d:\relearn\.cache\huggingface"
import torch
import pandas as pd
import numpy as np
from sklearn.metrics import classification_report, accuracy_score, f1_score
from transformers import AutoTokenizer, AutoModelForSequenceClassification

def evaluate():
    model_dir = r"d:\relearn\dataset\models_and_baselines\deberta_primary_model"
    base_dir = r"d:\relearn\dataset\individual_response_dataset"
    test_path = os.path.join(base_dir, "test.csv")
    ood_path = os.path.join(base_dir, "ood_test.csv")

    label_classes = np.load(os.path.join(model_dir, "label_classes.npy"), allow_pickle=True)
    label2idx = {cls: i for i, cls in enumerate(label_classes)}

    device = "cuda" if torch.cuda.is_available() else "cpu"
    print(f"Loading model from {model_dir} on {device}...")
    tokenizer = AutoTokenizer.from_pretrained(model_dir)
    model = AutoModelForSequenceClassification.from_pretrained(model_dir).to(device)
    model.eval()

    def run_eval(df, name):
        print(f"\n--- EVALUATING {name} ({len(df)} samples) ---")
        df["text"] = "Question: " + df["question_text"].fillna("") + " | Student Response: " + df["student_response"].fillna("")
        y_true = [label2idx[l] for l in df["misconception_label"]]
        y_pred = []
        batch_size = 32
        for i in range(0, len(df), batch_size):
            batch_texts = df["text"].iloc[i:i+batch_size].tolist()
            enc = tokenizer(batch_texts, return_tensors="pt", padding=True, truncation=True, max_length=256).to(device)
            with torch.no_grad():
                logits = model(**enc).logits
                preds = torch.argmax(logits, dim=-1).cpu().numpy()
                y_pred.extend(preds)

        acc = accuracy_score(y_true, y_pred)
        f1_mac = f1_score(y_true, y_pred, average="macro", zero_division=0)
        print(f"{name} ACCURACY: {acc*100:.2f}% | Macro F1: {f1_mac:.4f}")

        # Find classes with lowest recall
        rep = classification_report(y_true, y_pred, target_names=label_classes, output_dict=True, zero_division=0)
        low_recall_classes = []
        for cls_name in label_classes:
            if cls_name in rep:
                rec = rep[cls_name]["recall"]
                supp = rep[cls_name]["support"]
                if rec < 0.85:
                    low_recall_classes.append((cls_name, rec, supp))
        low_recall_classes.sort(key=lambda x: x[1])
        print(f"Classes with Recall < 85% ({len(low_recall_classes)} classes):")
        for cls_name, rec, supp in low_recall_classes[:10]:
            print(f"  - {cls_name[:45]}: Recall={rec*100:.1f}% (Support={supp})")

        return acc, f1_mac, y_true, y_pred

    df_test = pd.read_csv(test_path)
    run_eval(df_test, "HELD-OUT TEST SET")

    if os.path.exists(ood_path):
        df_ood = pd.read_csv(ood_path)
        run_eval(df_ood, "OOD CHALLENGE BENCHMARK")

if __name__ == "__main__":
    evaluate()
