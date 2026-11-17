import pandas as pd
import streamlit as st
import plotly.express as px
import yfinance as yf
from datetime import date

st.title("Pertemuan 10: Interaksi Streamlit dan Yohoo Finance")

kamus_ticker = {
    "GOOGL":'Google',
    "AAPL":'Apple Inc',
    "SBUX":'Starbucks',
    "MCD": 'McDonald',
    "META":'Meta Platform Inc',
    "TLKM.JK":'Telkom Indonesia (Persero) Tbk',
    "BBNI.JK":'Bank Negara Indonesia (persero) Tbk',
    "BMRI.JK":'Bank Mandiri (persero) Tbk',
    "BBRI.JK":'Bank Rakyat Indonesia (persero) Tbk',
    "NESN":'Nesle SA'
}

ticker_symbol = st.selectbox(
    'Silahkan pilih kode perusahaan:',
    sorted (kamus_ticker.keys())
)

st.write(kamus_ticker[ticker_symbol])

ticker_data= yf.Ticker(ticker_symbol)

pilihan_periode = st.selectbox(
    'pilih periode:',
  ['1d', '5d', '2mo', '5mo', '1y', '5y']
)
tgl_mulai = st.date_input(
    'mulai tanggal',
    value=date.today()
)
tgl_akhir = st.date_input(
    'sampel tanggal',
    value=date.today()
)
st.write(f'Tanggal mulai:{Tgl_mulai}')
st.write(f'Tanggal akhir: {Tgl_akhir}')
df_ticker = ticker_data.history(
    start=str(Tgl_mulai),
    end=str(tgl_akhir)
)

pilihan_tampil_tabel = st.checkbox('Tampilan tabel')

if pilihan_tampilan_tabel == True:
    st.write("## Lima Data Awal")
    st.write(df_ticker.head() )

st.write(f"## Visualisasi pergerakan saham {kamus_ticker[ticker_symbol]}")

pilihan_atribut=st.multiselect(
         'silahkan pilih atribut yang akan ditampilkan:',
         ['Low', 'High', 'Open', 'close', 'volume']
)

grafik=px.line(
    df_ticker,
    y=pilihan_atribut,
    title=f"harga saham{kamus_ticker[ticker_symbol]}"
)
st.plotly_chart(grafik)

st.write()

#https://share.streamlit.io/
#https://github.com/
#https://share.streamlit.io/user/arwajunjun-ai




    




