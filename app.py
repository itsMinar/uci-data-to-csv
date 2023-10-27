# Import necessary libraries
import pandas as pd
from ucimlrepo import fetch_ucirepo

# Fetch a dataset with the ID from the UCI ML Repository, here I used 45(Heart Disease)
raw_data_set = fetch_ucirepo(id=45)

# Create a DataFrame from the original dataset
df = pd.DataFrame(raw_data_set.data.original)

# Find columns that are not of type int or float
non_numeric_columns = [
    col for col in df.columns if not pd.api.types.is_numeric_dtype(df[col])]


# Check for NaN values in each column
nan_columns = df.columns[df.isna().any()].tolist()

# For each column with NaN (missing) values in the DataFrame
for column in nan_columns:
    # Check if the column is not in the list of non-numeric columns
    if column not in non_numeric_columns:
        # Calculate the mean value of the column and make it round figure
        rounded_mean_value = round(df[column].mean())

        # Fill the NaN values in the column with the rounded mean value
        df[column].fillna(rounded_mean_value, inplace=True)

        # Print a message indicating that NaN values in the column have been filled with the rounded mean value
        print(column, "=> column's NaN value is filled with rounded mean value")


# Save the DataFrame to a CSV file named 'data.csv'
df.to_csv('data.csv', index=False)

# Print a success message
print('\nSuccessfully created the CSV file. Thanks!')
