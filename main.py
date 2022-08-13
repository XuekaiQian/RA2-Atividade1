choice = int(input("Digite 1, 2 ou 3 para escolher a entrada de conjuntos: "))
if choice == 1:
  arq = open("arqtexto.txt", 'r')
if choice == 2:
  arq = open("arqtexto2.txt", 'r')
if choice == 3:
  arq = open("arqtexto3.txt", 'r')
operation = int(arq.readline(1))
counter = 0
def Union(cou1, cou2):
  counter1 = cou1
  counter2 = cou2
  print("Conjunto 1 {", ','.join(map(str, counter1)), "}, ", end='', sep="")
  print("Conjunto 2 {", ','.join(map(str, counter2)), "}.", end=' ', sep="")
  result = counter1 + counter2
  for line in counter1:
    for line2 in counter2:
      if line == line2:
        result.remove(line)
  print('Resultado: {', ','.join(map(str, result)), '}', sep="")
def Intersection(cou1, cou2):
  counter1 = cou1
  counter2 = cou2
  print("Conjunto 1 {", ','.join(map(str, counter1)), "}, ", end='', sep="")
  print("Conjunto 2 {", ','.join(map(str, counter2)), "}.", end=' ', sep="")
  for line in counter1:
    for line2 in counter2:
      if line == line2:
        result.append(line)
  print('Resultado: {', ','.join(map(str, result)), '}', sep="")
def Difference(cou1, cou2):
  counter1 = cou1
  counter2 = cou2
  print("Conjunto 1 {", ','.join(map(str, counter1)), "}, ", end='', sep="")
  print("Conjunto 2 {", ','.join(map(str, counter2)), "}.", end=' ', sep="")
  for line in counter1:
    if line not in counter2:
      result.append(line)
  print('Resultado: {', ','.join(map(str, result)), '}', sep="")
def Cartesian(cou1, cou2):
  counter1 = cou1
  counter2 = cou2
  print("Conjunto 1 {", ','.join(map(str, counter1)), "}, ", end='', sep="")
  print("Conjunto 2 {", ','.join(map(str, counter2)), "}.", end=' ', sep="")
  print("Resultado: {", end='')
  for line in counter1:
    for line2 in counter2:
      print('(', line, ',', sep="", end='')
      print(line2, '),', sep="", end='')
  print('}')
while counter < operation:
  for line in arq:
    counter1 = []
    counter2 = []
    result = []
    if line.startswith("U"):
      print('União: ', end='')
      cou1 = arq.readline().replace(',', '').split()
      cou2 = arq.readline().replace(',', '').split()
      Union(cou1, cou2)
      counter += 1
    if line.startswith("I"):
      print('Interseção: ', end='')
      cou1 = arq.readline().replace(',', '').split()
      cou2 = arq.readline().replace(',', '').split()
      Intersection(cou1, cou2)
      counter += 1
    if line.startswith("D"):
      print('Diferença: ', end='')
      cou1 = arq.readline().replace(',', '').split()
      cou2 = arq.readline().replace(',', '').split()
      Difference(cou1, cou2)
      counter += 1
    if line.startswith("C"):
      print('Cartesiano: ', end='')
      cou1 = arq.readline().replace(',', '').split()
      cou2 = arq.readline().replace(',', '').split()
      Cartesian(cou1, cou2)
      counter += 1
