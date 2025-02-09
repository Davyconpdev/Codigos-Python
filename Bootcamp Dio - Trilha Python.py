#1�  Desafio: A Aventura do Explorador
# Entrada de dados
quantidade_passos = int(input()) 
#verificando e  repetindo(la�o)
if(quantidade_passos>0):
         print('Explorador: 1 passo')
    for n in range(2,quantidade_passos +1):
         print('Explorador:',n,'passos'.format(n))
    elif(quantidade_passos==0):
         print("Nenhum passo dado na floresta.")


#2� Lista de itens do personagem do jogo
#Solicitando e cadastrando os itens informados pelo usu�rio
i1 = input()
i2 = input()
i3 = input()
# Lista para armazenar os itens
itens = [i1 ,i2 ,i3]
# Exibindo a lista de itens
print("Lista de itens:")
for item in itens:
    print(f"- {item}")


#3� Armazenamento de dados � vida
#Solicitando os valores 
capacidade_atual, aumento_percentual = map(int, input().split())
resultado = int(capacidade_atual * aumento_percentual / 100 + capacidade_atual)
   print(resultado)


#4� O grande dep�sito-solucionando problemas banc�rios
valor = float(input())
#verificando o valor (R$) informado
if valor > 0:
   print('Deposito realizado com sucesso!')
   print('Saldo atual: R$ %.2f'%valor)
elif valor < 0:
    print('Valor invalido! Digite um valor maior que zero.')
else:
    print('Encerrando o programa...')

  
#5� Estrtura de dados: organizando os seus ativos
#lista 
ativos = []
#Entrada da quantidade de ativos
quantidadeAtivos = int(input())

#Entrada dos c�digos dos ativos
for i in range(quantidadeAtivos):
    codigoAtivo = input()
    ativos.append(codigoAtivo)
# Ordenar os ativos em ordem alfab�tica.
    ativos = sorted(ativos)
#Imprimir a lista de ativos ordenada, conforme a tabela de exemplos.
print(ativos[0])
print(ativos[-2])
print(ativos[-1])


#6�  Validando a For�a de Senhas no IAM.
def verificar_forca_senha(senha):
  comprimento_minimo = 8
  tem_letra_maiuscula = False
  tem_letra_minuscula = False
  tem_numero = False
  tem_caractere_especial = False
# Verificando o comprimento da senha
  if len(senha) < comprimento_minimo:
    return f"Sua senha e muito curta. Recomenda-se no minimo {comprimento_minimo} caracteres."
#  Verifique se a senha cont�m letras mai�sculas e min�sculas
  mai�sculas = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','X','Y','Z']
 for l in mai�sculas:
    if l in senha:
      tem_letra_maiuscula = True
    elif l.lower() in senha:
      tem_letra_minuscula = True
  # Verificando se a senha cont�m sequ�ncias comuns
  sequencias_comuns = ["123456", "abcdef"]
  for sequencia in sequencias_comuns:
    if sequencia in senha:
      return "Sua senha contem uma sequencia comum. Tente uma senha mais complexa."
 # Verificando se a senha cont�m palavras comuns
  palavras_comuns = ["password", "123456", "qwerty"]
  if senha in palavras_comuns:
    return "Sua senha e muito comum. Tente uma senha mais complexa."
 # Verificar o comprimento m�nimo e crit�rios de valida��o
  numeros = ['0','1','2','3','4','5','6','7','8','9']
  for n in numeros:
    if n in senha:
      tem_numero = True
simbolo = ['*','!','@','#','$','%','~','^','&','+','-','?','/','>','<','|','=','(',')']
  for i in simbolo:
    if i in senha:
      tem_caractere_especial = True
if len(senha) >= comprimento_minimo and tem_letra_maiuscula and tem_letra_minuscula and tem_numero and tem_caractere_especial:
    return "Sua senha atende aos requisitos de seguranca. Parabens!"
  else:
    return "Sua senha nao atende aos requisitos de seguranca."
  
