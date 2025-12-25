#  Analisis Data Sepeda
M. Irfan Maulana-Teknik Informatika 2025


1. Struktur File
* dashboard.py: File utama aplikasi Streamlit (kodingan).
* day.csv: Dataset penyewaan sepeda yang digunakan.
* requirements.txt: Daftar library (Pandas, Matplotlib, Seaborn, Streamlit).
* README.md: Dokumen penjelasan proyek ini.

2. Insight dari Data
Berdasarkan visualisasi yang ada di dashboard:
1. Tren Harian: Terjadi kenaikan jumlah penyewa yang signifikan dari tahun 2011 ke 2012, terutama di pertengahan tahun.
2. Kondisi Hari: Rata-rata penyewaan sepeda lebih tinggi pada **Hari Kerja** dibandingkan Hari Libur. Ini menunjukkan bahwa sepeda digunakan sebagai alat transportasi rutin oleh pengguna.

3.  Cara Menjalankan di Lokal
1. Pastikan kamu sudah punya Python di laptop.
2. Install semua library yang diperlukan, jalankan di terminal:
   pip install -r requirements.txt

4. Cara deploy
streamlit run dashboard.py
