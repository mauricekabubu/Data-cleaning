# Student Performance Prediction System

## Overview
This project is a **Machine Learning pipeline** that cleans student performance data and trains a model to predict a student's grade based on factors such as:

- Weekly self-study hours
- Attendance percentage
- Class participation
- Total score

The system performs the following steps:

1. Data Cleaning
2. Data Preprocessing
3. Model Training
4. Model Evaluation
5. Model Saving

The final trained model is saved and can later be used in applications such as dashboards, APIs, or web applications.

---

# Project Structure

```
project-folder
│
├── data/
│   └── student_performance.csv
│
├── clean_data/
│   └── clean.csv
│
├── clean_data/cleaned_data/
│   └── cleaned.csv
│
├── logistic_model.pkl
│
├── clean_data_script.py
├── train_model.py
└── README.md
```

---

# Features

✔ Cleans raw student performance datasets  
✔ Handles missing values safely  
✔ Removes duplicate records  
✔ Converts numeric columns to proper numeric format  
✔ Encodes categorical variables  
✔ Trains a **Logistic Regression Machine Learning model**  
✔ Evaluates model accuracy and classification metrics  
✔ Saves the trained model for later use  

---

# Technologies Used

- **Python**
- **Pandas** – Data manipulation
- **Scikit-learn** – Machine Learning
- **Joblib** – Model saving
- **OS module** – File handling

---

# Step 1: Data Cleaning

The first script cleans the raw dataset before training the machine learning model.

### What the cleaning process does:

1. Reads the raw CSV dataset.
2. Ensures the output directory exists.
3. Selects important columns:
   - `Student_id`
   - `Weekly_self_study_hours`
   - `attendance_percentage`
   - `class_participation`
   - `total_score`
   - `grade`
4. Removes rows with missing values.
5. Removes duplicate records.
6. Converts numeric columns into proper numeric data types.
7. Saves the cleaned dataset.

### Output

```
clean_data/clean.csv
```

---

# Step 2: Data Preprocessing

After cleaning, the training script:

1. Loads multiple cleaned CSV files.
2. Combines them into one dataset.
3. Normalizes column names (lowercase and trimmed).
4. Handles missing values:
   - Numeric columns → filled with **median**
   - Categorical columns → filled with **mode**

---

# Step 3: Encoding Categorical Data

Machine learning models cannot understand text values.

So categorical columns are converted into numbers using:

```
LabelEncoder
```

Example:

| Grade | Encoded |
|------|--------|
| A | 0 |
| B | 1 |
| C | 2 |

---

# Step 4: Feature Selection

The model uses the following **features**:

- Weekly study hours
- Attendance percentage
- Class participation
- Total score

The **target variable** is:

```
grade
```

Student ID is removed because it is not useful for prediction.

---

# Step 5: Train Test Split

The dataset is split into:

- **80% Training Data**
- **20% Testing Data**

```
train_test_split(test_size=0.2)
```

This ensures the model is tested on unseen data.

---

# Step 6: Model Training

The project uses a **Logistic Regression model**.

Logistic Regression is commonly used for **classification problems** where the output is a category such as grades.

```
model = LogisticRegression(max_iter=1000)
model.fit(x_train, y_train)
```

---

# Step 7: Model Evaluation

After training, the model is evaluated using:

### Accuracy Score

Shows how often the model predicts correctly.

### Classification Report

Includes:

- Precision
- Recall
- F1-score

Example output:

```
Model Accuracy: 0.87
```

---

# Step 8: Saving the Model

The trained model is saved using **Joblib**.

```
joblib.dump(model, "logistic_model.pkl")
```

Saved file:

```
logistic_model.pkl
```

This model can later be used for:

- Web APIs
- Dashboards
- Student analytics tools
- Prediction systems

---

# How to Run the Project

### 1 Install dependencies

```bash
pip install pandas scikit-learn joblib
```

---

### 2 Run the data cleaning script

```bash
python clean_data_script.py
```

---

### 3 Train the model

```bash
python train_model.py
```

---

# Example Use Case

Schools or educational platforms can use this system to:

- Predict student grades
- Identify struggling students early
- Improve academic performance monitoring

---

# Future Improvements

Possible upgrades:

- Add **Random Forest or XGBoost models**
- Build a **Flask API**
- Create a **student performance dashboard**
- Add **data visualization**
- Deploy as a **web application**

---

# Author

Maurice Kabubu

Aspiring **Software Developer & Data Scientist** interested in:

- Machine Learning
- Data Science
- Backend Development
- Building impactful software systems.

---
