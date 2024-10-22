import matplotlib.pyplot as plt
import pandas as pd

# x=[1,2,3,4]
# y=[1,4,9,16]
# plt.boxplot(x,y)
# plt.xlabel("Eje X")
# plt.ylabel("Eje Y")
# plt.title("Grafico Simple")
# plt.show()

df=pd.read_csv("poblacion.csv")
x=df["Date"]
y=df["COL"]
z=df["AFG"]
t=df["ARG"]
plt.stackplot(x,y)
plt.stackplot(x,z)
plt.stackplot(x,t)
plt.xlabel("Fecha")
plt.ylabel("Poblation")
plt.title("Grafico Simple")
plt.show()