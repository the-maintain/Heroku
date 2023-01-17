import streamlit as st
import pickle
import numpy as np
import pandas as pd
import requests
from PIL import Image

def add_logo(logo_path, width, height):
    """Read and return a resized logo"""
    logo = Image.open(logo_path)
    return logo



st.set_page_config(page_title="Pankreatit'te progresyon tahminleme modeli")
tabs=["Pankreatit Nedir?","Tahminleme Modeli","Hakkında"]
page = st.sidebar.radio("Sekmeler",tabs)

# Get the file
r = requests.get('https://github.com/the-maintain/Heroku/raw/main/pankreatit2/model.pk1')

# Save the file
with open('model.pk1', 'wb') as f:
    f.write(r.content)

model = pickle.load(open('model.pk1', 'rb'))

b = pd.DataFrame(columns = ['SEX', 'AGE', 'WBC', 'NEU', 'LYM', 'HGB', 'PLT', 'NEU*PLT',
'SII','GLU', 'UREA', 'CREA', 'AST', 'ALT', 'LDH', 'LIPASE', 'CRP', 'PLR',
 'NLR', 'NEW_AMY_LIP', 'NEW_WBC_EQL', 'NEW_AMY_UREA', 'RADIO_SCORE'],
data = [[1.0,24.0,9.8,7.42,1.31, 12.8, 279.0, 2070.18,1580.0,64.0,25.3, 0.62,
        80.0,282.0, 177.0,264.0,26.23,212.0,5.0,855.0,1.07,0.042809,48.0]])
b.head()
model.predict(b)
if page == "Tahminleme Modeli":
    my_logo = add_logo(logo_path="pankreatit2/Miuul.jpeg", width=30, height=40)
    st.image(my_logo)
    st.markdown("<h1 style='text-align:center;'>Pankreatit</h1>",unsafe_allow_html=True)
    st.write(""" Acil Serviste Akut Pankreatit Tanısı Alan Hastaların Progresyon  Tahmini""")

    SEX = st.selectbox('PATIENTS SEX',('FEMALE', 'MALE'))
    AGE = st.number_input("AGE",min_value=1)
    WBC = st.number_input("Lökosit Miktarıx1000",min_value=1.,max_value=100.)
    NEU = st.number_input("Nötrofil Miktarıx1000",min_value=1.,max_value=100.)
    LYM = st.number_input("Lenfosit Miktarıx1000",min_value=1.,max_value=100.)
    HGB = st.number_input("HGB Seviyesi",min_value=1.,max_value=25.)
    PLT = st.number_input("Trombosit MiktarıX1000",min_value=10.,max_value=800.)
    GLU = st.number_input("Kan Glukoz Düzeyi",min_value=40,max_value=800)
    UREA = st.number_input("Üre Miktarı",min_value=2,max_value=100)
    CREA = st.number_input("Kreatinin Seviyesi",min_value=0.1,max_value=20.)
    AST = st.number_input("AST",min_value=1,max_value=None)
    ALT = st.number_input("ALT",min_value=1,max_value=None)
    LDH = st.number_input("LDH")
    AMYLASE = st.number_input("AMYLASE",min_value=1,max_value=10000)
    LIPASE = st.number_input("LIPASE",min_value=1,max_value=10000)
    CRP = st.number_input("CRP")
    RADIO = st.selectbox(
        'Radyolojik görüntülenmesine göre pankreas görünümü',
        ('Hafif', 'Orta', 'Ağır'))


    a = pd.DataFrame(data=[[0 if SEX == "FEMALE" else 1,AGE,WBC,NEU,LYM,HGB,PLT,NEU*PLT,
                            NEU*PLT/LYM,GLU,UREA,CREA,AST,ALT,LDH,LIPASE,CRP,PLT/LYM,
                            NEU/LYM,AMYLASE+LIPASE,WBC-NEU-LYM,UREA/AMYLASE, 1*AGE if RADIO=="Hafif" else (2*AGE if RADIO=="Orta" else AGE*3)]],
                    columns=['SEX', 'AGE', 'WBC', 'NEU', 'LYM', 'HGB', 'PLT', 'NEU*PLT',
     'SII', 'GLU', 'UREA', 'CREA', 'AST', 'ALT', 'LDH', 'LIPASE', 'CRP', 'PLR',
     'NLR', 'NEW_AMY_LIP', 'NEW_WBC_EQL', 'NEW_AMY_UREA', 'RADIO_SCORE'])

    button=st.button("Tahmin Et")
    if button==True:
        with st.spinner("Tahmin yapılıyor,Lütfen Bekleyiniz..."):
            output = model.predict(a)
            st.write(output)
            st.write("Patient's progress is getting {}".format("worse" if output==1 else "better"))




if page == "Pankreatit Nedir?":
    my_logo = add_logo(logo_path="pankreatit2/Miuul.jpeg", width=30, height=40)
    st.image(my_logo)
    st.markdown("<h1 style='text-align:center;'>PANKREAS ENZİMLERİNİN PANKREAS İÇİNDE AKTİVASYONUDUR</h1>",unsafe_allow_html=True)



if page == "Hakkında":
    st.markdown("""      2022 yılından itibaren faaliyet göstermeye başlıyan MiuulHEALTH  değişen teknolojik şartlar altında 
insan sağlığını daha değerli kılma misyonunu kendine yol bilmiştir. Günümüz teknolojilerini yakından
 takip ederek, sektöründeki lider sağlık kuruluşlarına  danışmanlık, tasarım, yazılım ve dijital 
pazarlama hizmetleri sunmaktadır. Amacımız Makine öğrenmesi ve Derin  öğrenmesi algoritmaları 
araclılığı ile insan sağlığında öncü haber alma vizyonumuzu güçlendirmek, gündelik hayatımızın 
kaçınılmazı olan sağlık sorunlarına durum hayati tehlikeye varmadan müdahale etmektir.""")


 