# Obtendo a senha do usu�rio
senha = input().strip()
# Verificando a for�a da senha
resultado = verificar_forca_senha(senha)
# Imprimindo o resultado
print(resultado)


#7� O Rob� inteligente. 
# Crie a Fun��o para classificar um n�mero como positivo, negativo ou zero
def classificar_numero(numero):
  while numero != 0:
    if numero > 0:
      return "positivo!"
    elif numero < 0:
      return "negativo!"
  def main():
      positivos = 0
      negativos = 0
   while True:
        numero = int(input())
# Encerra o loop se o usu�rio digitar 0.
    if numero == 0:
         break 
 # Chama a fun��o classificar_numero para imprimir a classifica��o do n�mero
        print(classificar_numero(numero))

 # Fa�a a verifica��o para saber quantos n�meros positivos e negativos foram inseridos
        if numero > 0:
           positivos+=1
        if numero < 0:
           negativos+=1
  # Imprime a quantidade de n�meros positivos e negativos inseridos
    print(f"{positivos} n�meros positivos, {negativos} n�meros negativos")
if __name__ == "__main__":
    main()


#8� A jornada da classifica��o frut�fera.
# Desenvolva a Fun��o para prever a classe da fruta
def prever_fruta(peso, textura, cor):
    # L�gica de decis�o baseada nas caracter�sticas fornecidas
    if peso >= 150 and textura == "smooth" and cor == "red":
        return "A fruta � um morango!"
    elif peso >= 130 and textura == "rough" and cor == "red":
        return "A fruta � uma ma��!"
    elif peso >= 120 and textura == "smooth" and cor == "orange":
        return "A fruta � uma laranja!"
    elif peso >= 150 and textura == "rough" and cor == "yellow":
        return "A fruta � uma banana!"
    else:
        return "N�o foi poss�vel classificar a fruta."
# Entrada do usu�rio
peso_fruta = float(input())
textura_fruta = input()
cor_fruta = input()
# Chamada da fun��o de previs�o
resultado = prever_fruta(peso_fruta, textura_fruta, cor_fruta)
# Sa�da da previs�o
print(resultado)


#9� A Quest�o Intrincada da Magia Preditiva
# Fun��o para prever a afinidade elemental do feiticeiro
def prever_afinidade_elemental(intensidade, componente_raro, fase_lunar, idade_feiticeiro, afinidade_animais):
 # Convertendo a resposta do componente raro e afinidade com animais para booleanos
    componente_raro = componente_raro.lower() == "sim"
    afinidade_animais = afinidade_animais.lower() == "sim"
# Desenvolva a L�gica de decis�o para prever a afinidade elemental
    if intensidade >= 5 and fase_lunar == "crescente" and idade_feiticeiro > 100:
        return "A afinidade elemental do feiticeiro � com o elemento Fogo!"
    elif intensidade >= 7 and True and fase_lunar == "cheia" and idade_feiticeiro <= 100 and afinidade_animais == False:
        return "A afinidade elemental do feiticeiro � com o elemento �gua!"
    elif intensidade >= 7 and True and fase_lunar == "cheia" and idade_feiticeiro <= 100 and True:
        return "A afinidade elemental do feiticeiro � com o elemento Terra!" 
    else:
        return "A afinidade elemental do feiticeiro � com o elemento Ar!"

# Entrada do usu�rio
intensidade_feitico = int(input())
componente_raro_feitico = input()
fase_lunar_feitico = input()
idade_feiticeiro = int(input ())
afinidade_animais_feiticeiro = input()
# Fazendo a previs�o
resultado = prever_afinidade_elemental(intensidade_feitico, componente_raro_feitico, fase_lunar_feitico, idade_feiticeiro, afinidade_animais_feiticeiro)
# Sa�da da previs�o
print(resultado)
