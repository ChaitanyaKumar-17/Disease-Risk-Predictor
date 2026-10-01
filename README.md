# 🏥 Disease Risk Prediction System

An end-to-end machine learning web application that predicts diseases from reported symptoms using a Random Forest classifier, served via a Flask API and visualised with a Streamlit frontend.

---

## 📁 Project Structure

```
.
├── Training.csv           # Training dataset (4,920 samples, 132 symptoms, 41 diseases)
├── Testing.csv            # Testing dataset
├── train_model.py         # ML pipeline: preprocessing, training, evaluation, saving
├── app.py                 # Flask REST API backend
├── frontend.py            # Streamlit frontend UI
├── disease_info.py        # Disease descriptions & precautions lookup table
├── requirements.txt       # Python dependencies
├── model/                 # Auto-created after training
│   ├── disease_rf_model.pkl
│   ├── label_encoder.pkl
│   └── symptom_columns.pkl
└── README.md
```

---

## ⚙️ Setup & Installation

### 1. Install dependencies
```bash
pip install -r requirements.txt
```

### 2. Train the model
```bash
python train_model.py
```
This will train a Random Forest on `Training.csv`, evaluate it on `Testing.csv`, and save the model artifacts to `model/`.

### 3. Start the Flask API (Terminal 1)
```bash
python app.py
```
The API runs at `http://localhost:5000`

### 4. Launch the Streamlit frontend (Terminal 2)
```bash
streamlit run frontend.py
```
The app opens at `http://localhost:8501`

---

## 🔗 API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/health` | API health check |
| GET | `/api/symptoms` | Returns all 132 symptom names |
| POST | `/api/predict` | Predict disease from symptoms |
| GET | `/api/disease/<name>` | Get disease info by name |
| GET | `/api/diseases` | List all diseases with severity |

### Example: POST `/api/predict`
```json
// Request
{
  "symptoms": ["itching", "skin_rash", "nodal_skin_eruptions"]
}

// Response
{
  "predicted_disease": "Fungal infection",
  "confidence": 0.955,
  "top_predictions": [
    {"disease": "Fungal infection", "probability": 0.955},
    {"disease": "Acne", "probability": 0.020},
    ...
  ],
  "info": {
    "description": "A fungal infection ...",
    "precautions": ["Keep skin clean and dry", ...],
    "severity": "Low"
  }
}
```

---

## 🧠 Model Details

| Property | Value |
|----------|-------|
| Algorithm | Random Forest Classifier |
| Estimators | 200 trees |
| Features | 132 binary symptom columns |
| Classes | 41 diseases |
| Training samples | 4,920 |
| Test samples | 42 |
| Expected Test Accuracy | ~98–100% |

---

## 🖥️ Frontend Pages

| Page | Description |
|------|-------------|
| 🔍 Predict | Select symptoms → get prediction + confidence gauge + top-5 differential diagnosis chart |
| 📋 Disease Explorer | Browse all 41 diseases filtered by severity with descriptions and precautions |
| ℹ️ About | Architecture overview, tech stack, and project details |

---

## ⚠️ Disclaimer

This tool is built for **educational and demonstration purposes only**. It is **not a substitute for professional medical advice, diagnosis, or treatment**. Always consult a qualified healthcare provider.

---

## 🛠️ Tech Stack

- **Machine Learning:** scikit-learn (RandomForestClassifier)
- **Backend:** Flask
- **Frontend:** Streamlit
- **Visualisation:** Plotly
- **Data Processing:** pandas, numpy
