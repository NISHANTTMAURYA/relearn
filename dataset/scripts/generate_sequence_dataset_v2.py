import json
import random
import uuid
import os
import copy

def load_data(filepath):
    if not os.path.exists(filepath): return []
    with open(filepath, 'r') as f:
        return json.load(f)

def generate_augmented(data, count, length_range=(3,7)):
    if not data: return []
    augmented = []
    
    # We want at least 'count' samples, balancing classes
    from collections import defaultdict
    class_dict = defaultdict(list)
    for d in data:
        class_dict[d.get('sequence_level_label', 'UNKNOWN')].append(d)
        
    classes = list(class_dict.keys())
    
    for _ in range(count):
        cls = random.choice(classes)
        template = random.choice(class_dict[cls])
        
        new_seq = copy.deepcopy(template)
        new_seq['sequence_id'] = f"seq_{uuid.uuid4().hex[:8]}"
        new_seq['student_id'] = f"student_{random.randint(1000, 9999)}"
        
        target_len = random.randint(*length_range)
        attempts = new_seq.get('ordered_attempts', [])
        
        if not attempts:
            continue
            
        # expand or trim attempts
        while len(attempts) < target_len:
            attempts.append(copy.deepcopy(random.choice(attempts)))
        
        if len(attempts) > target_len:
            attempts = attempts[:target_len]
            
        # slightly modify text to add variance
        for a in attempts:
            a['confidence'] = random.choice(['high', 'medium', 'low'])
            if 'student_response' in a and a['student_response']:
                words = a['student_response'].split()
                if len(words) > 2:
                    random.shuffle(words) # dumb shuffle for variance
                    a['student_response'] = " ".join(words)
                    
        new_seq['ordered_attempts'] = attempts
        augmented.append(new_seq)
        
    return augmented

def main():
    base_dir = r"d:\relearn\dataset\sequence_dataset"
    train_path = os.path.join(base_dir, "train_sequences.json")
    val_path = os.path.join(base_dir, "val_sequences.json")
    test_path = os.path.join(base_dir, "test_sequences.json")
    
    train_data = load_data(train_path)
    val_data = load_data(val_path)
    test_data = load_data(test_path)
    
    # Expand
    train_v2 = train_data + generate_augmented(train_data, max(0, 5000 - len(train_data)))
    val_v2 = val_data + generate_augmented(val_data, max(0, 1000 - len(val_data)))
    test_v2 = test_data + generate_augmented(test_data, max(0, 1000 - len(test_data)))
    
    with open(os.path.join(base_dir, "train_sequences_v2.json"), "w") as f:
        json.dump(train_v2, f, indent=2)
    with open(os.path.join(base_dir, "val_sequences_v2.json"), "w") as f:
        json.dump(val_v2, f, indent=2)
    with open(os.path.join(base_dir, "test_sequences_v2.json"), "w") as f:
        json.dump(test_v2, f, indent=2)
        
    print(f"Generated v2 dataset: Train={len(train_v2)}, Val={len(val_v2)}, Test={len(test_v2)}")
    
    labels = [d.get('sequence_level_label') for d in train_v2]
    from collections import Counter
    print("Label Distribution Train V2:", Counter(labels))

if __name__ == "__main__":
    main()
