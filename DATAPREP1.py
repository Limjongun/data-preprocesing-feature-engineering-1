import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv("dirty_cafe_sales.csv")

print(df.head())
print(df.tail())
print(df.columns)
print(df.shape)
print(df.info())
print(df.describe())

# cek missing awal
print(df.isnull().sum())
missing_percentage = df.isnull().sum() / len(df) * 100
print(missing_percentage)

# ganti token aneh jadi NaN
missing_token = ['UNKNOWN', 'ERROR', '', 'None', 'nan']
df = df.replace(missing_token, np.nan)

print("\nmissing value setelah replace")
print(df.isna().sum())

# cek duplikasi
print("duplicate:", df.duplicated().sum())
print("\nduplikat di transaksi id:")
print(df['Transaction ID'].duplicated().sum())

# ubah tipe data numerik
num_cols = ['Quantity', 'Price Per Unit', 'Total Spent']
for col in num_cols:
    df[col] = pd.to_numeric(df[col], errors='coerce')

# ubah tanggal
df['Transaction Date'] = pd.to_datetime(df['Transaction Date'], errors='coerce')
print("\nsudah diubah")
print(df.dtypes)

# cek missing lagi
print("\nkolom paling bermasalah")
missing_percentage = df.isnull().sum() / len(df) * 100
print(missing_percentage.sort_values(ascending=False))

# isi missing kategori
cat_col = ['Item', 'Payment Method', 'Location']
for col in cat_col:
    df[col] = df[col].fillna(df[col].mode()[0])

# isi missing numerik berbasis logika bisnis
mask = df['Total Spent'].isna() & df['Quantity'].notna() & df['Price Per Unit'].notna()
df.loc[mask, 'Total Spent'] = df.loc[mask, 'Quantity'] * df.loc[mask, 'Price Per Unit']

mask = df['Quantity'].isna() & df['Total Spent'].notna() & df['Price Per Unit'].notna()
df.loc[mask, 'Quantity'] = df.loc[mask, 'Total Spent'] / df.loc[mask, 'Price Per Unit']

mask = df['Price Per Unit'].isna() & df['Total Spent'].notna() & df['Quantity'].notna()
df.loc[mask, 'Price Per Unit'] = df.loc[mask, 'Total Spent'] / df.loc[mask, 'Quantity']

# isi sisa missing numerik dengan median
for col in num_cols:
    df[col] = df[col].fillna(df[col].median())

# kalau Quantity memang count item, bulatkan
df['Quantity'] = df['Quantity'].round()

# hapus transaksi tanpa tanggal lebih awal
df = df.dropna(subset=['Transaction Date'])

# cek konsistensi
df['Calc Total'] = df['Quantity'] * df['Price Per Unit']
df['Diff'] = df['Total Spent'] - df['Calc Total']
print(df['Diff'].describe())

# outlier detection
print("\noutlier detect: total spent")

Q1 = df['Total Spent'].quantile(0.25)
Q3 = df['Total Spent'].quantile(0.75)
IQR = Q3 - Q1

lower = Q1 - 1.5 * IQR
upper = Q3 + 1.5 * IQR

outlier = df[(df['Total Spent'] < lower) | (df['Total Spent'] > upper)]
print(outlier.shape)

# capping outlier
lower_cap = df['Total Spent'].quantile(0.01)
upper_cap = df['Total Spent'].quantile(0.99)
df['Total Spent'] = df['Total Spent'].clip(lower=lower_cap, upper=upper_cap)

# setelah clip, hitung ulang konsistensi
df['Calc Total'] = df['Quantity'] * df['Price Per Unit']
df['Diff'] = df['Total Spent'] - df['Calc Total']

# filter quantity tidak valid
df = df[df['Quantity'] > 0]
df = df[df['Quantity'] <= 20]

# feature engineering waktu
df['Year'] = df['Transaction Date'].dt.year
df['Month'] = df['Transaction Date'].dt.month
df['Day'] = df['Transaction Date'].dt.day
df['Day_Name'] = df['Transaction Date'].dt.day_name()
df['is_weekend'] = df['Day_Name'].isin(['Saturday', 'Sunday']).astype(int)

# feature engineering transaksi
df['high_value_transaction'] = (df['Total Spent'] >= df['Total Spent'].quantile(0.90)).astype(int)

# avg_item_price sebaiknya hati-hati
df['avg_item_price'] = df['Total Spent'] / df['Quantity']

# visualisasi missing value
plt.figure(figsize=(10, 5))
sns.heatmap(df.isna(), cbar=False, yticklabels=False)
plt.title("Missing Value Heatmap")
plt.show()

# simpan hasil
df.to_csv("cafe_clean2.csv", index=False)