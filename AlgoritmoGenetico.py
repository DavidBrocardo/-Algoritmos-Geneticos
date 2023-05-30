#---------------------------Descrição------------------------------#
#                Algoritmo Genetico
# Autores : David Antonio Brocardo
#         : Leonardo Bednarczuk Balan de Oliveira
#         : Gabriel Santos da Silva
# Função de Otimização:
#            𝑍 = − (100∗(𝑥^2−𝑦)^2+(1−𝑥)^2)
# Restrições:
#            𝑥 ∈ [−2,2]
#            𝑦 ∈ [−2,2]
#Valores Base:
#           𝑥=1, 𝑦=1, 𝑧=0
#  Codificação: binária
#  Método de Seleção: ranking
#  Método de Cruzamento: dois pontos fixos
#  Método de Mutação: binária
#  Elitismo: 0,5% por geração
#-----------------------------------------------------------------#

#      Importação da bibiloteca ultilizadas
import math  # bibiloteca de funções matemáticas
import random  # necessário para utilizar o módulo random
import Graficos  #Referente ao arquivo Graficos.py , responsavel pela geração dos graficos

#      Variaveis
#declaração de variáveis
x1 = float
y1 = float
z1 = float

x = []  # Os vetores X, Y, Z serão os responsaveis por armazenar a populacao
y = [
]  # Sendo que o Z será o resultados dos fitness dos pais X e Y, sendo que cada conjunto x e y é um elemento
z = []

melhoresZ = [
]  #Responsável por armazenar os melhores fitness de todas as interações
newPopX = [
]  #Vetores que serão ulizados para armazenar a novas populações, resultante do cruzamento, mutação ..
newPopY = []

melhorResposta = int
melhorX = float
melhorY = float
melhorZ = float
MelhorValor = float
MelhorValor = 55555555.55555  #Valor alto, somente para que na primeira interção qualquer valor que seja, possa ser armazenado
melhorRes1 = int
melhorRes1 = 100000
melhorRes2 = int
melhorRes2 = 100000
valoresCruzados = int
valoresCruzados = 10
menordis = float
menordis = 1000000000


#--------------------------------FUNÇÕES----------------------------------#
#=========================================================================
# Responsavel por gerar a população inicial
# Somemente ultilizado uma unica vez
def randXYZ():
  for i in range(200):
    #para gerar valores negativos usa-se o random de 0 à 4 e subtraí-se 2 depois, pois: x[-2,2] e y[-2,2];
    x.append(random.uniform(0, 4) - 2)
    y.append(random.uniform(0, 4) - 2)
    z.append(
      calculoZ(x[i], y[i])
    )  #Já realiza o calculo do fitness dos primeiros valores e armazena no vetor z
  return 0


#=================================================================


#=================================================================
# Função para o calculo do FITNESS
# def calculoZ( x1,  y1):
# Calcula o fitness através dos valores aleatorios de X e Y (Na primeira interação)
# A parti da segunda interação calcula o fitness atraves dos valores ja cruzados mutados...
# parametros:
def calculoZ(x1, y1):
  # Função base: 𝑍 = −(100 ∗ (𝑥^2 − 𝑦)^2 + (1 − 𝑥)^2)
  z1 = -(100 * ((x1**2) - y1)**2 + (1 - x1)**2)
  return z1


#=================================================================
#Responsavel por retorna o melhor elemento de um conjunto de valores
#Ultilizada para definir qual valor será feito o cruzamento
#Ao qual seleciona sempre o melhor


def rank(x1, y1, z1):
  #declaração das distancias pro melhor resultado
  distX = float
  distY = float
  distZ = float
  #valor aleatório grande para a 1º iteração

  # X
  distX = x1 - 1
  if (distX < 0):
    distX *= -1
  # Y
  distY = y1 - 1
  if (distY < 0):
    distY *= -1
  distZ = z1 - 1
  # Z
  if (distZ < 0):
    distZ *= -1
  dist = float
  dist = (float)(distX + distY + distZ)

  return dist


#=================================================================
# def Elitismo (x1, y1 ,z1):
# Seleciona a melhor Resposta por interação
# Elitismo de 0.5%
# Como estamos trabalhando com uma população de 200 individuos, o eletismo retornara somente um 1 individuo.
# O elemento selecionado, será o qual apresenta o melhor fitness


def Elitismo(x1, y1, z1):
  #declaração das distancias pro melhor resultado
  distX = float
  distY = float
  distZ = float
  #valor aleatório grande para a 1º iteração
  distX = 10.0
  distY = 10.0
  distZ = 1000.0
  menordis = 100000000055505
  melhorRes = int

  for i in range(200):  #range conta de 0 a 200
    # X
    distX = x[i] - 1
    if (distX < 0):
      distX *= -1
    # Y
    distY = y[i] - 1
    if (distY < 0):
      distY *= -1
    distZ = z[i] - 1
    # Z
    if (distZ < 0):
      distZ *= -1
    dist = float
    dist = (float)(distX + distY + distZ)

    if (dist < menordis):
      menordis = dist
      melhorRes = i

  return melhorRes


