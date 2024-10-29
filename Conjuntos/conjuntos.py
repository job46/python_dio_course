# numeros ={1,2,4,5,6,7}
# numeros =list(numeros)
# print(numeros[2])

conjunto_a={1,4,5}
conjunto_b={3,7,8}
conjunto_a.add(3)
conjunto_uniao =(conjunto_a.union(conjunto_b)).intersection(conjunto_b)
conjunto_intercessao=((conjunto_a.intersection(conjunto_b)).difference(conjunto_a)).union(conjunto_b)
print(conjunto_uniao)
print(conjunto_intercessao)
