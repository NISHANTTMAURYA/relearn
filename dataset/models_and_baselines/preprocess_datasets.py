import json
import os
import re
import pandas as pd

BASE_DIR = r"d:\relearn\dataset\training_ready_datasets"
INDIV_DIR = os.path.join(BASE_DIR, "individual_response_dataset")
SEQ_DIR = os.path.join(BASE_DIR, "sequence_dataset")

def clean_text(text):
    if not isinstance(text, str):
        return ""
    # Standardize whitespace and remove extraneous artifacts
    text = re.sub(r'\s+', ' ', text).strip()
    return text

def preprocess_individual_dataset():
    print("Preprocessing Individual-Response Dataset...")
    df = pd.read_csv(os.path.join(INDIV_DIR, "individual_responses.csv"))
    
    # Text cleaning
    df["clean_question"] = df["question_text"].apply(clean_text)
    df["clean_response"] = df["student_response"].apply(clean_text)
    df["clean_correct"] = df["correct_answer_and_steps"].apply(clean_text)
    
    # Combined model input: context + question + student response
    df["model_input_text"] = (
        "Topic: " + df["topic_concept"].astype(str) + 
        " | Question: " + df["clean_question"] + 
        " | Student Response: " + df["clean_response"]
    )
    
    # Label simplification for standard classification
    df["target_label"] = df["misconception_label"]
    
    # Save preprocessed version
    out_csv = os.path.join(INDIV_DIR, "preprocessed_individual_responses.csv")
    df.to_csv(out_csv, index=False)
    print(f"Preprocessed individual dataset saved to {out_csv} ({len(df)} rows)")
    return df

def preprocess_sequence_dataset():
    print("Preprocessing Sequence Dataset...")
    seq_path = os.path.join(SEQ_DIR, "student_sequences.json")
    with open(seq_path, "r", encoding="utf-8") as f:
        sequences = json.load(f)
        
    flattened_rows = []
    for seq in sequences:
        sid = seq["sequence_id"]
        st_id = seq["student_id"]
        pattern_label = seq["sequence_level_label"]
        status = seq.get("learning_status", seq.get("status", "UNKNOWN"))
        split = seq.get("split", "train")
        
        attempts = seq.get("ordered_attempts", [])
        total_steps = len(attempts)
        
        # Aggregate attempt texts
        responses_concat = " -> ".join([f"Step {a.get('step', i+1)}: {clean_text(a.get('student_response', a.get('response', '')))}" for i, a in enumerate(attempts)])
        diagnoses_concat = " -> ".join([a.get("individual_diagnosis", a.get("diagnosis", "UNKNOWN")) for a in attempts])

        
        flattened_rows.append({
            "sequence_id": sid,
            "student_id": st_id,
            "topic": seq.get("topic", ""),
            "total_steps": total_steps,
            "responses_sequence": responses_concat,
            "individual_diagnoses_sequence": diagnoses_concat,
            "sequence_pattern_label": pattern_label,
            "learning_status": status,
            "split": split
        })
        
    df_seq = pd.DataFrame(flattened_rows)
    out_csv = os.path.join(SEQ_DIR, "preprocessed_sequences.csv")
    df_seq.to_csv(out_csv, index=False)
    print(f"Preprocessed sequence dataset saved to {out_csv} ({len(df_seq)} sequences)")
    return df_seq

if __name__ == "__main__":
    preprocess_individual_dataset()
    preprocess_sequence_dataset()
    print("Preprocessing complete!")
