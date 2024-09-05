# def mensagem_teste():
#    print(f"Hello World!")

# def soma_numeros(numero1, numero2):
#    print(numero1+numero2)

# mensagem_teste()
# soma_numeros(10,20)

# exercicios para praticar funcoes 
# Criação de Função Simples:

# Escreva uma função chamada cumprimentar() que exiba a mensagem "Olá, seja bem-vindo!".
# Escreva uma segunda função chamada cumprimentar_usuario(nome) que receba o nome de uma 
# pessoa como argumento e exiba a mensagem "Olá, [nome]!".

import math


def cumprimentar():
    print("Olá, seja bem-vindo! ")

def cumprimentar_usuario(nome="Joaquim"):
    print(f"Na boa {nome}, Seja benvindo!")

cumprimentar()
cumprimentar_usuario()

# 2. Calculando o Fatorial:

# Escreva uma função chamada fatorial(n) que retorne o fatorial de um número n (ex.: fatorial de 5 é 54321 = 120).

def factorial(n):
   print(f"O fatorial de {n} é {math.factorial(n)}")

factorial(10)

# Verificação de Número Primo:

# Crie uma função chamada eh_primo(n) que retorne True se o número for primo e False caso contrário.

def e_primo(numero):
    if ((numero%2!=0)  and (numero!=1)):
        print(f"{numero} é primo")

    elif(numero==2):
         print(f"{numero} é primo")

    else:
        print(f"{numero} não é primo")
        

e_primo(145)