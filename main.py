import streamlit as st

st.title("Ücretli Vergi Hesaplama (2026)")
gelir=st.number_input("Gelir giriniz", min_value=0)

vergi=0

if gelir <=190_000:
  vergi=gelir*0.15

elif gelir<=400_000:
  vergi=((190_000*0.15)
  +((gelir-190_000)*0.20))

elif gelir<=1_500_000:
  vergi=((190_000*0.15)
  +(210_000*0.20)
  +((gelir-400_000)*0.27))

elif gelir<=5_300_000:
  vergi=((190_000*0.15)
  +(210_000*0.20)
  +(1_100_000*0.27)
  +((gelir-1_500_000)*0.35))

else:
  vergi=((190_000*0.15)
  +(210_000*0.20)
  +(1_100_000*0.27)
  +(3_800_000*0.35)
  +((gelir-5_300_000)*0.40))


st.write("Vergi.",vergi)
