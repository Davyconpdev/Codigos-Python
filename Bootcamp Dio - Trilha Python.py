#1º  Desafio: A Aventura do Explorador
# Entrada de dados
quantidade_passos = int(input()) 
#verificando e  repetindo(laço)
if(quantidade_passos>0):
         print('Explorador: 1 passo')
    for n in range(2,quantidade_passos +1):
         print('Explorador:',n,'passos'.format(n))
    elif(quantidade_passos==0):
         print("Nenhum passo dado na floresta.")


#2º Lista de itens do personagem do jogo
#Solicitando e cadastrando os itens informados pelo usuário
i1 = input()
i2 = input()
i3 = input()
# Lista para armazenar os itens
itens = [i1 ,i2 ,i3]
# Exibindo a lista de itens
print("Lista de itens:")
for item in itens:
    print(f"- {item}")


#3º Armazenamento de dados é vida
#Solicitando os valores 
capacidade_atual, aumento_percentual = map(int, input().split())
resultado = int(capacidade_atual * aumento_percentual / 100 + capacidade_atual)
   print(resultado)


#4º O grande depósito-solucionando problemas bancários
valor = float(input())
#verificando o valor (R$) informado
if valor > 0:
   print('Deposito realizado com sucesso!')
   print('Saldo atual: R$ %.2f'%valor)
elif valor < 0:
    print('Valor invalido! Digite um valor maior que zero.')
else:
    print('Encerrando o programa...')

  
#5º Estrtura de dados: organizando os seus ativos
#lista 
ativos = []
#Entrada da quantidade de ativos
quantidadeAtivos = int(input())

#Entrada dos códigos dos ativos
for i in range(quantidadeAtivos):
    codigoAtivo = input()
    ativos.append(codigoAtivo)
# Ordenar os ativos em ordem alfabética.
    ativos = sorted(ativos)
#Imprimir a lista de ativos ordenada, conforme a tabela de exemplos.
print(ativos[0])
print(ativos[-2])
print(ativos[-1])


#6º  Validando a Força de Senhas no IAM.
def verificar_forca_senha(senha):
  comprimento_minimo = 8
  tem_letra_maiuscula = False
  tem_letra_minuscula = False
  tem_numero = False
  tem_caractere_especial = False
# Verificando o comprimento da senha
  if len(senha) < comprimento_minimo:
    return f"Sua senha e muito curta. Recomenda-se no minimo {comprimento_minimo} caracteres."
#  Verifique se a senha contém letras maiúsculas e minúsculas
  maiúsculas = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','X','Y','Z']
 for l in maiúsculas:
    if l in senha:
      tem_letra_maiuscula = True
    elif l.lower() in senha:
      tem_letra_minuscula = True
  # Verificando se a senha contém sequências comuns
  sequencias_comuns = ["123456", "abcdef"]
  for sequencia in sequencias_comuns:
    if sequencia in senha:
      return "Sua senha contem uma sequencia comum. Tente uma senha mais complexa."
 # Verificando se a senha contém palavras comuns
  palavras_comuns = ["password", "123456", "qwerty"]
  if senha in palavras_comuns:
    return "Sua senha e muito comum. Tente uma senha mais complexa."
 # Verificar o comprimento mínimo e critérios de validação
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
  
# Obtendo a senha do usuário
senha = input().strip()
# Verificando a força da senha
resultado = verificar_forca_senha(senha)
# Imprimindo o resultado
print(resultado)


#7º O Robô inteligente. 
# Crie a Função para classificar um número como positivo, negativo ou zero
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
# Encerra o loop se o usuário digitar 0.
    if numero == 0:
         break 
 # Chama a função classificar_numero para imprimir a classificação do número
        print(classificar_numero(numero))

 # Faça a verificação para saber quantos números positivos e negativos foram inseridos
        if numero > 0:
           positivos+=1
        if numero < 0:
           negativos+=1
  # Imprime a quantidade de números positivos e negativos inseridos
    print(f"{positivos} números positivos, {negativos} números negativos")
if __name__ == "__main__":
    main()


#8º A jornada da classificação frutífera.
# Desenvolva a Função para prever a classe da fruta
def prever_fruta(peso, textura, cor):
    # Lógica de decisão baseada nas características fornecidas
    if peso >= 150 and textura == "smooth" and cor == "red":
        return "A fruta é um morango!"
    elif peso >= 130 and textura == "rough" and cor == "red":
        return "A fruta é uma maçã!"
    elif peso >= 120 and textura == "smooth" and cor == "orange":
        return "A fruta é uma laranja!"
    elif peso >= 150 and textura == "rough" and cor == "yellow":
        return "A fruta é uma banana!"
    else:
        return "Não foi possível classificar a fruta."
# Entrada do usuário
peso_fruta = float(input())
textura_fruta = input()
cor_fruta = input()
# Chamada da função de previsão
resultado = prever_fruta(peso_fruta, textura_fruta, cor_fruta)
# Saída da previsão
print(resultado)


#9º A Questão Intrincada da Magia Preditiva
# Função para prever a afinidade elemental do feiticeiro
def prever_afinidade_elemental(intensidade, componente_raro, fase_lunar, idade_feiticeiro, afinidade_animais):
 # Convertendo a resposta do componente raro e afinidade com animais para booleanos
    componente_raro = componente_raro.lower() == "sim"
    afinidade_animais = afinidade_animais.lower() == "sim"
# Desenvolva a Lógica de decisão para prever a afinidade elemental
    if intensidade >= 5 and fase_lunar == "crescente" and idade_feiticeiro > 100:
        return "A afinidade elemental do feiticeiro é com o elemento Fogo!"
    elif intensidade >= 7 and True and fase_lunar == "cheia" and idade_feiticeiro <= 100 and afinidade_animais == False:
        return "A afinidade elemental do feiticeiro é com o elemento Água!"
    elif intensidade >= 7 and True and fase_lunar == "cheia" and idade_feiticeiro <= 100 and True:
        return "A afinidade elemental do feiticeiro é com o elemento Terra!" 
    else:
        return "A afinidade elemental do feiticeiro é com o elemento Ar!"

# Entrada do usuário
intensidade_feitico = int(input())
componente_raro_feitico = input()
fase_lunar_feitico = input()
idade_feiticeiro = int(input ())
afinidade_animais_feiticeiro = input()
# Fazendo a previsão
resultado = prever_afinidade_elemental(intensidade_feitico, componente_raro_feitico, fase_lunar_feitico, idade_feiticeiro, afinidade_animais_feiticeiro)
# Saída da previsão
print(resultado)
