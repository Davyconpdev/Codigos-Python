# Entrada de dados
quantidade_passos = int(input()) 
#verificando e  repetindo(la�o)
if(quantidade_passos>0):
         print('Explorador: 1 passo')
    for n in range(quantidade_passos +1):
         print('Explorador:',n,'passos'.format(n))
    elif(quantidade_passos==0):
         print("Nenhum passo dado na floresta.")
