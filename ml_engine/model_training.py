import os
import pandas as pd
import joblib
from sklearn.ensemble import AdaBoostClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, confusion_matrix

def train_adaboost(X, y):
    model = AdaBoostClassifier(n_estimators=100)
    model.fit(X, y)
    return model

def load_and_process_csv(path):
    df = pd.read_csv(path)
    df = df.dropna()
    y = df["Donor_Category"].map({"Under-Patron": 0, "Patron+": 1})
    X = df.drop(columns=["Donor_Category"])
    return train_test_split(X, y, test_size=0.2, random_state=42), df.columns.tolist()

def run_adaboost_on_all(data_dir="ml_engine/data", save_dir="model"):
    os.makedirs(save_dir, exist_ok=True)

    results = []

    for i, filename in enumerate(sorted(os.listdir(data_dir))):
        if filename.endswith(".csv"):
            path = os.path.join(data_dir, filename)
            (X_train, X_test, y_train, y_test), feature_names = load_and_process_csv(path)

            model = train_adaboost(X_train, y_train)

            # Save model
            model_path = os.path.join(save_dir, f"ada_model_{i+1}.pkl")
            joblib.dump(model, model_path)

            # Predictions + metrics
            y_pred = model.predict(X_test)
            y_proba = model.predict_proba(X_test)[:, 1]
            report = classification_report(y_test, y_pred, output_dict=True)
            cm = confusion_matrix(y_test, y_pred)

            results.append({
                "filename": filename,
                "model_path": model_path,
                "report": report,
                "confusion_matrix": cm,
                "y_true": y_test,
                "y_pred": y_pred,
                "y_proba": y_proba
            })

    return results
