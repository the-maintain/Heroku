import pandas as pd
import pickle
import numpy as np

SEX = input()
AGE = float(input())
WBC = float(input())
NEU = float(input())
LYM = float(input())
HGB = float(input())
PLT = float(input())
GLU = float(input())
UREA = float(input())
CREA = float(input())
AST = float(input())
ALT = float(input())
LDH = float(input())
AMYLASE = float(input())
LIPASE = float(input())
CRP = float(input())
RADIO = input()


a = pd.DataFrame(data=[[0 if SEX == "FEMALE" else 1,AGE,WBC,NEU,LYM,HGB,PLT,NEU*PLT,
                            NEU*PLT/LYM,GLU,UREA,CREA,AST,ALT,LDH,LIPASE,CRP,PLT/LYM,
                            NEU/LYM,AMYLASE+LIPASE,WBC-NEU-LYM,UREA/AMYLASE, 1*AGE if RADIO=="Hafif" else (2*AGE if RADIO=="Orta" else AGE*3)]],
                    columns=['SEX', 'AGE', 'WBC', 'NEU', 'LYM', 'HGB', 'PLT', 'NEU*PLT',
     'SII', 'GLU', 'UREA', 'CREA', 'AST', 'ALT', 'LDH', 'LIPASE', 'CRP', 'PLR',
     'NLR', 'NEW_AMY_LIP', 'NEW_WBC_EQL', 'NEW_AMY_UREA', 'RADIO_SCORE'])
print(a)
model = pickle.load(open('/home/rahman/PycharmProjects/pythonProject/pankreatit2/model.pk1', 'rb'))
output = model.predict(a)
print("Patient's progress is getting {}".format("worse" if output==1 else "better"))