#=================================================================


#=================================================================
# Função para transformar float para binario
# Para posteriomente realizar o cruzamento e a mutação
def floatParabin(number):
  inteira, decimal = str(number).split(".")  #separa a parte inteira da decimal
  #forçar os dois valores à tipagem inteira
  inteira = int(inteira)
  decimal = int(decimal)
  res1 = bin(inteira).lstrip("") + "."
  res2 = bin(decimal).lstrip("0b")

  #lstrip: método retorna uma cópia da string com os caracteres iniciais requeridos removidos
  res3 = res1 + res2  #parte inteira(em binário)+ parte decimal(em binário)
  return res3


#=================================================================


#=================================================================
# Função para transformar binario para int
# Funcao necessaria para o funcionamento da função BinparaFloat
def binary2int(binary):
  int_val, i, = 0, 0,
  while (binary != 0):
    a = binary % 10
    int_val = int_val + a * pow(2, i)
    binary = binary // 10
    i += 1
  return int_val


#=================================================================

#=================================================================
# Função para transformar de binario para float
# Para posteriomente realizar o novo calculo do fitness


def BinparaFloat(number):
  neg = int
  newFloat = float
  resulInt = float
  resulDeci = float

  inteira, decimal = str(number).split(".")  #separa a parte inteira da decimal
  if ((inteira == "-0b1")):
    neg = 1
  if ((inteira == "-0b0")):
    neg = 1

  inteira = inteira.lstrip('-0b')

  if (inteira == ""):
    inteira = "0"

  inteira = int(inteira)
  decimal = int(decimal)

  resulInt = float(binary2int(inteira))
  resulDeci = float(binary2int(decimal))

  while (resulDeci > 1):
    resulDeci = resulDeci / 10

  newFloat = resulInt + resulDeci
  if (neg == 1):
    newFloat = newFloat * -1
    neg = 0

  return newFloat


#=================================================================


#=================================================================
# Função responsavel pelo cruzamento de 2 pontos fixos
# Tendo como entrada 2 pais , e saida 2 filhos
# o conjunto Pai1X e Pai1Y corresponde a um pai somente
# o mesmo vale filho1X, filho1Y
def Cruzamento(Pai1X, Pai1Y, Pai2X, Pai2Y):
  filho1X = []
  filho1Y = []
  filho2X = []
  filho2Y = []
  cruzaSimNao = random.uniform(0, 1)
  if (cruzaSimNao < 0.7):
    #Realiza o Cruzamento somente se a taxa de cruzamento for aceita
    if (len(Pai1X) < len(Pai2X)):
      tamanhoX = len(Pai1X)
    else:
      tamanhoX = len(Pai2X)

    for i in range(tamanhoX):
      if ((i < 9)
          or (i > 16)):  #cruzamento de bits entre os pais x e y, metade|metade
        filho1X.append(Pai1X[i])
        filho2X.append(Pai2X[i])
      else:
        filho1X.append(Pai2X[i])
        filho2X.append(Pai1X[i])

      if (len(Pai1Y) < len(Pai2Y)):
        tamanhoY = len(Pai1Y)
      else:
        tamanhoY = len(Pai2Y)

    for i in range(tamanhoY):
      if ((i < 9)
          or (i > 16)):  #cruzamento de bits entre os pais x e y, metade|metade
        filho1Y.append(Pai1Y[i])
        filho2Y.append(Pai2Y[i])
      else:
        filho1Y.append(Pai2Y[i])
        filho2Y.append(Pai1Y[i])
    for i in range(tamanhoY - 1):
      filho1Y[0] = (filho1Y[0] + filho1Y[i + 1])
      filho2Y[0] = (filho2Y[0] + filho2Y[i + 1])
    for i in range(tamanhoX - 1):
      filho1X[0] = (filho1X[0] + filho1X[i + 1])
      filho2X[0] = (filho2X[0] + filho2X[i + 1])
    return filho1X[0], filho1Y[0], filho2X[0], filho2Y[0]
  else:
    #Caso a taxa de cruzamento não seja aceita mantem-se os mesmos valores
    return Pai1X, Pai1Y, Pai2X, Pai2Y


#=================================================================
#=================================================================
# Função responsavel pela Mutação dos filhos
# recebe como entrada somente um filho
# E sua mutação ocorrera somente se a taxa de mutação for aceita
def Mutacao(filho):
  filhoMutado = []
  tamanho = len(filho)
  for i in range(tamanho):
    if (i > 1):
      mutaSimNao = random.uniform(0, 1)
      #Se o valor for igual a 1 o bit sera invertido
      if (filho[i] == "."):
        filhoMutado.append(".")
      else:
        if (mutaSimNao < 0.05):
          if (filho[i] == "0"):
            filhoMutado.append("1")
          else:
            filhoMutado.append("0")
        else:
          filhoMutado.append(filho[i])
    else:
      filhoMutado.append(filho[i])
  for i in range(tamanho - 1):
    filhoMutado[0] = (filhoMutado[0] + filhoMutado[i + 1])
  return filhoMutado[0]


