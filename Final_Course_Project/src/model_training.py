import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import roc_auc_score, average_precision_score

def train_model(path="synthetic_dataset.csv"):
    df = pd.read_csv(path)
    X = df.drop("default", axis=1)
    y = df["default"]

    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)

    X_train, X_test, y_train, y_test = train_test_split(
        X_scaled, y, test_size=0.2, random_state=42, stratify=y
    )

    model = RandomForestClassifier(
        n_estimators=200,
        max_depth=10,
        random_state=42
    )

    model.fit(X_train, y_train)
    y_pred = model.predict_proba(X_test)[:, 1]

    return {
        "roc_auc": roc_auc_score(y_test, y_pred),
        "pr_auc": average_precision_score(y_test, y_pred),
        "model": model
    }
