"""
frontend.py
-----------
Streamlit frontend for the Disease Risk Prediction system.
Run: streamlit run frontend.py
Requires the Flask API to be running on http://localhost:5000
"""

import streamlit as st
import requests
import plotly.graph_objects as go
import plotly.express as px
import pandas as pd
import joblib
import os

# ── page config ───────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="Disease Risk Predictor",
    page_icon="🏥",
    layout="wide",
    initial_sidebar_state="expanded",
)

API_BASE = "http://localhost:5000"

# ── custom CSS ────────────────────────────────────────────────────────────────
st.markdown("""
<style>
    .main-header {
        font-size: 2.4rem;
        font-weight: 700;
        color: #1e3a5f;
        margin-bottom: 0.2rem;
    }
    .sub-header {
        font-size: 1rem;
        color: #57606a;
        margin-bottom: 1.5rem;
    }
    .result-card {
        background: #f0f7ff;
        border-left: 5px solid #3b82f6;
        border-radius: 8px;
        padding: 1.2rem 1.5rem;
        margin: 0.5rem 0;
    }
    .severity-badge {
        display: inline-block;
        padding: 3px 12px;
        border-radius: 20px;
        font-weight: 600;
        font-size: 0.85rem;
    }
    .disease-name {
        font-size: 1.8rem;
        font-weight: 700;
        color: #1e3a5f;
    }
    .confidence-text {
        font-size: 1.1rem;
        color: #374151;
    }
    .precaution-item {
        padding: 4px 0;
        color: #374151;
    }
    .disclaimer {
        background: #fff8e1;
        border-left: 4px solid #f59e0b;
        border-radius: 6px;
        padding: 0.8rem 1rem;
        font-size: 0.85rem;
        color: #92400e;
        margin-top: 1rem;
    }
    .metric-card {
        background: white;
        border: 1px solid #e5e7eb;
        border-radius: 8px;
        padding: 1rem;
        text-align: center;
    }
</style>
""", unsafe_allow_html=True)


# ── helper functions ──────────────────────────────────────────────────────────

@st.cache_data(ttl=300)
def fetch_symptoms():
    try:
        r = requests.get(f"{API_BASE}/api/symptoms", timeout=5)
        r.raise_for_status()
        data = r.json()
        return data["symptoms"], data["display_names"]
    except Exception:
        # fallback: load directly from saved model artifact
        if os.path.exists("model/symptom_columns.pkl"):
            cols = joblib.load("model/symptom_columns.pkl")
            display = sorted(set(s.strip().replace("_", " ").title() for s in cols))
            return cols, display
        return [], []


@st.cache_data(ttl=300)
def fetch_all_diseases():
    try:
        r = requests.get(f"{API_BASE}/api/diseases", timeout=5)
        r.raise_for_status()
        return r.json()["diseases"]
    except Exception:
        return []


def call_predict(symptoms: list[str]) -> dict | None:
    try:
        r = requests.post(
            f"{API_BASE}/api/predict",
            json={"symptoms": symptoms},
            timeout=10,
        )
        r.raise_for_status()
        return r.json()
    except requests.exceptions.ConnectionError:
        st.error("⚠️ Cannot reach the Flask API. Make sure `app.py` is running on port 5000.")
        return None
    except Exception as e:
        st.error(f"Prediction error: {e}")
        return None


def severity_color(severity: str) -> str:
    return {
        "Low":      "#22c55e",
        "Moderate": "#f59e0b",
        "High":     "#ef4444",
        "Critical": "#7c3aed",
    }.get(severity, "#6b7280")


