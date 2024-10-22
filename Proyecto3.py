import matplotlib.pyplot as plt
import pandas as pd

df=pd.read_csv("1.csv")

#region pacifica
choco = df.loc[(df["DEPARTAMENTO"] == "Chocó") & (df["SEDES_CONECTADAS_A_INTERNET"])]
f= choco[["AÑO","DEPARTAMENTO","SEDES_CONECTADAS_A_INTERNET"]]
anno_choco= f["AÑO"]
sedes_conectadas_internet=f["SEDES_CONECTADAS_A_INTERNET"]

narinno=df.loc[(df["DEPARTAMENTO"] == "Nariño") & (df["SEDES_CONECTADAS_A_INTERNET"])]

sedes_conectadas_internet_narinno=narinno["SEDES_CONECTADAS_A_INTERNET"]


ValledelCauca=df.loc[(df["DEPARTAMENTO"] == "Valle del Cauca") & (df["SEDES_CONECTADAS_A_INTERNET"])]
valle= ValledelCauca[["AÑO","DEPARTAMENTO","SEDES_CONECTADAS_A_INTERNET"]]
sedes_conectadas_internet_ValledelCauca= valle["SEDES_CONECTADAS_A_INTERNET"]





#Cauca

Cauca=df.loc[(df["DEPARTAMENTO"] == "Cauca") & (df["SEDES_CONECTADAS_A_INTERNET"])]
Cauca= Cauca[["AÑO","DEPARTAMENTO","SEDES_CONECTADAS_A_INTERNET"]]
sedes_conectadas_internet_Cauca= Cauca["SEDES_CONECTADAS_A_INTERNET"]






plt.plot(anno_choco,sedes_conectadas_internet)
plt.plot(anno_choco, sedes_conectadas_internet_narinno)
plt.plot(anno_choco, sedes_conectadas_internet_Cauca)
plt.plot(anno_choco,sedes_conectadas_internet_ValledelCauca)
plt.legend(["Chocó","Nariño","Cauca","Valle del Cauca"])
plt.xlabel("Año")
plt.ylabel("Cantidas de sedes conectadas a internet")
plt.title("Conexión a internet en el pacifico")
plt.show()
