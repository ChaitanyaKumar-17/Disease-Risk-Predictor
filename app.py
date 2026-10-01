"""
app.py
------
Flask REST API for the Disease Risk Prediction backend.

Endpoints:
  GET  /api/symptoms          → list of all symptom names
  POST /api/predict           → predict disease from selected symptoms
  GET  /api/disease/<name>    → get disease description + precautions
  GET  /health                → health check
"""

import os
import numpy as np
import joblib
from flask import Flask, jsonify, request
from disease_info import get_disease_info, DISEASE_INFO, SEVERITY_COLOR

app = Flask(__name__)

# ── load model artifacts ──────────────────────────────────────────────────────
MODEL_DIR = "model"

model         = joblib.load(os.path.join(MODEL_DIR, "disease_rf_model.pkl"))
label_encoder = joblib.load(os.path.join(MODEL_DIR, "label_encoder.pkl"))
symptom_cols  = joblib.load(os.path.join(MODEL_DIR, "symptom_columns.pkl"))

print(f"[INFO] Model loaded — {len(label_encoder.classes_)} diseases, {len(symptom_cols)} symptoms")


# ── routes ────────────────────────────────────────────────────────────────────

@app.route("/health", methods=["GET"])
def health():
    return jsonify({"status": "ok"})


@app.route("/api/symptoms", methods=["GET"])
def get_symptoms():
    """Return a clean, sorted list of all symptom names."""
    cleaned = sorted(set(s.strip().replace("_", " ").title() for s in symptom_cols))
    return jsonify({"symptoms": symptom_cols, "display_names": cleaned})


@app.route("/api/predict", methods=["POST"])
def predict():
    """
    Request body (JSON):
      { "symptoms": ["itching", "skin_rash", "fatigue"] }

    Response (JSON):
      {
        "predicted_disease": "Fungal infection",
        "confidence": 0.93,
        "top_predictions": [
            {"disease": "Fungal infection", "probability": 0.93},
            ...
        ],
        "info": { "description": "...", "precautions": [...], "severity": "Low" }
      }
    """
    data = request.get_json(force=True)
    selected = data.get("symptoms", [])

    if not selected:
        return jsonify({"error": "No symptoms provided."}), 400

    # Build feature vector
    feature_vector = np.zeros(len(symptom_cols), dtype=np.int8)
    unrecognised = []
    for sym in selected:
        sym_clean = sym.strip().lower().replace(" ", "_")
        if sym_clean in symptom_cols:
            feature_vector[symptom_cols.index(sym_clean)] = 1
        else:
            unrecognised.append(sym)

    # Predict
    proba = model.predict_proba(feature_vector.reshape(1, -1))[0]
    top_indices = np.argsort(proba)[::-1][:5]

    top_predictions = [
        {
            "disease": label_encoder.classes_[i].strip(),
            "probability": round(float(proba[i]), 4),
        }
        for i in top_indices
    ]

    predicted = top_predictions[0]["disease"]
    confidence = top_predictions[0]["probability"]
    info = get_disease_info(predicted)

    return jsonify({
        "predicted_disease": predicted,
        "confidence": confidence,
        "top_predictions": top_predictions,
        "info": info,
        "unrecognised_symptoms": unrecognised,
    })


@app.route("/api/disease/<path:disease_name>", methods=["GET"])
def disease_detail(disease_name):
    info = get_disease_info(disease_name)
    return jsonify({"disease": disease_name, **info})


@app.route("/api/diseases", methods=["GET"])
def all_diseases():
    result = []
    for d in sorted(label_encoder.classes_):
        info = get_disease_info(d.strip())
        result.append({
            "name": d.strip(),
            "severity": info["severity"],
            "severity_color": SEVERITY_COLOR.get(info["severity"], "#6b7280"),
        })
    return jsonify({"diseases": result})


# ── entry point ───────────────────────────────────────────────────────────────
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=False)
