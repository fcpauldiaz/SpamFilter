from numpy import unique
from read import DataClassifier
class NaiveBayes:
  def __init__(self, data, kSmooth, th):
    self.data = data
    self.k = kSmooth
    self.priorSpam = 0
    self.priorHam = 0
    self.diff = 0
    self.threshold = th
  #P(M|SPAM)
  def probMessage(self, word, type, data):
    count = 0
    totalType = 0
    for message in data:
      index = message.index('\t')
      typeL = message[:index]
      msg = message[index:]
      msg = msg.split(" ")
      for wrd in msg:      
        if (wrd == word and type == typeL):
          count += 1
        if (type == typeL):
          totalType += 1

    return float(count + self.k)/float(totalType + self.k*self.diff)

  def getDifferent(self):
    diff = []
    for message in self.data:
      index = message.index('\t')
      msg = message[index:].strip()
      msg = msg.replace(".", " ")
      msg = msg.replace("!", " ")
      msg = msg.replace("?", " ")
      msg = msg.replace("*", " ")
      msg = msg.replace("-", " ")
      msg = msg.replace(":", " ")
      msg = msg.replace(";", " ")
      msg = msg.split(" ")
      for wrd in msg:      
        diff.append(wrd)
    self.diff =  len(unique(diff))

  def setData(self, data):
    self.data = data
  #P(M|HAM)
  def messageHam(self, word):
    return
  def prior(self, countHam, countSpam):
    self.priorSpam = float(countSpam + self.k)/float((countSpam+countHam) + self.k*2)
    self.priorHam = float(countHam + self.k)/float((countSpam+countHam) + self.k*2)
  #P(M|SPAM)*P(SPAM)/P(M|SPAM)*P(SPAM) + P(M|HAM)*P(HAM)
  def calcProb(self, data):
    success = 0
    total = 0
    for message in data:
      index = message.index('\t')
      typeL = message[:index]
      msg = message[index:]
      #print typeL
      msg = msg.split(" ")
      probsSpam = []
      probHam = []
      for word in msg:
        p1 = self.probMessage(word, "spam", data)
        probsSpam.append(p1)
        p2 = self.probMessage(word, "ham", data)
        probHam.append(p2)
      #return self.priorHam
      a = reduce(lambda x, y: x*y, probsSpam)
      b = reduce(lambda x, y: x*y, probHam)
      
      if (a != 0 and b != 0):
        prob =  (a*self.priorSpam)/ float(a*self.priorSpam + b*self.priorHam)
        #si es spam
        if (typeL == "spam"):
          if (prob > self.threshold):
            success += 1
          total += 1
      
    return float(success)/float(total)

classifier = DataClassifier("test_corpus2.txt")
training, cross, test = classifier.getData(classifier.separateData, 0.8, 0.1, 0.1)
#print rem_data
#print len(training)
naive = NaiveBayes(training, 1, 0.8)
naive.getDifferent()
naive.prior(classifier.countHam, classifier.countSpam)
print "rendimiento " + str(naive.calcProb(cross))
