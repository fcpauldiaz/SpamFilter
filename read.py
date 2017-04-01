file = open("test_corpus.txt", "r") 
cantLines = 5573
training = (int)(cantLines * 0.8)
cross_validation = (int)(cantLines * 0.10)
test = (int)(cantLines * 0.10)
count = 0
training_data = []
cross_validation_data = []
test_data = []


count_training = 0
total = training + cross_validation + test
cantType = (int)(training/2.0)

cantHam = 0
cantSpam = 0
remaining_data = []
inserterted = False
for line in file: 
  index = line.index('\t')
  newLine = line[index:].strip()
  typeL = line[:index].strip()
  if typeL == "ham":
    if (cantHam < 3860):
      training_data.append(line.strip())
      cantHam += 1
      count += 1
      inserterted = True
  elif typeL == "spam":
    if (cantSpam < 597):
      training_data.append(line.strip())
      cantSpam += 1
      count += 1
      inserterted = True
  if (inserterted == False):
    remaining_data.append(line.strip())
  inserterted = False

cantHam = 0
cantSpam = 0
remaining_data2 = []
inserterted = False
for line in remaining_data: 
  index = line.index('\t')
  newLine = line[index:].strip()
  typeL = line[:index].strip()
  if typeL == "ham":
    if (cantHam < 483):
      cross_validation_data.append(line.strip())
      cantHam += 1
      count += 1
      inserterted = True
  elif typeL == "spam":
    if (cantSpam < 75):
      cross_validation_data.append(line.strip())
      cantSpam += 1
      count += 1
      inserterted = True
  if (inserterted == False):
    remaining_data2.append(line.strip())
  inserterted = False

cantHam = 0
cantSpam = 0
inserterted = False
for line in remaining_data2: 
  index = line.index('\t')
  newLine = line[index:].strip()
  typeL = line[:index].strip()
  if typeL == "ham":
    if (cantHam < 483):
      test_data.append(line.strip())
      cantHam += 1
      count += 1
  elif typeL == "spam":
    if (cantSpam < 75):
      test_data.append(line.strip())
      cantSpam += 1
      count += 1
 
print len(training_data) + len(cross_validation_data) + len(test_data)

print len(cross_validation_data)
# print count, "total"
# countHam = 0
# countSpam = 0
# for line in training_data:
#   index = line.index('\t')
#   newLine = line[index:].strip()
#   typeL = line[:index].strip()
#   if typeL == "ham":
#       countHam += 1
#   elif typeL == "spam":
#     countSpam += 1

# print countHam, countSpam
# print 2229+747
# print (cantHam*0.1), (cantSpam*0.1)
#training ham = 3860, spam=597
#cross_evaluation ham = 483, spam = 75
#test ham = 483, spam = 75
#86.60% es HAM y esl 13.4 % es SPAM
#
#Expectation Maximization
#Un universo/modelo que maximice la probabilidad de una observacion
#Es un algoritmo no supervisado

#Modelo mixto gaussiano
#Encontrar varios gaussianos. Combinar los gaussianos
#Se convierte en uno
#La integral es 1.
#Distribucion probabilistica
#Entre mas alta la ponderacion mas se parece al gaussiano
#