a = open("test_corpus.txt", "r")
countHam = 0
countSpam = 0
for line in a:
  index = line.index('\t')
  newLine = line[index:].strip()
  typeL = line[:index].strip()
  if (typeL == "ham"):
   countHam += 1
  elif typeL == "spam":
   countSpam += 1

print countSpam
print countHam
print countHam*0.8
