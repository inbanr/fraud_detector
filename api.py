from flask import Flask, request, jsonify
import joblib
import pandas as pd
from sklearn.metrics import classification_report, roc_auc_score
from sklearn.model_selection import train_test_split

app = Flask(__name__)
model = joblib.load('model.joblib')

# Load data for metrics endpoint
data = pd.read_csv('data/creditcard.csv')
data = data.rename(columns={'Class': 'fraud'})
feature_cols = [
    'Time',
    'V1','V2','V3','V4','V5','V6','V7','V8','V9','V10','V11','V12','V13','V14',
    'V15','V16','V17','V18','V19','V20','V21','V22','V23','V24','V25','V26','V27','V28',
    'Amount'
]
X = data[feature_cols]
y = data['fraud']

_, X_test, _, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

@app.route('/metrics', methods=['GET'])
def metrics():
    y_pred = model.predict(X_test)
    y_prob = model.predict_proba(X_test)[:, 1]
    report = classification_report(y_test, y_pred, output_dict=True)
    auc = roc_auc_score(y_test, y_prob)
    return jsonify({'classification_report': report, 'auc_roc': auc})

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json
    features = [data[col] for col in feature_cols]
    prob = model.predict_proba([features])[0][1]
    pred = int(prob >= 0.5)
    return jsonify({'fraud_probability': prob, 'predicted_fraud': pred})

if __name__ == '__main__':
    app.run(debug=True)
