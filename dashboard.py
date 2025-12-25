import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

#judul halaman
st.title("Dashboard Data Sepeda-Tugas Machine Learning GDG")
st.sidebar.write("M. Irfan Maulana-Teknik Informatika 2025")

#load data
df= pd.read_csv("day.csv")
df['dteday']=pd.to_datetime(df['dteday'])

#Tabel data
if st.checkbox("Tampilkan Data Mentah"):
    st.write(df)

#Grafik 1 Tren Harian
st.subheader(" Tren Penyewaan Sepeda (2011-2012)")
fig1, ax1=plt.subplots(figsize=(16,8))
#Gambar garis
ax1.plot(df["dteday"], df["cnt"], color="#0F4A91")
#Memberi label
ax1.set_xlabel("Tanggal")
ax1.set_ylabel("Jumlah Sewa")
st.pyplot(fig1)
st.write("**Insight:** Terjadi peningkatan signifikan di tahun 2012 dibandingkan 2011, dengan puncak di pertengahan tahun.")

#Grafik 2
st.subheader(" Rata-rata penyewaan pada hari kerja dan libur")
avg_sewa=df.groupby('workingday')['cnt'].mean()
fig2,ax2=plt.subplots(figsize=(10,6))
avg_sewa.plot(kind='bar', color=["#CB4F33", "#079621"], ax=ax2)

ax2.set_xticklabels(['Hari Libur', 'Hari Kerja'], rotation=0)
ax2.set_ylabel("Rata-rata penyewa")

st.pyplot(fig2)
st.write("**Insight:** Rata-rata penyewaan lebih tinggi pada hari kerja, menunjukkan penggunaan utama untuk transportasi rutin.")

