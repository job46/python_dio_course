#Exercício 1: Verifique se um número é positivo e se é divisível por 2 e por 3 ao mesmo tempo.
numero=12
resultado = (numero>0 and (numero%2==0) and (numero%3==0))
print(resultado)

#Exercício 2: Verifique se um número não é negativo ou se é maior que 10.

numero = -5
resposta = ((not numero<0) or (numero>10))
print(resposta)

#Exercício 1: Verifique se a soma de dois números é maior que 100.

numero1, numero2 =10, 20

resultado_soma = (numero1+numero2)
print (resultado_soma>10)

#Exercício 1: Comece com um saldo de 500 e, em seguida, adicione 200, subtraia 50 e multiplique por 2. Qual é o saldo final?

saldo = 500
saldo =(saldo+200 -50)*2
print (saldo)

#Exercício 1: Crie duas listas diferentes com o mesmo conteúdo e verifique se elas são o mesmo objeto na memória.
lista1=[1,2,4]
lista2=[1,2,4]

print(lista1 is not lista2)

frase = "Aprendendo Python com exercícios práticos"

print("Python" in frase)
