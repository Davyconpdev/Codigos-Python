number = float(input('digite um n�mero: '))

if number > 0:
    print("� Positivo")
elif number < 0:
    print("� Negativo")
else:
    print("Zero")


###-----------------------


number = int(input('digite um n�mero: '))

if number %2 == 0:
    print("� Par")
else:
    print("� �mpar")
    
    
###-----------------------


ano = int(input('Informe seu ano de nascimento: '))

idade = 2024 - ano

if idade >= 16:
    print("Voc� est� apto(a) a votar")
else:
    print("Voc� N�O est� apto(a) a votar")
 
 
###-----------------------


idade = int(input('informe sua idade: '))

if idade <= 12:
  print("Crian�a")
elif idade > 12 and idade < 18:
  print("Adolescente")
elif idade > 17 and idade < 60:
  print("Adulto")
else:
  print("Idoso")
    
    
    
###-----------------------


n1 = int(input('um n�mero: '))
n2 = int(input('outro n�mero: '))

if n1 % n2 == 0:
    print(f"{n1} � divis�vel por {n2}")
else:
    print(f"{n1} N�O � divis�vel por {n2}") 