def confidence_gauge(value: float) -> go.Figure:
    fig = go.Figure(go.Indicator(
        mode="gauge+number",
        value=round(value * 100, 1),
        number={"suffix": "%", "font": {"size": 28}},
        title={"text": "Prediction Confidence", "font": {"size": 14}},
        gauge={
            "axis": {"range": [0, 100], "tickwidth": 1},
            "bar": {"color": "#3b82f6"},
            "steps": [
                {"range": [0,  40], "color": "#fee2e2"},
                {"range": [40, 70], "color": "#fef9c3"},
                {"range": [70, 100], "color": "#dcfce7"},
            ],
            "threshold": {
                "line": {"color": "#1e3a5f", "width": 3},
                "thickness": 0.75,
                "value": value * 100,
            },
        },
    ))
    fig.update_layout(height=220, margin=dict(t=30, b=0, l=20, r=20))
    return fig


def top5_bar_chart(top_predictions: list) -> go.Figure:
    diseases = [p["disease"] for p in reversed(top_predictions)]
    probs    = [round(p["probability"] * 100, 2) for p in reversed(top_predictions)]
    colors   = ["#3b82f6" if i == len(diseases) - 1 else "#93c5fd" for i in range(len(diseases))]

    fig = go.Figure(go.Bar(
        x=probs,
        y=diseases,
        orientation="h",
        marker_color=colors,
        text=[f"{p}%" for p in probs],
        textposition="outside",
    ))
    fig.update_layout(
        title="Top 5 Predicted Diseases",
        xaxis_title="Probability (%)",
        height=280,
        margin=dict(t=40, b=20, l=10, r=60),
        xaxis=dict(range=[0, 110]),
        plot_bgcolor="white",
        paper_bgcolor="white",
    )
    return fig


# ── sidebar ───────────────────────────────────────────────────────────────────
with st.sidebar:
    st.markdown("""
<svg xmlns="http://www.w3.org/2000/svg" width="72" height="72" viewBox="0 0 64 64">
  <rect width="64" height="64" rx="12" fill="#1e3a5f"/>
  <rect x="28" y="10" width="8" height="44" rx="3" fill="white"/>
  <rect x="10" y="28" width="44" height="8" rx="3" fill="white"/>
</svg>
""", unsafe_allow_html=True)
    st.markdown("## 🏥 Disease Risk Predictor")
    st.markdown("---")
    st.markdown("""
**How to use:**
1. Select the symptoms you are experiencing
2. Click **Predict Disease**
3. Review the prediction and precautions

> 🔴 This tool is for **educational purposes only**.  
> Always consult a qualified doctor for diagnosis.
""")
    st.markdown("---")
    page = st.radio("Navigation", ["🔍 Predict", "📋 Disease Explorer", "ℹ️ About"])


# ── load data ─────────────────────────────────────────────────────────────────
symptom_cols, display_names = fetch_symptoms()

# map display → raw column key
display_to_raw = {}
if symptom_cols and display_names:
    for raw, disp in zip(symptom_cols, sorted(set(s.strip().replace("_", " ").title() for s in symptom_cols))):
        display_to_raw[disp] = raw


