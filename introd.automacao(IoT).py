num1 = 5
num2 = 7
conta = num1 + num2 
print ("Resultado:",conta)

###---------------------------------------------------------------------

num1 = 10
num2 = 20
conta = num1 - num2 
print ("Resultado:",conta)

###---------------------------------------------------------------------

num1 = 3
num2 = 4
conta = num1 * num2 
print ("Resultado:",conta)

###---------------------------------------------------------------------

dividendo = 100
divisor = 5
divisao = dividendo/divisor
print ("Resultado: {:.2f}".format(divisao))

###---------------------------------------------------------------------

largura = float(input("Largura: "))
altura = float(input("Altura: "))
calculo = largura * altura
print ("\nÁrea do triângulo: {:.2f} Unidade(s) Medida".format(calculo))

###---------------------------------------------------------------------

raio = float(input("Raio: ")) 
calculo = (2 * 3.14) * raio
print("\nCircunferência do circulo: {:.2f} Unidade(s) Medida".format(calculo))

###---------------------------------------------------------------------

raio = float(input("Raio: ")) 
calculo = (4/3 * 3.14) * (raio**3)
print("\nVolume da Esfera: {:.2f} Unidade(s) Medida".format(calculo))

###---------------------------------------------------------------------

celsius = float(input("Temperatura(C°): ")) 
fahrenheit = (celsius * 9/5) + 32
print("\nCelsius: {:.1f}°\nFahrenheit: {:.1f}°".format(celsius,fahrenheit))

###---------------------------------------------------------------------

total = int(input("Um número: ")) 
percentual = int(input("Valor Percentual: ")) 
calculo = total * (percentual/100)
print("\nPercentual: {:.2f}".format(calculo))

###---------------------------------------------------------------------

lado = float(input("Lado do Quadrado: "))
calculo = 4 * lado
print("\nPerímetro do quadrado: {:.1f}".format(calculo))



fahrenheit = float(input("Temperatura(F°): ")) 
celsius = (fahrenheit - 32) / 9 * 5
print("\nFahrenheit: {:.1f}°\nCelsius: {:.1f}°".format(fahrenheit,celsius))

###---------------------------------------------------------------------

altura = float(input("Altura: "))
calculo = 72.7 * altura - 58
print("Peso Ideal para Homens: {:.1f} Kg".format(calculo))
calculo = 62.1 * altura - 44.7
print("Peso Ideal para Mulheres: {:.1f} Kg".format(calculo))

###---------------------------------------------------------------------

peso = float(input("Peso do peixe: "))
excesso = peso - 50.0 
multa = excesso * 4.0
if(peso > 50.0):
    print("\nPeso: %.2f"%(peso))
    print("Peso Excedente: {:.2f}".format(excesso))
    print("Multa - Valor a Pagar: R${:.2f}".format(multa))
else:
    excesso = 0.0
    multa = 0.0
    print("\nPeso: %.2f"%(peso)) 
    print("Peso Excedente: {:.2f}".format(excesso))
    print("Multa - Valor a Pagar: R${:.2f}".format(multa))

###---------------------------------------------------------------------

valor = float(input("Remuneração por Hora: "))
hora = float(input("Horas trabalhadas: "))
salarioB = valor * hora
ir = salarioB * 0.11
inss = salarioB * 0.08
sindc = salarioB * 0.05
salarioL = salarioB - (ir + inss + sindc) 
print("\nSalário Bruto: R${:.2f}".format(salarioB))
print("Imposto de Renda: R${:.2f}".format(ir))
print("INSS: R${:.2f}".format(inss))
print("Sindicato: R${:.2f}".format(sindc))
print("Salário Líquido: R${:.2f}".format(salarioL))
###---------------------------------------------------------------------

number = int(input('digite um número: '))  
if number %2 == 0:     
print("É Par") 
else:     
print("É Ímpar")     
###---------------------------------------------------------------------

num1 = float(input('digite um número: '))
num2 = float(input('digite outro número: '))
if num1 > num2:
    print("\n%f é maior"%(num1))
elif num1 == num2:
    print("\nSão iguais") 
else:
    print("\n%f é maior"%(num2))
###---------------------------------------------------------------------  

nota1 = float(input('Sua 1ª nota: '))
nota2 = float(input('Sua 2ª nota: '))   
media = (nota1 + nota2) / 2
if media >= 7:
    print("\nAprovado!")
