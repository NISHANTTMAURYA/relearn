import os
os.environ["HF_HOME"] = r"d:\relearn\.cache\huggingface"
import torch
import pandas as pd
import numpy as np
from transformers import AutoTokenizer, AutoModelForSequenceClassification

model_dir = r"d:\relearn\dataset\models_and_baselines\deberta_primary_model"
base_dir = r"d:\relearn\dataset\individual_response_dataset"
label_classes = np.load(os.path.join(model_dir, "label_classes.npy"), allow_pickle=True)
label2idx = {cls: i for i, cls in enumerate(label_classes)}

device = "cuda" if torch.cuda.is_available() else "cpu"
tokenizer = AutoTokenizer.from_pretrained(model_dir)
model = AutoModelForSequenceClassification.from_pretrained(model_dir).to(device)
model.eval()

df_ood = pd.read_csv(os.path.join(base_dir, "ood_test.csv"))
df_ood["text"] = "Question: " + df_ood["question_text"].fillna("") + " | Student Response: " + df_ood["student_response"].fillna("")
y_true = [label2idx[l] for l in df_ood["misconception_label"]]

y_pred = []
batch_size = 32
for i in range(0, len(df_ood), batch_size):
    batch_texts = df_ood["text"].iloc[i:i+batch_size].tolist()
    enc = tokenizer(batch_texts, return_tensors="pt", padding=True, truncation=True, max_length=256).to(device)
    with torch.no_grad():
        preds = torch.argmax(model(**enc).logits, dim=-1).cpu().numpy()
        y_pred.extend(preds)

df_ood["predicted"] = [label_classes[p] for p in y_pred]
df_ood["is_correct"] = df_ood["misconception_label"] == df_ood["predicted"]

print(f"Overall OOD Accuracy: {df_ood['is_correct'].mean()*100:.2f}% ({df_ood['is_correct'].sum()}/{len(df_ood)})")

print("\nAccuracy by challenge_type:")
for ct, grp in df_ood.groupby("challenge_type"):
    print(f"  {ct:<30}: {grp['is_correct'].mean()*100:.1f}% ({grp['is_correct'].sum()}/{len(grp)})")

print("\nSample Misclassifications in OOD:")
for _, row in df_ood[~df_ood['is_correct']].head(10).iterrows():
    print(f"Type: {row['challenge_type']} | Question: {row['question_text'][:50]}...")
    print(f"  Response: {row['student_response']}")
    print(f"  Expected:  {row['misconception_label'][:45]}")
    print(f"  Predicted: {row['predicted'][:45]}")
