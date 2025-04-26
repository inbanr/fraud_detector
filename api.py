from flask import Flask, request, jsonify
import joblib
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, roc_auc_score

app = Flask(__name__)
w, b, feature_cols = joblib.load('model.joblib')

# Load data for metrics endpoint
data = pd.read_csv('data/creditcard.csv')
data = data.rename(columns={'Class': 'fraud'})
X = data[feature_cols].values
y = data['fraud'].values

_, X_test, _, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

def sigmoid(z):
    return 1 / (1 + np.exp(-z))

@app.route('/metrics', methods=['GET'])
def metrics():
    z = np.dot(X_test, w) + b
    y_prob = sigmoid(z)
    y_pred = (y_prob >= 0.5).astype(int)

    report = classification_report(y_test, y_pred, output_dict=True)
    auc = roc_auc_score(y_test, y_prob)
    return jsonify({'classification_report': report, 'auc_roc': auc})

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json
    x = np.array([data[col] for col in feature_cols])
    z = np.dot(x, w) + b
    prob = sigmoid(z)
    pred = int(prob >= 0.5)
    return jsonify({'fraud_probability': prob, 'predicted_fraud': pred})

if __name__ == '__main__':
    app.run(debug=True)
