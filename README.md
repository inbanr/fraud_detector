# Credit Card Fraud Detection

This project is a complete end-to-end machine learning application that detects fraudulent credit card transactions using **Logistic Regression trained with custom Gradient Descent**.  
It features a **React dashboard frontend** to visualize model performance.

We use the **Credit Card Fraud Detection** dataset from Kaggle:  
[https://www.kaggle.com/datasets/dhanushnarayananr/credit-card-fraud](https://www.kaggle.com/datasets/dhanushnarayananr/credit-card-fraud)

---

## 📂 Project Structure

```
fraud-detection/
├── backend/
│   ├── data/
│   │   └── creditcard.csv       # Place Kaggle dataset here
│   ├── model.joblib             # Saved model parameters (weights, bias)
│   ├── train.py                 # Train model manually using gradient descent
│   ├── api.py                   # Flask API serving predictions and metrics
│   └── requirements.txt         # Python dependencies
└── frontend/
    ├── src/
    │   ├── App.js
    │   ├── Dashboard.js
    │   └── index.js
    └── package.json             # React dependencies
```

---

## 🛠️ How it Works

- **Training**:
  - Manual Logistic Regression using custom **gradient descent**, **sigmoid activation**, and **loss function**.
  - No use of sklearn's `LogisticRegression` model.
  - Features `Time` and `Amount` are standardized before training.

- **Backend**:
  - Flask API (`api.py`) exposes:
    - `POST /predict`: Predict fraud probability.
    - `GET /metrics`: Return precision, recall, F1-score, and AUC-ROC.

- **Frontend**:
  - Built with React.js
  - Fetches metrics from the Flask backend.
  - Displays model performance using Chart.js graphs.

---

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/inbanr/fraud-detection.git
cd fraud-detection
```

---

### 2. Backend Setup

#### a. Install Python Dependencies

```bash
cd backend
python3 -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
pip install -r requirements.txt
```

#### b. Download and Place Dataset

- Download `creditcard.csv` from Kaggle:  
  [https://www.kaggle.com/datasets/dhanushnarayananr/credit-card-fraud](https://www.kaggle.com/datasets/dhanushnarayananr/credit-card-fraud)
- Place it inside the `backend/data/` folder.

#### c. Train the Model

```bash
python train.py
```

#### d. Start the Flask API

```bash
python api.py
```

The API will be available at: `http://localhost:5000`

---

### 3. Frontend Setup

```bash
cd ../frontend
npm install
npm start
```

The React app will be available at: `http://localhost:3000`

Make sure the backend Flask server is running on port 5000 before starting the frontend.

---

## 📈 Example Model Metrics

| Metric         | Example Value |
|:---------------|:--------------|
| Precision (Fraud) | 0.91 |
| Recall (Fraud)    | 0.87 |
| F1-Score (Fraud)  | 0.89 |
| AUC-ROC           | 0.97 |

*(Note: Actual results may vary depending on random splits.)*

---

## 📚 Tech Stack

- Machine Learning: Custom Logistic Regression (no sklearn models)
- Backend: Flask
- Frontend: React.js + Chart.js
- Data: Kaggle Credit Card Fraud Detection Dataset

---

## 📜 License

This project is open-source and free to use for educational and project purposes.

---

## ✨ Acknowledgements

- [Kaggle: Credit Card Fraud Detection Dataset](https://www.kaggle.com/datasets/dhanushnarayananr/credit-card-fraud)
- Deep Learning Specialization (Andrew Ng) for the Gradient Descent inspiration

---
