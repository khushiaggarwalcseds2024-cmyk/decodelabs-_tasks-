
# Data Cleaning Project using Python

## Project Overview

This project performs basic data cleaning on an Excel dataset using Python and Pandas. The script loads the dataset, checks for missing values, fills missing coupon codes, removes duplicate records, checks for duplicate Order IDs, and saves the cleaned dataset into a new Excel file.

---

## Features

* Load Excel dataset using Pandas
* Check missing values in all columns
* Replace blank CouponCode values with "No Coupon"
* Remove duplicate rows
* Identify duplicate Order IDs
* Save cleaned data to a new Excel file

---

## Requirements

Install the required libraries:

```bash
pip install pandas openpyxl
```

---

## Files

* `Dataset for Data Analytics.xlsx` → Original dataset
* `clean_data.py` → Python script for data cleaning
* `Project1_Cleaned_Dataset.xlsx` → Cleaned output dataset

---

## Python Code

```python
import pandas as pd

# Dataset load karo
df = pd.read_excel("Dataset for Data Analytics.xlsx")

# Missing values check karo
print("Missing Values:")
print(df.isnull().sum())

# CouponCode blanks fill karo
if 'CouponCode' in df.columns:
    df['CouponCode'] = df['CouponCode'].fillna("No Coupon")

# Duplicate rows remove karo
df = df.drop_duplicates()

# Duplicate OrderID check karo
if 'OrderID' in df.columns:
    print("Duplicate OrderID:", df['OrderID'].duplicated().sum())

# Cleaned file save karo
df.to_excel("Project1_Cleaned_Dataset.xlsx", index=False)

print("Project Completed Successfully!")
```

---

## How to Run

1. Place the dataset file in the project folder.
2. Open the folder in VS Code.
3. Open Terminal.
4. Install dependencies:

```bash
pip install pandas openpyxl
```

5. Run the script:

```bash
python clean_data.py
```

---

## Output

After successful execution:

* Missing values report will be displayed in the terminal.
* Duplicate rows will be removed.
* Missing CouponCode values will be replaced with "No Coupon".
* Cleaned dataset will be saved as:

```text
Project1_Cleaned_Dataset.xlsx
```

---

## Author

Khushi Aggarwal

## Tools Used

* Python
* Pandas
* OpenPyXL
* Visual Studio Code

