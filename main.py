import streamlit as st
import requests

url=f"https://api.coinlore.net/api/tickers/"
data=requests.get(url).json()["data"]

fiyat={coin["symbol"]:float(coin["price_usd"]) for coin in data}
coins=list(fiyat.keys())

col1, col2, col3 = st.columns(3)

with col1:
    gonderilen_coin=st.selectbox("Gönderilen coin",coins)

with col2:
    alinan_coin=st.selectbox("Alınan coin",coins)

with col3:
    miktar=st.number_input("Miktar", value=1.0)

if st.button("Dönüştür"):
    if gonderilen_coin in fiyat and alinan_coin in fiyat:
        results=(fiyat[gonderilen_coin]/fiyat[alinan_coin]*miktar)
        st.success(f"{miktar} {gonderilen_coin} = {results:6f} {alinan_coin}")
    else:
        st.error("Coin Bulunamadı")
