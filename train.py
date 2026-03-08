import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report
import joblib

# Step 1: Load multiple CSVs
files = ["clean_data/clean.csv", "clean_data/cleaned_data/cleaned.csv"]
data_list = [pd.read_csv(f) for f in files]
data = pd.concat(data_list, ignore_index=True)

# Step 2: Normalize column names
data.columns = [col.lower().strip() for col in data.columns]

# Step 3: Fill missing values safely
# Numeric columns
numeric_cols = data.select_dtypes(include=['int64', 'float64']).columns
for col in numeric_cols:
    median_value = data[col].median()
    data[col] = data[col].fillna(median_value)

# Categorical columns
categorical_cols = data.select_dtypes(include=['object', 'string']).columns
for col in categorical_cols:
    mode_value = data[col].mode()[0]
    data[col] = data[col].fillna(mode_value)

# Step 4: Label encode categorical columns
label_encoders = {}
for col in categorical_cols:
    le = LabelEncoder()
    data[col] = le.fit_transform(data[col])
    label_encoders[col] = le

# Step 5: Features and target
target_column = "grade"
X = data.drop(["student_id", target_column], axis=1, errors='ignore')
y = data[target_column]

# Step 6: Train-test split
x_train, x_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Step 7: Train Logistic Regression
model = LogisticRegression(max_iter=1000)
model.fit(x_train, y_train)

# Step 8: Predict & Evaluate
y_pred = model.predict(x_test)
print("Model Accuracy:", accuracy_score(y_test, y_pred))
print(classification_report(y_test, y_pred))

# Step 9: Save the model
joblib.dump(model, "logistic_model.pkl")
print("Model saved as logistic_model.pkl")
print("Script started successfully")