import pandas as pd
import os

try:
    # File paths
    input_file = "data/student_dropout_dataset_v3.csv"
    output_file = "clean_data/cleaned_data/cleaned.csv"

    def clean_data(input_file, output_file):
        # Ensure output folder exists
        os.makedirs(os.path.dirname(output_file), exist_ok=True)
        
        # Read CSV
        df = pd.read_csv(input_file)
        
        # Columns we care about
        required_columns = ["Student_id","Internet_Access","Study_Hours",
                            "per_Day","Attendance_Rate","Assignment_Delay_Days",
                            "Stress_Index","GPA","Semester_GPA","CGPA","Semester",
                            "Department","Dropout"]
        
        # Keep only available required columns
        available_columns = [col for col in required_columns if col in df.columns]
        
        # Drop rows with missing values in required columns
        if available_columns:
            df.dropna(subset=available_columns, inplace=True)
        
        # Drop duplicates
        df.drop_duplicates(inplace=True)
        
        # Convert numeric columns to numbers (coerce errors to NaN)
        numeric_columns = ["Weekly_self_study_hours","attendance_percentage","class_participation","total_score"]
        for col in numeric_columns:
            if col in df.columns:
                df[col] = pd.to_numeric(df[col], errors="coerce")
        
        # Save cleaned data
        df.to_csv(output_file, index=False)
        print(f"Data cleaned and saved to {output_file}")

    # Run cleaning
    clean_data(input_file, output_file)
except Exception as e:
    print(f"Error occured in {e}")