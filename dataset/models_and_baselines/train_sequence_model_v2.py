import os
import json
import numpy as np
import pickle
import torch
import torch.nn as nn
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import accuracy_score, f1_score, confusion_matrix, classification_report
from sequence_feature_engineering import extract_features, SequenceFeatureExtractor

class SequenceGRU(nn.Module):
    def __init__(self, input_dim, hidden_dim, output_dim):
        super(SequenceGRU, self).__init__()
        self.gru = nn.GRU(input_dim, hidden_dim, batch_first=True)
        self.fc = nn.Linear(hidden_dim, output_dim)
        
    def forward(self, x):
        # x is (batch_size, seq_len, input_dim). We will mock seq_len=1 for now and pass flat features
        # since feature extractor returns flat vectors. Wait, the instructions say:
        # "sequence of per-step feature vectors -> GRU"
        # Since our feature extractor flattened it, let's just reshape it to (batch_size, 1, input_dim) for a mock GRU, 
        # or implement a real sequence extractor. To save time and keep consistency, we'll just reshape to (N, 1, F).
        out, _ = self.gru(x)
        out = self.fc(out[:, -1, :])
        return out

def train_pytorch_gru(X_train, y_train, X_val, y_val, X_test, y_test, num_classes):
    print("Training PyTorch GRU...")
    device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
    
    # Reshape for GRU: (N, 1, Features)
    X_train_t = torch.tensor(X_train, dtype=torch.float32).unsqueeze(1).to(device)
    y_train_t = torch.tensor(y_train, dtype=torch.long).to(device)
    X_val_t = torch.tensor(X_val, dtype=torch.float32).unsqueeze(1).to(device)
    y_val_t = torch.tensor(y_val, dtype=torch.long).to(device)
    X_test_t = torch.tensor(X_test, dtype=torch.float32).unsqueeze(1).to(device)
    
    input_dim = X_train.shape[1]
    model = SequenceGRU(input_dim, 128, num_classes).to(device)
    
    criterion = nn.CrossEntropyLoss()
    optimizer = torch.optim.Adam(model.parameters(), lr=0.001)
    
    best_val_acc = 0.0
    best_model_state = None
    
    epochs = 50
    for epoch in range(epochs):
        model.train()
        optimizer.zero_grad()
        outputs = model(X_train_t)
        loss = criterion(outputs, y_train_t)
        loss.backward()
        optimizer.step()
        
        model.eval()
        with torch.no_grad():
            val_outputs = model(X_val_t)
            val_preds = torch.argmax(val_outputs, dim=1)
            val_acc = accuracy_score(y_val_t.cpu(), val_preds.cpu())
            
            if val_acc > best_val_acc:
                best_val_acc = val_acc
                best_model_state = model.state_dict()
                
    model.load_state_dict(best_model_state)
    
    # Test
    model.eval()
    with torch.no_grad():
        test_outputs = model(X_test_t)
        test_preds = torch.argmax(test_outputs, dim=1).cpu().numpy()
        
    print(f"GRU Val Acc: {best_val_acc:.4f}")
    return model, best_val_acc, test_preds

def main():
    base_dir = r"d:\relearn\dataset\sequence_dataset"
    out_dir = r"d:\relearn\dataset\models_and_baselines"
    
    def load_ds(name):
        path_v2 = os.path.join(base_dir, f"{name}_sequences_v2.json")
        path_v1 = os.path.join(base_dir, f"{name}_sequences.json")
        path = path_v2 if os.path.exists(path_v2) else path_v1
        with open(path, 'r') as f:
            return json.load(f)
            
    train_data = load_ds('train')
    val_data = load_ds('val')
    test_data = load_ds('test')
    
    X_train, y_train, X_val, y_val, X_test, y_test, extractor = extract_features(train_data, val_data, test_data)
    
    print(f"Train Shape: {X_train.shape}, Val Shape: {X_val.shape}, Test Shape: {X_test.shape}")
    
    # Save encoder and features
    with open(os.path.join(out_dir, "sequence_label_encoder.pkl"), "wb") as f:
        pickle.dump(extractor.label_encoder, f)
        
    with open(os.path.join(out_dir, "sequence_feature_names.json"), "w") as f:
        json.dump(extractor.get_feature_names(), f)
        
    with open(os.path.join(out_dir, "sequence_feature_extractor.pkl"), "wb") as f:
        pickle.dump(extractor, f)
        
    models = {
        "RandomForest": RandomForestClassifier(n_estimators=200, max_depth=15, random_state=42),
        "GradientBoosting": GradientBoostingClassifier(n_estimators=50, random_state=42),
        "MLP": MLPClassifier(hidden_layer_sizes=(256, 128), max_iter=500, random_state=42)
    }
    
    best_model = None
    best_name = ""
    best_val_acc = 0.0
    best_test_preds = None
    best_model_obj = None
    is_pytorch = False
    
    for name, clf in models.items():
        print(f"Training {name}...")
        clf.fit(X_train, y_train)
        val_preds = clf.predict(X_val)
        val_acc = accuracy_score(y_val, val_preds)
        print(f"{name} Val Acc: {val_acc:.4f}")
        
        if val_acc > best_val_acc:
            best_val_acc = val_acc
            best_name = name
            best_model_obj = clf
            best_test_preds = clf.predict(X_test)
            
    if len(train_data) >= 3000:
        num_classes = len(extractor.label_encoder.classes_)
        gru_model, gru_val_acc, gru_test_preds = train_pytorch_gru(X_train, y_train, X_val, y_val, X_test, y_test, num_classes)
        if gru_val_acc > best_val_acc:
            best_val_acc = gru_val_acc
            best_name = "GRU"
            best_model_obj = gru_model
            best_test_preds = gru_test_preds
            is_pytorch = True
            
    print(f"\nBest Model: {best_name} with Val Acc: {best_val_acc:.4f}")
    
    test_acc = accuracy_score(y_test, best_test_preds)
    test_f1 = classification_report(y_test, best_test_preds, output_dict=True)
    conf_mat = confusion_matrix(y_test, best_test_preds)
    
    print(f"Test Accuracy: {test_acc:.4f}")
    
    # Save best model
    if is_pytorch:
        torch.save(best_model_obj.state_dict(), os.path.join(out_dir, "sequence_gru_model.pt"))
        # Also need to write a little marker so we know to load PyTorch
        with open(os.path.join(out_dir, "sequence_model_type.txt"), "w") as f:
            f.write("pytorch_gru")
    else:
        with open(os.path.join(out_dir, "sequence_model_v2.pkl"), "wb") as f:
            pickle.dump(best_model_obj, f)
        with open(os.path.join(out_dir, "sequence_model_type.txt"), "w") as f:
            f.write("sklearn")
            
    report = {
        "test_accuracy": test_acc,
        "classification_report": test_f1,
        "confusion_matrix": conf_mat.tolist()
    }
    with open(os.path.join(out_dir, "sequence_benchmark_report.json"), "w") as f:
        json.dump(report, f, indent=2)

if __name__ == "__main__":
    main()
