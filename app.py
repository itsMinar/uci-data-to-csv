# Import necessary libraries
from ucimlrepo import fetch_ucirepo
import pandas as pd

# Fetch a dataset with the ID from the UCI ML Repository, here I used 45(Heart Disease)
raw_data_set = fetch_ucirepo(id=45)

# Create a DataFrame from the original dataset
df = pd.DataFrame(raw_data_set.data.original)

# Check for NaN values in each column
nan_columns = df.columns[df.isna().any()].tolist()

# Calculate the mean value and round them to the nearest integer then Replace NaN values with the calculated the mean value of each column
for column in nan_columns:
    mean_value = df[column].mean()
    df[column].fillna(round(mean_value), inplace=True)


# Save the DataFrame to a CSV file named 'data.csv'
df.to_csv('data.csv', index=False)

# Print a success message
print('Successfully created the CSV file. Thanks!')
