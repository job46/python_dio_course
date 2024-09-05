#Verificação de Idade
#Escreva um programa que peça ao usuário sua idade e verifique se ele tem idade suficiente para dirigir
# (idade mínima de 18 anos). Se sim, exiba "Você pode dirigir". Se não, exiba "Você ainda não pode dirigir".

# idade = int(input("Informe a sua idade: "))
# if idade>=18:
#     print("Você pode dirigir")
# else:
#     print("Voce ainda nao pode dirigir")

#Número Par ou Ímpar
#Solicite ao usuário que insira um número inteiro e verifique se o número é par ou ímpar.
#Exiba "Número par" ou "Número ímpar" conforme o caso.
    
# print("================//================")
# numero = int(input("Informe o numero: "))
# if numero%2==0:
#     print("Número Par.")

# else:
#     print("Número impar")
# print(f"O número informado foi: {numero}")

#Verificação de Notas
#Solicite ao usuário a nota final de um aluno. Se a nota for 7 ou mais, exiba "Aprovado". 
#Se a nota for entre 5 e 7, exiba "Recuperação". Se for menor que 5, exiba "Reprovado".

nota = float(input("Informe a sua a nota final: "))
if nota>=7:
    print("Aprovado")

elif 5<=nota<7:
    print("Recuperação")

if nota<5:
    print("Reprovado")
print(f"A nota informada foi: {nota}")

# Calculadora Simples
# Crie um programa que funcione como uma calculadora simples. Solicite ao usuário dois números e a operação desejada (+, -, *, /). 
# Use condicionais para realizar a operação correspondente e exibir o resultado.

#numero1 = float(input("Informe o primeiro n"))