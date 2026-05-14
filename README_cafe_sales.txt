Café Sales Data Cleaning & Feature Engineering

Project ini berisi proses data cleaning, handling missing value, outlier detection, dan feature engineering menggunakan Python pada dataset transaksi café.

Dataset yang digunakan:
- dirty_cafe_sales.csv

Tujuan project:
- membersihkan data transaksi yang kotor
- memperbaiki missing value
- menangani outlier
- membuat fitur baru untuk analisis bisnis
- menyiapkan dataset untuk visualisasi atau machine learning

Project Workflow

1. Import Library

Library yang digunakan:
- pandas
- numpy
- matplotlib
- seaborn

Digunakan untuk:
- manipulasi data
- visualisasi
- preprocessing dataset

2. Data Understanding

Melakukan eksplorasi awal dataset dengan:
- df.head()
- df.tail()
- df.info()
- df.describe()

Tujuan:
- memahami struktur data
- mengecek tipe data
- melihat statistik awal dataset

3. Handling Missing Value

Dataset memiliki nilai seperti:
- UNKNOWN
- ERROR
- None

Nilai tersebut diubah menjadi NaN.

Strategi Missing Value:

Kategori
Kolom:
- Item
- Payment Method
- Location

diisi menggunakan modus (mode()).

Numerik
Kolom:
- Quantity
- Price Per Unit
- Total Spent

diisi menggunakan logika bisnis:

Total Spent = Quantity x Price Per Unit

Jika masih ada missing value:
- diisi menggunakan median

4. Duplicate Checking

Melakukan pengecekan:
- duplicate row
- duplicate Transaction ID

Hasil:
- tidak ditemukan duplicate data

5. Data Type Conversion

Konversi tipe data menggunakan:
- pd.to_numeric()
- pd.to_datetime()

Tujuan:
- memastikan kolom numerik bisa dihitung
- memastikan tanggal bisa digunakan untuk feature engineering

6. Outlier Detection

Outlier dideteksi menggunakan metode IQR (Interquartile Range).

Rumus:
IQR = Q3 - Q1

Batas outlier:
Lower = Q1 - 1.5(IQR)
Upper = Q3 + 1.5(IQR)

7. Outlier Handling

Outlier pada Total Spent ditangani menggunakan clip().

Metode ini disebut:
- capping
- winsorizing

Tujuan:
- menjaga distribusi data tetap stabil
- tanpa menghapus terlalu banyak transaksi

8. Feature Engineering

Feature baru yang dibuat:

- Year: tahun transaksi
- Month: bulan transaksi
- Day: hari transaksi
- Day_Name: nama hari
- is_weekend: weekend / weekday
- high_value_transaction: transaksi bernilai tinggi
- avg_item_price: rata-rata harga item

9. Visualization

Visualisasi yang dibuat:
- missing value heatmap
- boxplot outlier
- distribusi transaksi
- analisis dasar penjualan

Library:
- matplotlib
- seaborn

Business Insights

Beberapa insight yang bisa diperoleh:
- metode pembayaran paling populer
- pola transaksi weekend vs weekday
- distribusi transaksi bernilai tinggi
- analisis spending customer
- deteksi data transaksi tidak valid

Tech Stack

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn

Output

Dataset hasil cleaning:
- cafe_clean2.csv

Dataset ini sudah:
- bebas missing value utama
- lebih stabil terhadap outlier
- siap digunakan untuk dashboard, visualisasi, machine learning, atau business analytics

How to Run

Install dependency:
pip install pandas numpy matplotlib seaborn

Run script:
python main.py

Future Improvements

Beberapa improvement yang bisa dilakukan:
- dashboard interaktif menggunakan Power BI atau Tableau
- machine learning prediction
- customer segmentation
- time series forecasting
- anomaly detection

Author

Created for learning:
- Data Cleaning
- Data Preprocessing
- Feature Engineering
- Exploratory Data Analysis (EDA)
