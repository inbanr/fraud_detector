import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, roc_auc_score
import joblib

# Load the Kaggle credit card fraud dataset
data = pd.read_csv('data/creditcard.csv')

# Rename the 'Class' column to 'fraud' for clarity
data = data.rename(columns={'Class': 'fraud'})

# Define feature columns and target
feature_cols = [
    'Time',
    'V1','V2','V3','V4','V5','V6','V7','V8','V9','V10','V11','V12','V13','V14',
    'V15','V16','V17','V18','V19','V20','V21','V22','V23','V24','V25','V26','V27','V28',
    'Amount'
]
X = data[feature_cols]
y = data['fraud']

# Split data into train/test sets with stratification
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

# Initialize and train the logistic regression model
model = LogisticRegression(
    penalty='l2',
    C=1.0,
    class_weight='balanced',
    max_iter=1000,
    solver='liblinear'
)
model.fit(X_train, y_train)

# Evaluate the model on test data
y_pred = model.predict(X_test)
y_prob = model.predict_proba(X_test)[:, 1]
print(classification_report(y_test, y_pred))
print('AUC-ROC:', roc_auc_score(y_test, y_prob))

# Save the trained model
joblib.dump(model, 'model.joblib')
