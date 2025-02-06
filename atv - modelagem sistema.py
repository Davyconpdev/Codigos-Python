number = float(input('digite um número: '))

if number > 0:
    print("É Positivo")
elif number < 0:
    print("É Negativo")
else:
    print("Zero")


###-----------------------


number = int(input('digite um número: '))

if number %2 == 0:
    print("É Par")
else:
    print("É Ímpar")
    
    
###-----------------------


ano = int(input('Informe seu ano de nascimento: '))

idade = 2024 - ano

if idade >= 16:
    print("Você está apto(a) a votar")
else:
    print("Você NÃO está apto(a) a votar")
 
 
###-----------------------


idade = int(input('informe sua idade: '))

if idade <= 12:
  print("Criança")
elif idade > 12 and idade < 18:
  print("Adolescente")
elif idade > 17 and idade < 60:
  print("Adulto")
else:
  print("Idoso")
    
    
    
###-----------------------


n1 = int(input('um número: '))
n2 = int(input('outro número: '))

if n1 % n2 == 0:
    print(f"{n1} é divisível por {n2}")
else:
    print(f"{n1} NÃO é divisível por {n2}") 
