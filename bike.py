import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Judul aplikasi
st.title("Analisis Pengaruh Cuaca Terhadap Peminjaman Sepeda")

# Membaca dataset dari lokal (ganti dengan path file dataset kamu)
data_day = pd.read_excel('D:\Bangkit Pepin\Dashboard\day.xlsx')  # Pastikan file 'data.csv' ada di folder yang sama atau ganti dengan path absolut

# Menampilkan data
st.write("Data yang dianalisis:")
st.dataframe(data_day.head())

# Menampilkan statistik deskriptif data
st.write("Statistik Deskriptif:")
st.write(data_day.describe())

# Visualisasi korelasi variabel cuaca dan peminjaman
st.write("Korelasi Cuaca dan Peminjaman Sepeda:")
cuaca_data = ['temp', 'hum', 'windspeed', 'cnt']  # Sesuaikan dengan nama kolom dataset
if all(col in data_day.columns for col in cuaca_data):
    fig, ax = plt.subplots()
    sns.heatmap(data_day[cuaca_data].corr(), annot=True, cmap='coolwarm', ax=ax)
    st.pyplot(fig)

# Visualisasi peminjaman sepeda di hari libur vs hari kerja
st.write("Perbandingan Peminjaman Sepeda: Hari Libur vs Hari Kerja")
if 'holiday' in data_day.columns and 'cnt' in data_day.columns:
    holiday_counts = data_day.groupby('holiday')['cnt'].mean().reset_index()
    fig, ax = plt.subplots()
    sns.barplot(x='holiday', y='cnt', data=holiday_counts, ax=ax)
    ax.set_title("Peminjaman Rata-rata di Hari Libur dan Hari Kerja")
    st.pyplot(fig)