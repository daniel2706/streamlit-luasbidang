import streamlit as st
from streamlit_option_menu import option_menu

# navigasi side bar
with st.sidebar :
    selected = option_menu ('Hitung Luas Bangun' , ['Hitung Luas Persegi Panjang','Hitung Luas Segitiga'], default_index=0)

# halaman hitung luas persegi panjang
if (selected == 'Hitung Luas Persegi Panjang') :
    st.title('Hitung Luas Persegi Panjang')

    panjang = st.number_input ("Masukkan Nilai Panjang", 0)
    lebar = st.number_input ("Masukkan Nilai Lebar", 0)
    hitung = st.button ("Hitung Luas")

    if hitung : 
        luas = panjang*lebar
        st.write ("Luas Persegi Panjang adalah = ", luas)
        st.success (f"Luas Persegi Panjang adalah = {luas}")

# halaman hitung luas segitiga
if (selected == 'Hitung Luas Segitiga') :
    st.title('Hitung Luas Segitiga')

    panjang = st.number_input ("Masukkan Nilai Panjang", 0)
    lebar = st.number_input ("Masukkan Nilai Lebar", 0)
    hitung = st.button ("Hitung Luas")

    if hitung : 
        luas = 0.5*(panjang*lebar)
        st.write ("Luas Segitiga adalah = ", luas)
        st.success (f"Luas Segitiga adalah = {luas}")