# ══════════════════════════════════════════════════════════════════════════════
# PAGE 1 — PREDICT
# ══════════════════════════════════════════════════════════════════════════════
if page == "🔍 Predict":
    st.markdown('<div class="main-header">🏥 Disease Risk Prediction</div>', unsafe_allow_html=True)
    st.markdown('<div class="sub-header">Select your symptoms to get an AI-powered disease risk assessment.</div>', unsafe_allow_html=True)

    if not symptom_cols:
        st.warning("Could not load symptoms. Ensure `train_model.py` has been run and model artifacts exist.")
        st.stop()

    # ── symptom selection ─────────────────────────────────────────────────────
    col_left, col_right = st.columns([2, 1])

    with col_left:
        st.markdown("### 📝 Select Symptoms")
        # Group symptoms alphabetically with a searchable multiselect
        selected_display = st.multiselect(
            "Search and select symptoms:",
            options=display_names,
            placeholder="Type to search symptoms…",
            help="You can select multiple symptoms.",
        )

        # Quick category shortcuts
        st.markdown("**Quick-select common groups:**")
        qc1, qc2, qc3, qc4 = st.columns(4)
        quick_add = []
        if qc1.button("🤧 Respiratory"):
            quick_add = ["Cough", "Breathlessness", "Phlegm", "Congestion", "Runny Nose"]
        if qc2.button("🤢 Digestive"):
            quick_add = ["Nausea", "Vomiting", "Abdominal Pain", "Diarrhoea", "Indigestion"]
        if qc3.button("🔥 Fever-related"):
            quick_add = ["High Fever", "Fatigue", "Sweating", "Chills", "Headache"]
        if qc4.button("🦴 Joint/Muscle"):
            quick_add = ["Joint Pain", "Muscle Weakness", "Back Pain", "Knee Pain", "Stiff Neck"]

        if quick_add:
            for qa in quick_add:
                if qa in display_names and qa not in selected_display:
                    selected_display.append(qa)

    with col_right:
        st.markdown("### 📊 Selected")
        st.metric("Symptoms chosen", len(selected_display))
        if selected_display:
            for sym in selected_display:
                st.markdown(f"✅ {sym}")

    st.markdown("---")

    # ── predict button ────────────────────────────────────────────────────────
    predict_btn = st.button("🔬 Predict Disease", type="primary", use_container_width=True)

    if predict_btn:
        if len(selected_display) < 2:
            st.warning("Please select at least 2 symptoms for a meaningful prediction.")
        else:
            # Map display names back to raw column keys
            raw_symptoms = [display_to_raw.get(d, d.lower().replace(" ", "_")) for d in selected_display]

            with st.spinner("Analysing symptoms…"):
                result = call_predict(raw_symptoms)

            if result:
                st.markdown("---")
                st.markdown("## 🩺 Prediction Results")

                disease  = result["predicted_disease"]
                conf     = result["confidence"]
                info     = result["info"]
                top5     = result["top_predictions"]
                severity = info.get("severity", "Unknown")
                sev_color = severity_color(severity)

                # ── main result card ──────────────────────────────────────────
                r1, r2, r3 = st.columns([3, 1.5, 1.5])

                with r1:
                    st.markdown(f"""
<div class="result-card">
  <div class="disease-name">🦠 {disease}</div>
  <span class="severity-badge" style="background:{sev_color}22; color:{sev_color}; border:1px solid {sev_color}">
    ⚡ {severity} Severity
  </span>
  <p style="margin-top:0.8rem; color:#374151;">{info.get('description','')}</p>
</div>
""", unsafe_allow_html=True)

                with r2:
                    st.plotly_chart(confidence_gauge(conf), use_container_width=True)

                with r3:
                    st.markdown("#### 🛡️ Precautions")
                    for prec in info.get("precautions", []):
                        st.markdown(f"• {prec}")

                # ── top 5 chart ───────────────────────────────────────────────
                st.markdown("#### 📈 Differential Diagnosis")
                st.plotly_chart(top5_bar_chart(top5), use_container_width=True)

                # ── detailed top-5 table ──────────────────────────────────────
                df_top = pd.DataFrame(top5)
                df_top["probability"] = df_top["probability"].apply(lambda x: f"{x*100:.2f}%")
                df_top.columns = ["Disease", "Confidence"]
                df_top.index = df_top.index + 1
                st.dataframe(df_top, use_container_width=True)

                # ── disclaimer ────────────────────────────────────────────────
                st.markdown("""
<div class="disclaimer">
⚠️ <strong>Medical Disclaimer:</strong> This prediction is generated by a machine learning model 
trained on symptom data and is intended for <strong>educational and informational purposes only</strong>. 
It is <strong>not a substitute for professional medical advice, diagnosis, or treatment</strong>. 
Always consult a qualified healthcare provider for any medical concerns.
</div>
""", unsafe_allow_html=True)