elif media >= 5 and media < 7:
    print("\nRecuperação.")
else: 
    print("\nReprovado.")
###---------------------------------------------------------------------
   
idade = int(input('Informe sua idade: '))
if idade < 18:
    print("\nMenor de idade.")
elif idade >= 18 and idade <= 60:
    print("\nAdulto.")
else:
    print("\nIdoso.")
###---------------------------------------------------------------------

nota = float(input('Sua nota: '))
if nota >= 7:
    print("\nAprovado!")
elif nota >= 5 and nota < 7:
    print("\nRecuperação.")
else: 
    print("\nReprovado.")
###---------------------------------------------------------------------

dia = int(input("Um número (1-7): "))
if dia == 1: 
    print("Domingo.")
elif dia == 2: 
    print("Segunda-feira.")
elif dia == 3: 
    print("Terça-feira.")
elif dia == 4: 
    print("Quarta-feira.")
elif dia == 5: 
    print("Quinta-feira.")
elif dia == 6: 
    print("Sexta-feira.")
elif dia == 7: 
    print("Sábado.")
else:
    print("Opção Inválida.")
    
###---------------------------------------------------------------------

l1 = float(input('Medida Lado 1: ')) 
l2 = float(input('Medida Lado 2: '))
l3 = float(input('Medida Lado 3: '))

a = l2 - l3
b = l2 + l3

c = l1 - l3
d = l1 + l3

e = l2 - l1
f = l2 + l1

if l1 > a and l1 < b and l1 > 0 and l2 > c and l2 < d and l2 > 0 and l3 > e and l3 < f and l3 > 0:
    print("\nForma um triângulo:")
    if l1 == l2 and l1 == l3 and l2 == l3:
        print("Triângulo Equilátero.")
    elif l1 == l2 or l1 == l3 or l2 == l3: 
       print("Triângulo Isósceles.")
    else: 
       print("Triângulo Escaleno.")
else:
    print("\nNão forma um triângulo.") 

###---------------------------------------------------------------------

idade = int(input('Informe sua idade: '))
if idade >= 16:
    print("\nJá vota.")
else: 
    print("\nNão vota.")
###---------------------------------------------------------------------    

salario = float(input('Informe seu salário: '))
if salario < 1000:
    aumento = salario * 0.10
else:
    aumento = salario * 0.05
print("Aumeto: R$%.2f"%(aumento))
###---------------------------------------------------------------------

preco = float(input('Informe o preço do produto: '))
if preco > 100:
   desconto = preco * 0.10
   preco -= desconto
   print("\nDesconto: R$%.2f"%(desconto))
   print("Preço descontado: R$%.2f"%(preco))
else:
   print("\nSem Desconto.")
###---------------------------------------------------------------------

quant = int(input('Quantidade (Litros): '))
tipo = input('Abasteceu com: ')
if tipo == "gasolina":
    preco = 6.5 * quant
    print("Preço: R$%.2f"%(preco))
else:
    preco = 5.0 * quant
    desconto = preco * 0.05
    preco -= desconto
    print("Preço: R$%.2f"%(preco))

###---------------------------------------------------------------------

num1 = float(input('Um número: ')) 
operacao = input('Uma Operação: ') 
num2 = float(input('Outro número: '))
    
def multiplica():
   return num1*num2
    
def divide():
    if num2 == 0:
        print("\nERRO.\nNão é possivel dividir por 0.")
    else:
      return num1/num2

def soma():
    return num1+num2

def subtrai():
    return num1*num2
    
if operacao == '*':
    print("\n%.2f x %.2f = %.2f"%(num1,num2,multiplica()))
elif operacao == '/': 
    print("\n%.2f / %.2f = %.2f"%(num1,num2,divide()))
elif operacao == '+': 
    print("\n%.2f + %.2f = %.2f"%(num1,num2,soma()))
elif operacao == '-': 
    print("\n%.2f - %.2f = %.2f"%(num1,num2,subtrai()))
else:
    print("\nOperações permitidas(* / + -)")

###---------------------------------------------------------------------   

peso = float(input("Seu peso: "))
altura = float(input("Sua altura: "))
imc = peso / altura**2
if imc < 18.5:
    print("\nAbaixo do peso.")
elif imc >= 18.5 and imc <= 24.9:
    print("\nPeso normal.")
elif imc >= 25 and imc <= 29.9:
    print("\nSobrepeso.")
else:
    print("\nObesidade.")
