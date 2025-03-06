# fraud_detector
AI-powered fraud detection system using XGBoost to identify suspicious transactions in real time. Built with React, Next.js, FastAPI, and PostgreSQL, with Dask for scalable data processing. Combines full-stack development and machine learning to enhance payment security.


# AI-Powered Fraud Detection System

## Overview
This project is a full-stack **fraud detection system** that leverages **machine learning (XGBoost)** to detect suspicious financial transactions in real time. It integrates **AI-driven anomaly detection** with an interactive dashboard for financial analysts, enhancing payment security and transparency.

## Features
- 🚀 Real-time transaction monitoring with fraud flagging
- 🔍 AI-powered fraud detection using **XGBoost**
- 📊 Interactive dashboard built with **React** and **Next.js** for visualization
- ⚡ Efficient data processing using **Dask** for large-scale financial data
- 🗄️ Backend API built with **FastAPI**, connected to **PostgreSQL** for secure data storage
- 📬 Supports real-time alert generation for high-risk transactions

## Tech Stack
- **Backend:** FastAPI, Python, Dask, XGBoost, PostgreSQL
- **Frontend:** React, Next.js, TypeScript
- **Machine Learning:** XGBoost for classification, MinMaxScaler for preprocessing
- **Data Processing:** Dask for scalable data handling

## How It Works
1. Transactions are ingested and stored in PostgreSQL.
2. Data is processed using **Dask** to handle large volumes efficiently.
3. Transactions are evaluated by a **pre-trained XGBoost model**, which assigns a fraud probability.
4. Results are displayed in a **React dashboard**, with high-risk transactions flagged for review.
5. Analysts can drill down into individual transactions, viewing features that contributed to the risk score.

## Installation
1. Clone the repository:
    ```bash
    git clone https://github.com/YOUR_USERNAME/fraud-detection-system.git
    ```
2. Install backend dependencies:
    ```bash
    cd backend
    pip install -r requirements.txt
    ```
3. Install frontend dependencies:
    ```bash
    cd frontend
    npm install
    ```
4. Run backend:
    ```bash
    cd backend
    uvicorn main:app --reload
    ```
5. Run frontend:
    ```bash
    cd frontend
    npm run dev
    ```

## Future Enhancements
- Add real-time webhook integration for instant fraud alerts.
- Enhance ML model with ensemble methods for improved accuracy.
- Add user role management for different analyst permissions.

## Folder Structure
fraud-detection-system/
├── backend/
│   ├── main.py                # Main FastAPI app (loading the model, handling API requests)
│   ├── model.py               # Code to load and use XGBoost model for predictions
│   ├── data_preprocessing.py   # (Optional) Data cleaning and preprocessing functions
│   ├── requirements.txt        # Python dependencies (FastAPI, Dask, XGBoost, etc.)
│   └── fraud_detection_xgb.model  # Saved XGBoost model file
│
├── frontend/
│   ├── components/             # React reusable components (tables, charts, etc.)
│   ├── pages/                   # Next.js pages (Dashboard, TransactionDetails, etc.)
│   ├── public/                  # Static assets if needed
│   ├── styles/                  # CSS or Tailwind configurations
│   ├── utils/                    # Helper functions (formatting dates, numbers, etc.)
│   ├── package.json             # Frontend dependencies
│   └── next.config.js           # Next.js configuration
│
├── data/
│   ├── creditcard_2023.csv      # Original dataset (optional, or use a sample file)
│   ├── processed_transactions.csv  # Processed data after Dask and normalization
│
├── .gitignore                    # Ignore unnecessary files (e.g., venv, node_modules)
├── README.md                     # Project description (use the one I drafted)
└── LICENSE                       # Optional (MIT License or other)

## Skills Demonstrated
- Full-Stack Development
- Machine Learning (XGBoost)
- Scalable Data Processing (Dask)
- API Development (FastAPI)
- Frontend Development (React + Next.js)
- Database Management (PostgreSQL)

---

## License
MIT License

---

### Author
Inban Rajamani

---