# ══════════════════════════════════════════════════════════════════════════════
# PAGE 2 — DISEASE EXPLORER
# ══════════════════════════════════════════════════════════════════════════════
elif page == "📋 Disease Explorer":
    st.markdown('<div class="main-header">📋 Disease Explorer</div>', unsafe_allow_html=True)
    st.markdown('<div class="sub-header">Browse all 41 diseases the model can predict, along with descriptions and severity.</div>', unsafe_allow_html=True)

    diseases = fetch_all_diseases()

    if not diseases:
        st.info("Start the Flask API (`python app.py`) to load disease data.")
    else:
        # Severity filter
        severities = ["All", "Low", "Moderate", "High", "Critical"]
        sel_sev = st.selectbox("Filter by severity:", severities)

        if sel_sev != "All":
            diseases = [d for d in diseases if d["severity"] == sel_sev]

        # Severity distribution pie
        sev_counts = pd.DataFrame(diseases).groupby("severity").size().reset_index(name="count")
        if not sev_counts.empty:
            color_map = {"Low": "#22c55e", "Moderate": "#f59e0b", "High": "#ef4444", "Critical": "#7c3aed", "Unknown": "#6b7280"}
            fig_pie = px.pie(
                sev_counts,
                names="severity",
                values="count",
                color="severity",
                color_discrete_map=color_map,
                title="Severity Distribution",
                hole=0.4,
            )
            fig_pie.update_layout(height=300, margin=dict(t=40, b=0))
            st.plotly_chart(fig_pie, use_container_width=True)

        # Disease cards
        st.markdown(f"### Showing {len(diseases)} disease(s)")
        for disease in diseases:
            sev_col = disease.get("severity_color", "#6b7280")
            sev = disease.get("severity", "Unknown")
            with st.expander(f"🦠 {disease['name']}  —  Severity: {sev}"):
                from disease_info import get_disease_info
                info = get_disease_info(disease["name"])
                st.markdown(f"**Description:** {info['description']}")
                st.markdown("**Precautions:**")
                for p in info.get("precautions", []):
                    st.markdown(f"  • {p}")


# ══════════════════════════════════════════════════════════════════════════════
# PAGE 3 — ABOUT
# ══════════════════════════════════════════════════════════════════════════════
elif page == "ℹ️ About":
    st.markdown('<div class="main-header">ℹ️ About This Project</div>', unsafe_allow_html=True)

    c1, c2 = st.columns(2)
    with c1:
        st.markdown("""
### 🎯 Project Goal
This project demonstrates an end-to-end **Disease Risk Prediction System** built using:
- **Scikit-learn** Random Forest classifier
- **Flask** REST API backend
- **Streamlit** Python-native frontend
- **Plotly** interactive visualisations

### 📊 Dataset
- **132 binary symptom features** (0/1)
- **41 disease classes** to predict
- **4,920 training samples** · **42 test samples**
- Source: [Kaggle Disease Symptom Dataset](https://www.kaggle.com/)
""")
    with c2:
        st.markdown("""
### 🏗️ Architecture

```
Training.csv / Testing.csv
        │
        ▼
  train_model.py
  (Random Forest)
        │
        ▼
  model/*.pkl  ─────────────▶  app.py (Flask API :5000)
                                        │
                                        ▼
                              frontend.py (Streamlit :8501)
```

### ⚙️ Tech Stack
| Layer | Technology |
|---|---|
| ML Model | scikit-learn RandomForest |
| Backend API | Flask |
| Frontend | Streamlit |
| Charts | Plotly |
| Data | pandas / numpy |
""")

    st.markdown("---")
    st.markdown("""
### 📁 Project Files
| File | Purpose |
|---|---|
| `train_model.py` | Data preprocessing + model training + saving |
| `app.py` | Flask REST API serving predictions |
| `frontend.py` | Streamlit UI |
| `disease_info.py` | Disease descriptions & precautions lookup |
| `Training.csv` | Training dataset |
| `Testing.csv` | Test dataset |
| `model/` | Saved model artifacts (pkl files) |

### ⚠️ Disclaimer
This system is built for **educational purposes** only. The predictions are based on a 
machine learning model and **should not replace professional medical consultation**.
""")

    st.markdown("---")
    st.caption("Built with Python · scikit-learn · Flask · Streamlit · Plotly")
