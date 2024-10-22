import pandas as pd

df=pd.read_csv("poblacion.csv")
# print(df.head()) 
# print(df.describe())
# print(df.tail())
# print(df.sample())
# print(df[["Date","COL","ARG"]])

# filtro=df[df['COL']>30000000]#agregar filtro
# print(filtro["COL"])

df['Ciudad']=df['COL'] # Aniadir columna
# df=df.drop(columns=["Edad"]) #Elimina Columna
print(df)
