import streamlit as st
import string
import random

name=st.text_input("Bir isim giriniz",value="Ahmet")
surname=st.text_input("Soyisim giriniz",value="Öztürk")
domain="arıbilgi.com"

basharf=name[0]

email=basharf+"."+surname+"@"+domain

email=email.lower()
email=email.replace("ç","c")
email=email.replace("ü","u")
email=email.replace("ğ","g")
email=email.replace("ş","s")
email=email.replace("ı","i")
email=email.replace("ö","o")

st.write(email)


Uzunluk=8

Karakterler=(string.ascii_lowercase+
string.ascii_uppercase+
string.digits+
string.punctuation)

Password="" .join(random.choices(Karakterler,k=Uzunluk))

st.text_input("Password", value=Password)
