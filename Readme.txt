Proyek Analisis Data Penyewaan Sepeda
Deskripsi
Proyek ini melakukan analisis data pada Bike Sharing Dataset untuk mengidentifikasi pola penggunaan sepeda berdasarkan waktu, cuaca, dan kondisi harian. Hasil analisis disajikan dalam bentuk dashboard interaktif.

Struktur Direktori
/dashboard: Berisi file dashboard.py dan dataset yang telah dibersihkan untuk tampilan visual.


/data: Dataset mentah dalam format CSV (harian dan jam).

notebook.ipynb: File dokumentasi proses analisis mulai dari pembersihan data hingga visualisasi.

requirements.txt: Daftar pustaka Python yang dibutuhkan.

Instalasi
Clone repositori ini:

Bash

git clone https://github.com/mirfanm2019/Proyek_Data_Sepeda.git
Instal library yang dibutuhkan:

Bash

pip install -r requirements.txt
Cara Menjalankan Dashboard
Masuk ke direktori dashboard:

Bash

cd dashboard
Jalankan aplikasi Streamlit:

Bash

streamlit run dashboard.py
Fitur Utama
Analisis tren penyewaan sepeda berdasarkan musim.

Perbandingan penggunaan sepeda pada hari kerja dan hari libur.

Visualisasi pengaruh kondisi cuaca terhadap jumlah pengguna.
