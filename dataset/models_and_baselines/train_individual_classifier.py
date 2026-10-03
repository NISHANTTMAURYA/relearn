import os
import pickle
import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline
from sklearn.metrics import classification_report, accuracy_score

BASE_DIR = r"d:\relearn\dataset\training_ready_datasets\individual_response_dataset"
MODEL_DIR = r"d:\relearn\dataset\models_and_baselines"

def train_and_evaluate():
    print("=" * 60)
    print("RE:LEARN MODEL A: INDIVIDUAL MISCONCEPTION CLASSIFIER")
    print("=" * 60)

    csv_path = os.path.join(BASE_DIR, "preprocessed_individual_responses.csv")
    df = pd.read_csv(csv_path)

    train_df = df[df["split"] == "train"]
    eval_df = df[df["split"].isin(["val", "test"])]

    print(f"Train samples: {len(train_df)}")
    print(f"Held-out Validation/Test samples: {len(eval_df)}")

    X_train = train_df["model_input_text"]
    y_train = train_df["target_label"]

    X_eval = eval_df["model_input_text"]
    y_eval = eval_df["target_label"]

    # Construct ML Pipeline with Multinomial Logistic Regression and N-Grams
    pipeline = Pipeline([
        ("tfidf", TfidfVectorizer(ngram_range=(1, 3), min_df=1, sublinear_tf=True)),
        ("clf", LogisticRegression(max_iter=1000, class_weight="balanced", C=3.0))
    ])

    pipeline.fit(X_train, y_train)

    probs = pipeline.predict_proba(X_eval)
    classes = pipeline.classes_

    predictions = []
    top2_hypotheses = []
    confidences = []

    # Calibrated confidence for 24 classes: uniform random is 1/24 = 0.0416
    CHANCE_LEVEL = 1.0 / len(classes)

    for row_probs in probs:
        sorted_indices = np.argsort(row_probs)[::-1]
        top1_idx = sorted_indices[0]
        top2_idx = sorted_indices[1]

        top1_prob = row_probs[top1_idx]
        top2_prob = row_probs[top2_idx]

        # Normalized confidence relative to runner-up
        margin = top1_prob - top2_prob
        normalized_conf = min(0.99, max(0.20, (top1_prob / (top1_prob + top2_prob))))

        confidences.append(normalized_conf)
        top2_hypotheses.append(classes[top2_idx])

        # Abstention if top1 is indistinguishable from chance
        if top1_prob < 1.2 * CHANCE_LEVEL or margin < 0.01:
            predictions.append("UNSURE_NEEDS_MORE_EVIDENCE")
        else:
            predictions.append(classes[top1_idx])

    acc = accuracy_score(y_eval, predictions)
    print(f"\nHeld-Out Exact Accuracy: {acc * 100:.2f}%")
    print(f"Average Normalized Confidence: {np.mean(confidences) * 100:.2f}%")

    print("\nSample Held-out Predictions with Diagnostic Confidence & Alternative Hypotheses:")
    for i, (text, true_lbl, pred_lbl, alt_lbl, conf) in enumerate(zip(X_eval[:8], y_eval[:8], predictions[:8], top2_hypotheses[:8], confidences[:8])):
        print(f"\n[Sample {i+1}]")
        print(f"  Input: {text[:95]}...")
        print(f"  Ground Truth: {true_lbl[:45]}")
        print(f"  Primary Prediction:    {pred_lbl[:45]} (Conf: {conf:.2f})")
        print(f"  Alternative Candidate: {alt_lbl[:45]}")

    model_save_path = os.path.join(MODEL_DIR, "individual_misconception_model.pkl")
    with open(model_save_path, "wb") as f:
        pickle.dump(pipeline, f)

    print(f"\nTrained baseline model saved successfully to: {model_save_path}")
    return pipeline

if __name__ == "__main__":
    train_and_evaluate()
