# Faculdade Única de Ipatinga
# Ciência da Computação / Sistemas de Informação
# Professor: Julio Cézar
# Trabalho 1 - valor 5 pontos

# Legenda
# Zero representa o espaço vazio
# Linha 4 coluna 1 = referência para o nó pai,
# Linha 4 coluna 2 = (FH) distancia de manhatan (dman),
# Linha 4 coluna 3 = (FH) número de peças fora do lugar (npfl)
# Linha 5 coluna 1 = (Custo do caminho) Profundidade
# A* = f(h) = g(n) + h(n)
import copy

tabuleiro_inicial = [[3, 4, 2],
                     [5, 1, 7],
                     [6, 0, 8], 
                     [0, 0, 0],
                     [0, 0, 0]] 

alvo = [[1, 2, 3],
        [8, 0, 4],
        [7, 6, 5]]


def verifica_alvo(tab):
    if tab[:3][:3] == alvo:
        return True
    else:
        return False

def imprime_tabuleiro(tab): 
  print('Profundidade do nó:', tab[4][0])
  print(tab[0])
  print(tab[1])
  print(tab[2])

def imprime_jogadas(tab):
  print("\nAs jogadas foram:")
  pilha = []
  #vai do nó objetivo até o nó raiz
  while(tab[3][1] != None): 
    pilha.append(tab)
    tab = tab[3][1]
  pilha.append(tab)
  while(len(pilha)>0):
    temp = pilha.pop()
    imprime_tabuleiro(temp)

def checa_tabuleiros(tab1, tab2): 
  sao_iguais = True 
  for i in range(3):
    for j in range(3):
      if tab1[i][j] != tab2[i][j]:
        sao_iguais = False
  return sao_iguais

