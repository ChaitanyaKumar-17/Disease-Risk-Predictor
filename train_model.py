"""
train_model.py
--------------
Trains a Random Forest classifier on the disease symptom dataset and saves:
  - model/disease_rf_model.pkl   : trained model
  - model/label_encoder.pkl      : label encoder (disease names)
  - model/symptom_columns.pkl    : ordered list of symptom feature columns
"""

import os
import pandas as pd
import numpy as np
import joblib
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import accuracy_score, classification_report

# ── paths ────────────────────────────────────────────────────────────────────
TRAIN_CSV  = "Training.csv"
TEST_CSV   = "Testing.csv"
MODEL_DIR  = "model"
os.makedirs(MODEL_DIR, exist_ok=True)

# ── load data ────────────────────────────────────────────────────────────────
print("Loading datasets …")
train_df = pd.read_csv(TRAIN_CSV)
test_df  = pd.read_csv(TEST_CSV)

# Drop trailing unnamed column if present
train_df = train_df.loc[:, ~train_df.columns.str.startswith("Unnamed")]
test_df  = test_df.loc[:,  ~test_df.columns.str.startswith("Unnamed")]

TARGET = "prognosis"

# ── feature / label split ────────────────────────────────────────────────────
symptom_cols = [c for c in train_df.columns if c != TARGET]

X_train = train_df[symptom_cols].values.astype(np.int8)
y_train_raw = train_df[TARGET].str.strip()

X_test  = test_df[symptom_cols].values.astype(np.int8)
y_test_raw  = test_df[TARGET].str.strip()

# ── label encode ─────────────────────────────────────────────────────────────
le = LabelEncoder()
le.fit(sorted(y_train_raw.unique()))
y_train = le.transform(y_train_raw)
y_test  = le.transform(y_test_raw)

print(f"Features   : {len(symptom_cols)}")
print(f"Diseases   : {len(le.classes_)}")
print(f"Train rows : {X_train.shape[0]}")
print(f"Test rows  : {X_test.shape[0]}")

# ── train ─────────────────────────────────────────────────────────────────────
print("\nTraining Random Forest …")
model = RandomForestClassifier(
    n_estimators=200,
    max_depth=None,
    random_state=42,
    n_jobs=-1,
)
model.fit(X_train, y_train)

# ── evaluate ──────────────────────────────────────────────────────────────────
y_pred = model.predict(X_test)
acc = accuracy_score(y_test, y_pred)
print(f"\nTest Accuracy : {acc * 100:.2f}%")
print("\nClassification Report:")
print(classification_report(y_test, y_pred, target_names=le.classes_))

# ── save artifacts ────────────────────────────────────────────────────────────
joblib.dump(model,        os.path.join(MODEL_DIR, "disease_rf_model.pkl"))
joblib.dump(le,           os.path.join(MODEL_DIR, "label_encoder.pkl"))
joblib.dump(symptom_cols, os.path.join(MODEL_DIR, "symptom_columns.pkl"))
print(f"\nModel artifacts saved to '{MODEL_DIR}/'")
