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