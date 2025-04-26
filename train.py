import pandas as pd
import numpy as np
import joblib
from sklearn.model_selection import train_test_split

# Load the Kaggle credit card fraud dataset
data = pd.read_csv('data/creditcard.csv')

# Rename 'Class' to 'fraud' for clarity
data = data.rename(columns={'Class': 'fraud'})

# Define feature columns
feature_cols = [
    'Time',
    'V1', 'V2', 'V3', 'V4', 'V5', 'V6', 'V7', 'V8', 'V9',
    'V10', 'V11', 'V12', 'V13', 'V14', 'V15', 'V16', 'V17',
    'V18', 'V19', 'V20', 'V21', 'V22', 'V23', 'V24', 'V25',
    'V26', 'V27', 'V28', 'Amount'
]

X = data[feature_cols].values
y = data['fraud'].values

# Split data
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

# Helper functions
def sigmoid(z):
    return 1 / (1 + np.exp(-z))

def compute_cost(X, y, w, b):
    m = X.shape[0]
    z = np.dot(X, w) + b
    f = sigmoid(z)
    cost = -(1/m) * np.sum(y * np.log(f + 1e-15) + (1 - y) * np.log(1 - f + 1e-15))
    return cost

def compute_gradient(X, y, w, b):
    m = X.shape[0]
    z = np.dot(X, w) + b
    f = sigmoid(z)
    dj_dw = (1/m) * np.dot(X.T, (f - y))
    dj_db = (1/m) * np.sum(f - y)
    return dj_dw, dj_db

# Initialize parameters
w = np.zeros(X_train.shape[1])
b = 0
alpha = 0.01
num_iters = 1000

# Gradient descent
for i in range(num_iters):
    dj_dw, dj_db = compute_gradient(X_train, y_train, w, b)
    w -= alpha * dj_dw
    b -= alpha * dj_db
    if i % 100 == 0:
        cost = compute_cost(X_train, y_train, w, b)
        print(f"Iteration {i}: Cost {cost:.4f}")

# Save the model parameters
joblib.dump((w, b, feature_cols), 'model.joblib')
print("Model trained and saved to model.joblib")
