import pandas as pd
import os

# 1. Define the file path (We are pretending this file exists for now)
DATA_FILE = 'sap_user_data.csv'

# 2. Read the file into a DataFrame
# Note: Since the file doesn't exist, we'll create a dummy one for testing.
try:
    df = pd.read_csv(DATA_FILE)
    print(f"Successfully loaded {DATA_FILE}")
except FileNotFoundError:
    print(f"--- FAKE DATA GENERATED FOR TEST ---")
    # Generating a fake DataFrame that has some missing values (NaN)
    data = {
        'User_ID': [1001, 1002, 1003, 1004, 1005],
        'Cost_Center': ['CC_A', 'CC_B', None, 'CC_D', 'CC_E'], # Missing value imperfection!
        'Role': ['Analyst', 'Manager', 'Analyst', 'Analyst', None] # Missing value imperfection!
    }
    df = pd.DataFrame(data)


# 3. Check for the most common imperfection: Missing values (NaN)
print("\n--- DATA INTEGRITY CHECK: MISSING VALUES ---")

# The .isnull() method checks every cell for a missing value (True/False)
# The .sum() method counts the number of True values (i.e., missing values) per column
missing_values_count = df.isnull().sum()

# 4. Print the results
print("Missing Value Count by Column:")
print(missing_values_count)

# Optional: If you want to know how many total missing values are in the entire dataset:
total_missing = df.isnull().sum().sum()
if total_missing > 0:
    print(f"\nAUDIT ALERT: Total missing values found: {total_missing}")
else:
    print("\nAudit passed: No missing values found.")


Git add
