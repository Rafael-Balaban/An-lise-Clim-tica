# Nome: Rafael Rosa Balaban Borba
# Data: 07/04/2024

# Leitura do arquivo
def cargaDados(nome):
  arq = open(nome,"r")
  dados = []

  for linha in arq:
    linha1 = linha[:-1] #Para retirar o \n
    dados.append(linha1)
  arq.close()
  return dados

# Para gerar uma lista do arquivo sem o cabecalho
def geraListaSemCabecalho(lista):
  nova = []
  ind = 1
  while ind < len(lista):
    nova.append(lista[ind])
    ind += 1
  return nova

# Para criar uma lista com somente os dados do intervalo
def separar(data1, data2):
  intervalo = []
  somaData1 = (int(data1.split('/')[2])*10000) + (int(data1.split('/')[1])*100) + (int(data1.split('/')[0]))
  somaData2 = (int(data2.split('/')[2])*10000) + (int(data2.split('/')[1])*100) + (int(data2.split('/')[0]))

  if somaData1 > somaData2: # Caso a segunda data digitada seja maior que a primeira
    aux = somaData1
    somaData1 = somaData2
    somaData2 = aux

  for item in listaSemCabe:
    colunas = item.split(',')
    data = colunas[0]
    somaData = (int(data.split('/')[2])*10000) + (int(data.split('/')[1])*100) + (int(data.split('/')[0]))

    if somaData >= somaData1 and somaData <= somaData2:
      intervalo.append(item)

  return intervalo

# Entrega todos os dados do intervalo
def todosDados(lista):
  data = []
  precip = []
  maxima = []
  minima = []
  tempMedia = []
  umidadeRelativa = []
  veloVento = []

  for item in lista:
    colunas = item.split(',')
    data.append(str(colunas[0]))
    precip.append(float(colunas[1]))
    maxima.append(float(colunas[2]))
    minima.append(float(colunas[3]))
    tempMedia.append(float(colunas[5]))
    umidadeRelativa.append(float(colunas[6]))
    veloVento.append(float(colunas[7]))

  for cont in range(0,len(lista)):
    print("Data: ",data[cont],end=";")
    print(f" Precipitação: {precip[cont]:.1f}",end=";")
    print(f" Temp. Máx.: {maxima[cont]:.1f}",end=";")
    print(f" Temp. Min.: {minima[cont]:.1f}",end=";")
    print(f" Temp. Média: {tempMedia[cont]:.1f}",end=";")
    print(f" Umidade relativa: {umidadeRelativa[cont]:.1f}",end=";")
    print(f" Velocidade do vento: {veloVento[cont]:.2f}km/h")

# Entrega a precipitação
def precipitacao(lista):
  data = []
  precip = []

  for item in lista:
    colunas = item.split(',')
    data.append(str(colunas[0]))
    precip.append(float(colunas[1]))

  for cont in range(0,len(lista)):
    print("Data: ",data[cont], " - Precipitação: ", precip[cont])

# Entrega a temperatura
def temperatura(lista):
  data = []
  temp = []

  for item in lista:
    colunas = item.split(',')
    data.append(str(colunas[0]))
    temp.append(float(colunas[5]))

  for cont in range(0,len(lista)):
    print("Data: ",data[cont], " - temperatura: ", temp[cont])

# Entrega a umidade e a velocidade do vento
def umidadeVento(lista):
  data = []
  umidade = []
  vento = []

  for item in lista:
    colunas = item.split(',')
    data.append(str(colunas[0]))
    umidade.append(float(colunas[6]))
    vento.append(float(colunas[7]))

  for cont in range(0,len(lista)):
    print(f"Data: {data[cont]}  - Umidade: {umidade[cont]:.2f} - Velocidade do vento: {vento[cont]:.2f}km/h")

# Gera o mês mais chuvoso do arquivo
def mesMaisChuvoso(lista):
  maiorPrecip = []
  dataMaisChuvoso = []
  dic = {}

  for item in lista:
    precip = []
    data = []
    colunas = item.split(',')
    data.append(colunas[0])
    precip.append(float(colunas[1]))

    if precip > maiorPrecip:
      maiorPrecip = precip
      dataMaisChuvoso = data

  dic[dataMaisChuvoso[0]] = maiorPrecip
  return dic

info = cargaDados("temperatura-umidade-vento-chuva.csv")
listaSemCabe = geraListaSemCabecalho(info)

# Parte visual
while True:
  # Escolhas
  print("Digite 1 para ver todos os dados do período informado.")
  print("Digite 2 para ver apenas os dados de precipitação do período informado.")
  print("Digite 3 para ver apenas os dados de temperatura do período informado.")
  print("Digite 4 para ver apenas os dados de umidade e vento do período informado.")
  print("Digite 0 para terminar o programa.")
  print()

  op = int(input("Digite a seua escolha: "))
  print()
  if op == 0: # Finiçização do programa
    print("Fim do programa.")
    break

  while op > 4 or op < 0:
    print("Opção Inválida.")
    op = int(input("Digite novamente a sua escolha: "))

  data1 = input("Escreva a primeira data do intervalo (xx/xx/xxxx): ") # Verifica se a data digitada está dentro do intervalo do arquivo
  somaData1 = (int(data1.split('/')[2])*10000) + (int(data1.split('/')[1])*100) + (int(data1.split('/')[0]))
  while somaData1 < 19610100 or somaData1 > 20160711:
    data1 = input("Escreva a primeira data do intervalo (xx/xx/xxxx), somente datas entre 01/01/1961 e 10/07/2016 são aceitas: ")
    somaData1 = (int(data1.split('/')[2])*10000) + (int(data1.split('/')[1])*100) + (int(data1.split('/')[0]))

  data2 = input("Escreva a segunda data do intervalo (xx/xx/xxxx): ") # Verifica se a data digitada está dentro do intervalo do arquivo
  somaData2 = (int(data2.split('/')[2])*10000) + (int(data2.split('/')[1])*100) + (int(data2.split('/')[0]))
  while somaData2 < 19610100 or somaData2 > 20160711:
    data2 = input("Escreva a segunda data do intervalo (xx/xx/xxxx), somente datas entre 01/01/1961 e 10/07/2016 são aceitas: ")
    somaData2 = (int(data2.split('/')[2])*10000) + (int(data2.split('/')[1])*100) + (int(data2.split('/')[0]))

  print("Dia com maior precipitação: ", mesMaisChuvoso(separar(data1, data2)))

  if op == 1:
    todosDados(separar(data1, data2))
    print()

  elif op == 2:
    precipitacao(separar(data1, data2))
    print()

  elif op == 3:
    temperatura(separar(data1, data2))
    print()

  elif op == 4:
    umidadeVento(separar(data1, data2))

  else:
    print()
    print("Opção inválida.")
    print()
