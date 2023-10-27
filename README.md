# UCI Dataset Processing

## Overview

This documentation outlines a Python script designed to process a dataset obtained from the UCI Machine Learning Repository. The script performs data retrieval, data cleaning, and CSV file export. The code primarily focuses on handling missing values and ensuring the dataset is in a structured format for further analysis.

## Purpose

The primary objective of this script is to automate the process of fetching a dataset from the UCI repository, checking for missing values, calculating mean values, and replacing missing data. The cleaned dataset is then saved as a CSV file, which can be used for machine learning, data analysis, or other data-related tasks.

## Workflow

The script follows a structured workflow:

### 1. Libraries Import

The code begins by importing the required libraries, including `ucimlrepo` for dataset retrieval and `pandas` for data manipulation.

### 2. Dataset Retrieval

The script retrieves a dataset from the UCI Machine Learning Repository using a specified ID (in this case, ID 45, which corresponds to the "Heart Disease" dataset).

### 3. Data Processing

The retrieved dataset is converted into a Pandas DataFrame, making it suitable for further analysis.

### 4. Missing Value Handling

The script identifies columns with missing values (NaN) by checking for NaN values in each column. For each column with missing values, the script calculates the mean value and replaces the NaN values with the rounded mean value, effectively filling in the missing data.

### 5. CSV File Export

The cleaned DataFrame is saved as a CSV file named 'data.csv'. The index is excluded from the saved file to maintain data integrity.

### 6. Success Message

Upon successful execution of the script, a success message is displayed, confirming the creation of the CSV file.

## Usage

This script can be utilized for processing UCI datasets, especially when dealing with missing values and the need for a clean and structured dataset. Users can customize the code by specifying the dataset's unique ID and by modifying the column names used for mean calculation and missing value handling.

## Conclusion

The UCI Dataset Processing script offers a convenient and automated solution for preparing clean datasets for machine learning and data analysis. By automating data cleaning tasks, users can streamline their workflow when working with UCI datasets from the repository.