def expandir_no(tab):   #retorna um conjunto de nós filhos com as próximas jogadas possíveis
  jogadas = [] #armazena os tabuleiros jogadas possíveis
   # 1 se vazio esta no meio do tabuleiro
  if tab[1][1] == 0:
    # move pra cima o zero
    a = copy.deepcopy(tab)  # copia o objeto
    a[1][1] = a[0][1]
    a[0][1] = 0
    a[4][0] = a[4][0] + 1  # profundidade do nó
    a[3][0] = tab  # criar referencia para o nó pai
    a[3][1] = dman(a[:3])
    a[3][2] = npfl(a[:3])
    jogadas.append(a)
    # move pra esquerda o zero
    a = copy.deepcopy(tab)  # copia o objeto
    a[1][1] = a[1][0]
    a[1][0] = 0
    a[4][0] = a[4][0] + 1  # profundidade do nó
    a[3][0] = tab
    a[3][1] = dman(a[:3])
    a[3][2] = npfl(a[:3])
    jogadas.append(a)
    # move pra direta o zero
    a = copy.deepcopy(tab)  # copia o objeto
    a[1][1] = a[1][2]
    a[1][2] = 0
    a[4][0] = a[4][0] + 1  # profundidade do nó
    a[3][0] = tab
    a[3][1] = dman(a[:3])
    a[3][2] = npfl(a[:3])
    jogadas.append(a)
    # move pra baixo o zero
    a = copy.deepcopy(tab)  # copia o objeto
    a[1][1] = a[2][1]
    a[2][1] = 0
    a[4][0] = a[4][0] + 1  # profundidade do nó
    a[3][0] = tab
    a[3][1] = dman(a[:3])
    a[3][2] = npfl(a[:3])
    jogadas.append(a)
  elif tab[0][0] == 0:
     # move pra direita o zero
    a = copy.deepcopy(tab)  # copia o objeto
    a[0][0] = a[0][1]
    a[0][1] = 0
    a[4][0] = a[4][0] + 1  # profundidade do nó
    a[3][0] = tab
    a[3][1] = dman(a[:3])
    a[3][2] = npfl(a[:3])
    jogadas.append(a)
     # move pra baixo o zero
    a = copy.deepcopy(tab)  # copia o objeto
    a[0][0] = a[1][0]
    a[1][0] = 0
    a[4][0] = a[4][0] + 1  # profundidade do nó
    a[3][0] = tab
    a[3][1] = dman(a[:3])
    a[3][2] = npfl(a[:3])
    jogadas.append(a)
  elif tab[0][1] == 0:
    # move pra esquerda o zero
    a = copy.deepcopy(tab)  # copia o objeto
    a[0][1] = a[0][0]
    a[0][0] = 0
    a[4][0] = a[4][0] + 1  # profundidade do nó
    a[3][0] = tab
    a[3][1] = dman(a[:3])
    a[3][2] = npfl(a[:3])
    jogadas.append(a)

    # move pra direita o zero
    a = copy.deepcopy(tab)  # copia o objeto
    a[0][1] = a[0][2]
    a[0][2] = 0
    a[4][0] = a[4][0] + 1  # profundidade do nó
    a[3][0] = tab
    a[3][1] = dman(a[:3])
    a[3][2] = npfl(a[:3])
    jogadas.append(a)

    # move pra baixo o zero
    a = copy.deepcopy(tab)  # copia o objeto
    a[0][1] = a[1][1]
    a[1][1] = 0
    a[4][0] = a[4][0] + 1  # profundidade do nó
    a[3][0] = tab
    a[3][1] = dman(a[:3])
    a[3][2] = npfl(a[:3])
    jogadas.append(a)

  elif tab[0][2] == 0:
     # move pra esquerda o zero
    a = copy.deepcopy(tab)  # copia o objeto
    a[0][2] = a[0][1]
    a[0][1] = 0
    a[4][0] = a[4][0] + 1  # profundidade do nó
    a[3][0] = tab
    a[3][1] = dman(a[:3])
    a[3][2] = npfl(a[:3])
    jogadas.append(a)

    # move pra baixo o zero
    a = copy.deepcopy(tab)  # copia o objeto
    a[0][2] = a[1][2]
    a[1][2] = 0
    a[4][0] = a[4][0] + 1  # profundidade do nó
    a[3][0] = tab
    a[3][1] = dman(a[:3])
    a[3][2] = npfl(a[:3])
    jogadas.append(a)

  elif tab[1][0] == 0:
    # move pra cima o zero
    a = copy.deepcopy(tab)  # copia o objeto
    a[1][0] = a[0][0]
    a[0][0] = 0
    a[4][0] = a[4][0] + 1  # profundidade do nó
    a[3][0] = tab
    a[3][1] = dman(a[:3])
    a[3][2] = npfl(a[:3])
    jogadas.append(a)

    # move pra baixo o zero
    a = copy.deepcopy(tab)  # copia o objeto
    a[1][0] = a[2][0]
    a[2][0] = 0
    a[4][0] = a[4][0] + 1  # profundidade do nó
    a[3][0] = tab
    a[3][1] = dman(a[:3])
    a[3][2] = npfl(a[:3])
    jogadas.append(a)

    # move pra direita o zero
    a = copy.deepcopy(tab)  # copia o objeto
    a[1][0] = a[1][1]
    a[1][1] = 0
    a[4][0] = a[4][0] + 1  # profundidade do nó
    a[3][0] = tab
    a[3][1] = dman(a[:3])
    a[3][2] = npfl(a[:3])
    jogadas.append(a)

  elif tab[1][2] == 0:
    # move pra baixo o zero
    a = copy.deepcopy(tab)  # copia o objeto
    a[1][2] = a[2][2]
    a[2][2] = 0
    a[4][0] = a[4][0] + 1  # profundidade do nó
    a[3][0] = tab
    a[3][1] = dman(a[:3])
    a[3][2] = npfl(a[:3])
    jogadas.append(a)
    
    # move pra cima o zero
    a = copy.deepcopy(tab)  # copia o objeto
    a[1][2] = a[0][2]
    a[0][2] = 0
    a[4][0] = a[4][0] + 1  # profundidade do nó
    a[3][0] = tab
    a[3][1] = dman(a[:3])
    a[3][2] = npfl(a[:3])
    jogadas.append(a)

    # move pra esquerda o zero
    a = copy.deepcopy(tab)  # copia o objeto
    a[1][2] = a[1][1]
    a[1][1] = 0
    a[4][0] = a[4][0] + 1  # profundidade do nó
    a[3][0] = tab
    a[3][1] = dman(a[:3])
    a[3][2] = npfl(a[:3])
    jogadas.append(a)

  elif tab[2][0] == 0:
    # move pra cima o zero
    a = copy.deepcopy(tab)  # copia o objeto
    a[2][0] = a[1][0]
    a[1][0] = 0
    a[4][0] = a[4][0] + 1  # profundidade do nó
    a[3][0] = tab
    a[3][1] = dman(a[:3])
    a[3][2] = npfl(a[:3])
    jogadas.append(a)

    # move pra direita o zero
    a = copy.deepcopy(tab)  # copia o objeto
    a[2][0] = a[2][1]
    a[2][1] = 0
    a[4][0] = a[4][0] + 1  # profundidade do nó
    a[3][0] = tab
    a[3][1] = dman(a[:3])
    a[3][2] = npfl(a[:3])
    jogadas.append(a)

  elif tab[2][1] == 0:
    # move pra cima o zero
    a = copy.deepcopy(tab)  # copia o objeto
    a[2][1] = a[1][1]
    a[1][1] = 0
    a[4][0] = a[4][0] + 1  # profundidade do nó
    a[3][0] = tab
    a[3][1] = dman(a[:3])
    a[3][2] = npfl(a[:3])
    jogadas.append(a)

    # move pra esquerda o zero
    a = copy.deepcopy(tab)  # copia o objeto
    a[2][1] = a[2][0]
    a[2][0] = 0
    a[4][0] = a[4][0] + 1  # profundidade do nó
    a[3][0] = tab
    a[3][1] = dman(a[:3])
    a[3][2] = npfl(a[:3])
    jogadas.append(a)

    # move pra direita o zero
    a = copy.deepcopy(tab)  # copia o objeto
    a[2][1] = a[2][2]
    a[2][2] = 0
    a[4][0] = a[4][0] + 1  # profundidade do nó
    a[3][0] = tab
    a[3][1] = dman(a[:3])
    a[3][2] = npfl(a[:3])
    jogadas.append(a)

  elif tab[2][2] == 0:
    # move pra cima o zero
    a = copy.deepcopy(tab)  # copia o objeto
    a[2][2] = a[1][2]
    a[1][2] = 0
    a[4][0] = a[4][0] + 1  # profundidade do nó
    a[3][0] = tab
    a[3][1] = dman(a[:3])
    a[3][2] = npfl(a[:3])
    jogadas.append(a)

    # move pra esquerda o zero
    a = copy.deepcopy(tab)  # copia o objeto
    a[2][2] = a[2][1]
    a[2][1] = 0
    a[4][0] = a[4][0] + 1  # profundidade do nó
    a[3][0] = tab
    a[3][1] = dman(a[:3])
    a[3][2] = npfl(a[:3])
    jogadas.append(a)

  #retorno do conjunto de jogadas (nós)
  return jogadas

