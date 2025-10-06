import pandas as pd

def main():
    # Load the cleaned evidence CSV
    df = pd.read_csv("OUTPUT2.csv")  # change this if your file is named cleaned_evidence.csv

    # Ensure timestamp is in datetime format
    df['timestamp'] = pd.to_datetime(df['timestamp'], errors='coerce')

    # Feature engineering
    df['hour_of_day'] = df['timestamp'].dt.hour
    df['day_of_week'] = df['timestamp'].dt.day_name()
    df['is_weekend'] = df['timestamp'].dt.dayofweek >= 5  # Saturday=5, Sunday=6

    # Save the new file
    df.to_csv("feature_engineered_evidence.csv", index=False)
    print("✅ Feature engineered file saved as feature_engineered_evidence.csv")

if __name__ == "__main__":
    main()
