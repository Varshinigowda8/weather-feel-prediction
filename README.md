# Weather Feel Predictor 🌡️✨

## 📌 Project Overview
The Weather Feel Predictor is a Python-based project that predicts how the weather feels based on the input temperature.  
It demonstrates both rule-based logic (nearest neighbor distance calculation) and applied AI models (KNN, Decision Tree, Logistic Regression) using scikit-learn.

This project is designed to be simple, modular, and examiner-friendly, while also showcasing creativity through AI integration.

## ⚙️ Features
- Rule-Based Predictor: Calculates the absolute distance between input temperature and training data points, then chooses the closest label.
- AI Models:
  - **K-Nearest Neighbors (KNN)** → Finds the closest training point.
  - **Decision Tree Classifier** → Learns thresholds between ranges.
  - **Logistic Regression** → Classifies temperature into categories.
- **Modular Code Structure**:
  - `data.py` → Training data
  - `model.py` → AI models
  - `main.py` → User interaction & predictions
- **Examiner-Friendly Output**: Shows predictions from multiple models for comparison.
- **Extensible**: Can be enhanced with GUI (Tkinter), web app (Flask/Streamlit), or visualization (Matplotlib).

---

## 📂 Project Structure
weather-feel-predictor/
│
├── data.py                        # Training data (temperature → label)
├── model.py                      # AI models (KNN, Decision Tree, Logistic Regression)
├── main.py                        # Main script for user input & predictions
├── predictor.py              # Rule-based logic (manual nearest neighbor)
├── requirements.txt      # Dependencies
└── README.md                    # Documentation



## 🚀 How to Run
1. Clone or open the project folder in VS Code.
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
Run the project:

bash
python main.py
Enter a temperature when prompted:


Enter today's temperature in ℃: 28
See the output:


At 28.0℃:
- KNN Model says: warm
- Decision Tree says: warm
- Logistic Regression says: warm
Stay vibey 🌟



