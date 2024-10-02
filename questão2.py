import re
def automato_computador (texto):
  estado = 0 
  posicoes = []
  casamentosExatos = []
  #Função de transição (delta) que descreve o automato
  transicoes = [
      {'c': 1},   #q0 -> q1 com 'c'
      {'o': 2},   #q1 -> q2 com 'o'
      {'m': 3},   #q2 -> q3 com 'm'
      {'p': 4},   #q3 -> q4 com 'p'
      {'u': 5},   #q4 -> q5 com 'u'
      {'t': 6},   #q5 -> q6 com 't'
      {'a': 7},   #q6 -> q7 com 'a'
      {'d': 8},   #q7 -> q8 com 'd'
      {'o': 9},   #q8 -> q9 com 'o'
      {'г': 0}    #q9 -> q0 com 'r' (volta ao estado inicial para continuar buscando)
  ]
  #Percorremos cada caractere do texto
  for i in range(len(texto)):
    char = texto[i]
    #Verificamos se existe uma transição no estado atual para o caractere
    if char in transicoes[estado]:
      estado = transicoes[estado][char]
    else:
      estado = 0 #Reinicia se não houver correspondência
      #Se chegamos ao estado final (49), encontramos uma ocorrência da palavra
    if estado = 9:
        posicoes.append(i+1) #Marca a posição da última letra 'r' estado Reinicia o estado para continuar buscando
        estado = 0 #Reinicia o estado para continuar buscando  
        #Verifica se o próximo caractere está disponível
        if i + 2 < len(texto):
            #Verifica se o próximo caractere é um espaço ou pontuação
            if texto[i + 2] in [" ", ".", ",", "!", "?", ";", ":"]: 
                  #Verifica se o caractere anterior não é uma letra
                  if not re.match(r'[a-zA-Z]', texto[(i - len("computador"))+1]): #verificando se a palavra está precedida por letras
                        casamentosExatos.append(i+1) # Marca como casamento exato
    return {'posicoes': posicoes, 'casamentos_exatos': casamentosExatos}
            
#Texto fornecido
texto = ("O computador é uma máquina capaz de variados tipos de tratamento automático de"
         "informações ou processamento de dados. Entende-se por computador um sistema físico que"
         "realiza algum tipo de computação. Assumiu-se que os computadores pessoais e laptops são"
         "ícones da era da informação. O primeiro computador eletromecânico foi construído por"
         "Konrad Zuse (1910–1995). Atualmente, um microcomputador é também chamado"
         "computador pessoal ou ainda computador doméstico.")

# Executa o automato
resultado = automato_computador(texto)
# Exibe as posições encontradas
print(f"A palavra 'computador' ocorre nas posições: {resultado['posicoes']}")
print(f"Os casamentos exatos ocorrem nas posições: {resultado['casamentos_exatos']}")