#heurística: numero de peças fora do lugar
def npfl(tab):
    num = 0
    if tab[0][0] != alvo[0][0]: num = num+1
    if tab[0][1] != alvo[0][1]: num = num+1
    if tab[0][2] != alvo[0][2]: num = num+1
    if tab[1][0] != alvo[1][0]: num = num+1
    if tab[1][1] != alvo[1][1]: num = num+1
    if tab[1][2] != alvo[1][2]: num = num+1
    if tab[2][0] != alvo[2][0]: num = num+1
    if tab[2][1] != alvo[2][1]: num = num+1
    if tab[2][2] != alvo[2][2]: num = num+1
    return num

# Busca índices para Distância de Manhattan
# pos = 0 (linha)
# pos = 1 (coluna)
def indices(elem, pos):
    for i in range(3):
        for j in range(3):
            if alvo[i][j] == elem :
                if pos == 0 :
                    return i
                return j

#Heurística: distancia_manhattan
def dman(tab):
    h = 0
    for i in range(3):
        for j in range(3):
            if tab[i][j] != 0 and tab[i][j] != alvo[i][j]:
                h = h + abs(indices(tab[i][j], 0) - i) + abs(indices(tab[i][j], 1) - j)
    return h

#ganho: A* = custo real do caminho, ou seja, a cada nó expandido soma-se +1
# a variável ganho


#############################
#ALGORITMOS DE BUSCA
#############################
 
#def busca_a_estrela(tab):

#implementar
    

####################
### MENU
####################

#print('*** IA - Jogo dos Oito  ***')
#print('*** O tabuleiro inicial ***')
#imprime_tabuleiro(tabuleiro_inicial)
#print('Informe qual algoritmo deseja utilizar: ')
#print("1: Busca Cega em Largura")
#print("2: Busca Cega em Profundidade")
#print("3: Busca Com Informação (A*) Heurística peças fora do lugar")
#print("4: Busca Com Informação (A*) Heurística Dist. Manhattan")
print(dman(tabuleiro_inicial))
#opcao = int(input('Informe uma opção: '))
#if(op==1):
#  busca_largura(tabuleiro_inicial)
#elif(op==2):
#  busca_profundidade(tabuleiro_inicial)
#elif(op==3):
#  busca_a_estrela(tabuleiro_inicial, 1)
#elif(op==4):
#  busca_a_estrela(tabuleiro_inicial, 2)
#print(tabuleiro_inicial[:3][:3]  ) 