#=======================================================================


#=======================================================================
# Função responsavel por definir quais valores serao cruzados e mutados
# Recebe como parametro a ultima população, já com os melhores valores mantidos
# é responsavel também por chamar as funções rank, floatParabin , Cruzamento , Mutacao e BinparaFloat
# Tem como retorno para função main a nova população
def novaPop(x, y, z):

  tamanhoPopulacao = 200
  MelhorValor = 10000000
  while (len(newPopX) < tamanhoPopulacao):

    for i in range(5):
      valoresCruzados = random.randint(0, 199)

      rankValor = rank(x[valoresCruzados], y[valoresCruzados],
                       z[valoresCruzados])
      if (rankValor < MelhorValor):
        MelhorValor = rankValor
        melhorRes1 = valoresCruzados
    MelhorValor = 1000000
    for i in range(5):
      valoresCruzados = random.randint(0, 199)
      rankValor = rank(x[valoresCruzados], y[valoresCruzados],
                       z[valoresCruzados])
      if (rankValor < MelhorValor):
        if (valoresCruzados != melhorRes1):
          MelhorValor = rankValor
          melhorRes2 = valoresCruzados
      else:
        i = i - 1

    #Transformando de Float para binario

    newX1 = floatParabin(x[melhorRes1])
    newY1 = floatParabin(y[melhorRes1])
    newX2 = floatParabin(x[melhorRes2])
    newY2 = floatParabin(y[melhorRes2])

    #xbin e ybin são os valores ja cruzados
    newX1, newY1, newX2, newY2 = Cruzamento(newX1, newY1, newX2, newY2)
    newX1 = Mutacao(newX1)
    newY1 = Mutacao(newY1)
    newX2 = Mutacao(newX2)
    newY2 = Mutacao(newY2)

    newPopX.append(BinparaFloat(newX1))
    newPopY.append(BinparaFloat(newY1))
    newPopX.append(BinparaFloat(newX2))
    newPopY.append(BinparaFloat(newY2))

  return newPopX, newPopY


#===================================================================================#

#------------------------------------->Main<---------------------------------------#
# Responsavel por chamar todas as funções necessarias para a otimização do algoritmo

#Gerando a população inicial
Graficos.ApagaGraficos(
)  #Limpa a pasta que contem as jpgs dos graficos da ultima execução
randXYZ()
NumElementos = 200
melhorResposta = Elitismo(
  x, y, z)  #Armazena a posição do vetor da melhor valor da iteração

#A melhor resposta passar direto para proxima interação
Melhorx = x[melhorResposta]
Melhory = y[melhorResposta]
Melhorz = z[melhorResposta]
MtodosX = float
MtodosY = float
MtodosZ = float
newPopX.append(Melhorx)
newPopY.append(Melhory)

xpenultima = []  #Responsavel por armazenar a ultima interação
ypenultima = []
melhorAtual = melhorResposta

#Calculo do Fitness da populaçao inicial
for i in range(200):
  xpenultima.append(x[i])
  ypenultima.append(y[i])
  z[i] = calculoZ(x[i], y[i])
x.clear()
y.clear()
#Aqui sera realizados a  quantidade INTERAÇÕES solicitadas

for i in range(50):
  x, y = novaPop(xpenultima, ypenultima, z)  #gera a nova população
  for a in range(200):
    xpenultima.append(x[a])
    ypenultima.append(y[a])
    z[a] = calculoZ(x[a], y[a])  #Calculo do fitness da nova população
  melhorResposta = Elitismo(x, y, z)  #melhor valor a cada iteração

  Melhorx = x[melhorResposta]
  Melhory = y[melhorResposta]
  print("Melhor Resposta da interação : ", i)
  print("x:", x[melhorResposta])
  print("y:", y[melhorResposta])
  print("z:", z[melhorResposta])
  #Grafico resposavel por mostrar a disposição do individuos ao passar das gerações
  Graficos.imgInteracao(x, y, i)

  melhoresZ.append(
    z[melhorResposta])  #Resposavel por armazenar os melhores fitness

  # Como já está salvo no vetor xpenultima e ypenultima podemos limpara os vetores x , y , newPopX , newPoy , para as proximas interações
  x.clear()
  y.clear()
  newPopX.clear()
  newPopY.clear()

  #como o vetores então limpos , podemos já armazenar a melhor resposta até entao, na nova população
  newPopX.append(Melhorx)
  newPopY.append(Melhory)
  melhorResposta = 0

#Grafico para apresentar todas as melhores resposta durante a execução do algoritmo
Graficos.GraficoEvolucaoDoFitness(melhoresZ)
