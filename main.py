choice = int(input("Digite 1, 2 ou 3 para escolher a entrada de conjuntos: "))
if choice == 1:
  arq = open("arqtexto.txt", 'r')
if choice == 2:
  arq = open("arqtexto2.txt", 'r')
if choice == 3:
  arq = open("arqtexto3.txt", 'r')
operation = int(arq.readline(1))
counter = 0
def Union(con1, con2):
  counter1 = con1
  counter2 = con2
  print("Conjunto 1 {", ','.join(map(str, counter1)), "}, ", end='', sep="")
  print("Conjunto 2 {", ','.join(map(str, counter2)), "}.", end=' ', sep="")
  result = counter1 + counter2
  for line in counter1:
    for line2 in counter2:
      if line == line2:
        result.remove(line)
  print('Resultado: {', ','.join(map(str, result)), '}', sep="")
def Intersection(con1, con2):
  counter1 = con1
  counter2 = con2
  print("Conjunto 1 {", ','.join(map(str, counter1)), "}, ", end='', sep="")
  print("Conjunto 2 {", ','.join(map(str, counter2)), "}.", end=' ', sep="")
  for line in counter1:
    for line2 in counter2:
      if line == line2:
        result.append(line)
  print('Resultado: {', ','.join(map(str, result)), '}', sep="")
def Difference(con1, con2):
  counter1 = con1
  counter2 = con2
  print("Conjunto 1 {", ','.join(map(str, counter1)), "}, ", end='', sep="")
  print("Conjunto 2 {", ','.join(map(str, counter2)), "}.", end=' ', sep="")
  for line in counter1:
    if line not in counter2:
      result.append(line)
  print('Resultado: {', ','.join(map(str, result)), '}', sep="")
def Cartesian(con1, con2):
  counter1 = con1
  counter2 = con2
  print("Conjunto 1 {", ','.join(map(str, counter1)), "}, ", end='', sep="")
  print("Conjunto 2 {", ','.join(map(str, counter2)), "}.", end=' ', sep="")
  print("Resultado: {", end='')
  for line in con1:
    for line2 in con2:
      print('(', line, ',', sep="", end='')
      print(line2, '),', sep="", end='')
  print('}')
while counter < operation:
  for line in arq:
