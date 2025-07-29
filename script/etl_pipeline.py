import pandas as pd
def validate_and_clean(df):
    # Drop rows where 'name' or 'department' or 'salary' is missing
    df = df.dropna(subset=['name', 'department', 'salary']).copy()
    # Use .loc to set salary column
    df.loc[:, 'salary'] = pd.to_numeric(df['salary'], errors='coerce')
    df = df.dropna(subset=['salary'])
    # Convert joining_date to datetime
    df.loc[:, 'joining_date'] = pd.to_datetime(df['joining_date'], errors='coerce')
    df = df.dropna(subset=['joining_date'])
    # Standardize 'status'
    df.loc[:, 'status'] = df['status'].str.capitalize()
    return df

# Load input data
df = pd.read_csv('employee_data_raw.csv')

# Clean data using validation function
df_cleaned = validate_and_clean(df)

# Save cleaned data
df_cleaned.to_csv('employee_data_cleaned.csv', index=False)

# Generate department-wise average salary summary
summary = (
    df_cleaned.groupby('department')['salary']
    .mean()
    .reset_index()
    .rename(columns={'salary': 'avg_salary'})
)

summary.to_csv('summary_report.csv', index=False)
