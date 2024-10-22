import pandas as pd
# #crea DataFrame
# data={"Nombre":['Ana','Luis','Carlos'],"Edad":['32','21','45'],"Telefono":['354543','767645','54542354']}
# df=pd.DataFrame(data)
# print(df["Nombre"])
# print(df)
# df.to_csv("salida.cvs",index=False)

df=pd.read_csv("poblacion.csv")
print(df.head())
print(df.describe())
print(df.tail())
print(df.sample())