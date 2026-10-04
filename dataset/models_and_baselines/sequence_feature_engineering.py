import json
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.preprocessing import LabelEncoder
from collections import Counter

class SequenceFeatureExtractor:
    def __init__(self, max_text_features=100):
        self.max_text_features = max_text_features
        self.tfidf = TfidfVectorizer(max_features=self.max_text_features, stop_words='english')
        self.label_encoder = LabelEncoder()
        self.misconception_codes = set()
        self.is_fitted = False
        self.misconception_list = []

    def fit(self, sequences):
        labels = []
        texts = []
        
        for seq in sequences:
            if 'sequence_level_label' in seq:
                labels.append(seq['sequence_level_label'])
            
            attempts = seq.get('ordered_attempts', [])
            seq_text = " ".join([a.get('student_response', '') for a in attempts if a.get('student_response')])
            texts.append(seq_text)
            
            for a in attempts:
                diag = a.get('individual_diagnosis', '')
                if diag and diag.startswith('MISC'):
                    self.misconception_codes.add(diag)
                    
        if labels:
            self.label_encoder.fit(labels)
            
        self.tfidf.fit(texts)
        self.misconception_list = sorted(list(self.misconception_codes))
        self.is_fitted = True

    def transform(self, sequences, return_labels=True):
        if not self.is_fitted:
            raise ValueError("Extractor is not fitted.")
            
        X = []
        y = []
        
        texts = []
        for seq in sequences:
            attempts = seq.get('ordered_attempts', [])
            
            length = len(attempts)
            if length == 0:
                # empty row fallback
                features = [0]*10
                texts.append("")
                X.append(features + [0]*len(self.misconception_list))
                if return_labels and 'sequence_level_label' in seq:
                    y.append(seq['sequence_level_label'])
                continue
                
            num_correct = sum(1 for a in attempts if a.get('is_correct'))
            num_misc = sum(1 for a in attempts if a.get('individual_diagnosis', '').startswith('MISC'))
            num_unsure = sum(
                1 for a in attempts
                if (isinstance(a.get('confidence'), (int, float)) and a.get('confidence', 1.0) < 0.6)
                or (isinstance(a.get('confidence'), str) and a.get('confidence', '').lower() in ['low', 'unsure'])
                or 'unsure' in str(a.get('student_response', '')).lower()
            )
            
            diags = [a.get('individual_diagnosis', '') for a in attempts]
            misc_diags = [d for d in diags if d.startswith('MISC')]
            unique_miscs = len(set(misc_diags))
            
            correct_ratio = num_correct / length
            
            # persistent same-misc ratio
            if len(misc_diags) > 0:
                most_common_count = Counter(misc_diags).most_common(1)[0][1]
                persistent_ratio = most_common_count / length
            else:
                persistent_ratio = 0.0
                
            last_correct = 1.0 if attempts[-1].get('is_correct') else 0.0
            
            # monotonically improving
            # track 'correctness' over time, e.g. [False, False, True] is improving.
            # We'll just define it as no True followed by False.
            improving = 1.0
            seen_true = False
            for a in attempts:
                is_c = a.get('is_correct')
                if is_c:
                    seen_true = True
                elif seen_true:
                    improving = 0.0
                    break
                    
            seq_text = " ".join([a.get('student_response', '') for a in attempts if a.get('student_response')])
            texts.append(seq_text)
            
            misc_counts = Counter(misc_diags)
            misc_vector = [misc_counts.get(m, 0) for m in self.misconception_list]
            
            features = [
                float(length), float(unique_miscs), float(num_correct), float(num_misc), float(num_unsure),
                float(correct_ratio), float(persistent_ratio), float(last_correct), float(improving)
            ]
            X.append(features + misc_vector)
            
            if return_labels and 'sequence_level_label' in seq:
                y.append(seq['sequence_level_label'])
                
        # TF-IDF
        text_features = self.tfidf.transform(texts).toarray()
        
        # Combine
        X_final = np.hstack((np.array(X), text_features))
        
        if return_labels and len(y) > 0:
            y_encoded = self.label_encoder.transform(y)
            return X_final, y_encoded
        else:
            return X_final
            
    def get_feature_names(self):
        names = [
            "length", "unique_miscs", "num_correct", "num_misc", "num_unsure",
            "correct_ratio", "persistent_ratio", "last_correct", "improving"
        ]
        names.extend(self.misconception_list)
        names.extend(self.tfidf.get_feature_names_out().tolist())
        return names

def extract_features(train_seqs, val_seqs, test_seqs):
    extractor = SequenceFeatureExtractor()
    extractor.fit(train_seqs)
    
    X_train, y_train = extractor.transform(train_seqs)
    X_val, y_val = extractor.transform(val_seqs)
    X_test, y_test = extractor.transform(test_seqs)
    
    return X_train, y_train, X_val, y_val, X_test, y_test, extractor
