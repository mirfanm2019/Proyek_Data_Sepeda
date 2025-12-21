import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
#judul halaman
st.title("Dashboard Data Sepeda")
st.write("M. Irfan Maulana-Teknik Informatika 2025")
#load data
df= pd.read_csv("day.csv")
df['dteday']=pd.to_datetime(df['dteday'])
#Tabel data
if st.checkbox("Tampilkan Data Mentah"):
    st.write(df)
#Grafik
st.subheader(" Grafik Penyewaan Sepeda (2011-2012)")



fig, ax = plt.subplots(figsize=(16, 8))
ax.plot(df["dteday"], df["cnt"], marker='o', linewidth=2, color="#059A61") 
ax.set_title("Jumlah Penyewaan Sepeda Harian", fontsize=20)
ax.set_xlabel("Tanggal", fontsize=15)
ax.set_ylabel("Jumlah Sewa", fontsize=15)
ax.grid(True)

# 6. Tampilkan Grafik di Website
st.pyplot(fig)