import numpy as np

lista1=[1,2,3,4,5,6,7,8,9,10]
lista2=[11,12,13,14,15,16,17,18,19,20]
lista3=[1,3,13,6,7,9,9,10,11,5]
# print(lista1)

arr1=np.array(lista1)
arr2=np.array(lista2)
# print(arr1)

# resultado=np.add(arr1,arr2)
# print(resultado)
# resultado1=np.subtract(arr1,arr2)
# print(resultado1)
# resultado2=np.multiply(arr1,arr2)
# print(resultado2)
# resultado3=np.divide(arr1,arr2)
# print(resultado3)
# resultado4=np.maximum(arr1,arr2)
# print(resultado4)
print("promedio" , np.mean(lista3))
print("mediana" , np.median(lista3))
print("desviasion std" , np.std(lista3))



