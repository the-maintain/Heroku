import streamlit as st
import pickle
import numpy as np
import pandas as pd



st.set_page_config(page_title="Pankreatit'te progresyon tahminleme modeli")
tabs=["Pankreatit Nedir?","Tahminleme Modeli","Tablolar","Hakkında"]
page = st.sidebar.radio("Sekmeler",tabs)

model = pickle.load(open('/home/rahman/PycharmProjects/pythonProject/pankreatit2/model.pk1', 'rb'))

b = pd.DataFrame(columns = ['SEX', 'AGE', 'WBC', 'NEU', 'LYM', 'HGB', 'PLT', 'NEU*PLT',
'SII','GLU', 'UREA', 'CREA', 'AST', 'ALT', 'LDH', 'LIPASE', 'CRP', 'PLR',
 'NLR', 'NEW_AMY_LIP', 'NEW_WBC_EQL', 'NEW_AMY_UREA', 'RADIO_SCORE'],
data = [[1.0,24.0,9.8,7.42,1.31, 12.8, 279.0, 2070.18,1580.0,64.0,25.3, 0.62,
        80.0,282.0, 177.0,264.0,26.23,212.0,5.0,855.0,1.07,0.042809,48.0]])
b.head()
model.predict(b)
if page == "Tahminleme Modeli":
    st.markdown("<h1 style='text-align:center;'>Pankreatit</h1>",unsafe_allow_html=True)
    st.write(""" Acil Serviste Akut Pankreatit Tanısı Alan Hastaların Progresyon  Tahmini""")

    SEX = st.selectbox('PATIENTS SEX',('FEMALE', 'MALE'))
    AGE = st.number_input("AGE")
    WBC = st.number_input("Lökosit Miktarı")
    NEU = st.number_input("Nötrofil Miktarı")
    LYM = st.number_input("Lenfosit Miktarı")
    HGB = st.number_input("HGB Seviyesi")
    PLT = st.number_input("Trombosit Miktarı")
    GLU = st.number_input("Kan Glukoz Düzeyi")
    UREA = st.number_input("Üre Miktarı")
    CREA = st.number_input("Kreatinin Seviyesi")
    AST = st.number_input("AST")
    ALT = st.number_input("ALT")
    LDH = st.number_input("LDH")
    AMYLASE = st.number_input("AMYLASE")
    LIPASE = st.number_input("LIPASE")
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
    st.markdown("<h1 style='text-align:center;'>PANKREAS ENZİMLERİNİN PANKREAS İÇİNDE AKTİVASYONUDUR</h1>",unsafe_allow_html=True)




