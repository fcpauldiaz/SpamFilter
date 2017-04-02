class DataClassifier:

  def __init__(self, name):
    self.countHam = 0
    self.countSpam = 0
    self.data = []
    for line in open(name, "r"): 
      index = line.index('\t')
      typeL = line[:index].strip()
      if (typeL == "ham"):
       self.countHam += 1
      elif typeL == "spam":
       self.countSpam += 1
      self.data.append(line)


  def separateData(self, process_data, percentage):
    remaining_data = []
    preClassifiedData = []
    inserterted = False
    cantHam = 0
    cantSpam = 0
    for line in process_data: 
      index = line.index('\t')
      typeL = line[:index]
      if typeL == "ham":
        if (cantHam < (int)(round(self.countHam*percentage))):
          preClassifiedData.append(line)
          cantHam += 1
          inserterted = True
      elif typeL == "spam":
        if (cantSpam < (int)(round(self.countSpam*percentage))):
          preClassifiedData.append(line)
          cantSpam += 1
          inserterted = True
      if (inserterted == False):
        remaining_data.append(line)
      inserterted = False
    return preClassifiedData, remaining_data

  def getData(self, classifyData, p1, p2, p3):
    training_data, rem_data = classifyData(classifier.data, p1)
    cross_validation, rem_data = classifyData(rem_data, p2)
    test_data, rem_data = classifyData(rem_data, p3)
    return training_data, cross_validation, test_data


classifier = DataClassifier("test_corpus.txt")
training, cross, test = classifier.getData(classifier.separateData, 0.8, 0.1, 0.1)
#print rem_data
print len(training) + len(cross) + len(test) 
