import os
import pickle
import pandas as pd
from pathlib import Path
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression, LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import matplotlib.pyplot as plt

BASE = Path(__file__).resolve().parent
MODEL_DIR = BASE / "models"
MODEL_DIR.mkdir(parents=True, exist_ok=True)

FEATURES = [
    "cgpa",
    "backlogs",
    "coding_score",
    "aptitude_score",
    "communication_score",
    "projects",
    "internships",
    "certifications",
    "github_contributions",
    "leetcode_solved",
    "hackathon",
    "soft_skills",
]


def load_data():
    path = BASE / "data.csv"
    if not path.exists():
        raise FileNotFoundError("data.csv not found. Run python data_generator.py first.")
    df = pd.read_csv(path)
    return df


def train_models(df):
    X = df[FEATURES]
    y = df["placement_status"]
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    logistic = LogisticRegression(max_iter=1000)
    rf = RandomForestClassifier(n_estimators=150, random_state=42)
    logistic.fit(X_train, y_train)
    rf.fit(X_train, y_train)
    try:
        import xgboost as xgb
        xgboost = xgb.XGBClassifier(use_label_encoder=False, eval_metric="logloss", random_state=42)
        xgboost.fit(X_train, y_train)
    except Exception:
        xgboost = None
    y_pred_log = logistic.predict(X_test)
    y_pred_rf = rf.predict(X_test)
    print("Logistic accuracy:", accuracy_score(y_test, y_pred_log))
    print("Random Forest accuracy:", accuracy_score(y_test, y_pred_rf))
    if xgboost is not None:
        y_pred_xgb = xgboost.predict(X_test)
        print("XGBoost accuracy:", accuracy_score(y_test, y_pred_xgb))
    with open(MODEL_DIR / "logistic_model.pkl", "wb") as f:
        pickle.dump(logistic, f)
    with open(MODEL_DIR / "random_forest_model.pkl", "wb") as f:
        pickle.dump(rf, f)
    if xgboost is not None:
        with open(MODEL_DIR / "xgboost_model.pkl", "wb") as f:
            pickle.dump(xgboost, f)
    feature_importance = pd.Series(rf.feature_importances_, index=FEATURES).sort_values(ascending=False)
    plt.figure(figsize=(8, 5))
    feature_importance.plot(kind="bar", color="#3b82f6")
    plt.title("Feature Importance from Random Forest")
    plt.tight_layout()
    plt.savefig(BASE / "feature_importance.png")
    plt.close()
    return logistic, rf, xgboost


def train_timeline(df):
    X = df[FEATURES]
    y = df["placement_month"]
    model = LinearRegression()
    model.fit(X, y)
    with open(MODEL_DIR / "timeline_model.pkl", "wb") as f:
        pickle.dump(model, f)
    return model


def main():
    df = load_data()
    train_models(df)
    train_timeline(df)
    print(f"Saved models to {MODEL_DIR}")


if __name__ == "__main__":
    main()
