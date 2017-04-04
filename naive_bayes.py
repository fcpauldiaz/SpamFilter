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
  def getMessage(self, message):
    try:
      index = message.index('\t')
    except:
      index = 0
    typeL = message[:index]
    msg = message[index:]
    msg = msg.split(" ")
    return msg, typeL
  #P(M|SPAM)
  def probMessage(self, word, type, data, processMessage):
    count = 0
    totalType = 0
    for message in data:
      msg, typeL = processMessage(message)
      for wrd in msg:     
        if (wrd == word and type == typeL):
          count += 1
        if (type == typeL):
          totalType += 1
    return float(count + self.k)/float(totalType + self.k*self.diff)

  def getDifferent(self):
    diff = []
    for message in self.data:
      try :
        index = message.index('\t')
      except:
        index = 0
      msg = message[index:].strip()
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
  # P(M|SPAM)*P(SPAM)/P(M|SPAM)*P(SPAM) + P(M|HAM)*P(HAM)
  def calcProb(self, data, processMessage, validate=True):
    success = 0
    total = 0
    if (validate == False):
      f = open('output.txt','w')
    for message in data:
    
      msg, typeL = processMessage(message)
      probsSpam = []
      probHam = []
      for word in msg:
        if (word != ''):
          p1 = self.probMessage(word, "spam", self.data, processMessage)
          probsSpam.append(p1)
          p2 = self.probMessage(word, "ham", self.data, processMessage)
          probHam.append(p2)
      #return self.priorHam
      a = reduce(lambda x, y: x*y, probsSpam)
      b = reduce(lambda x, y: x*y, probHam)
      
      if (a != 0 and b != 0):
        prob =  (a*self.priorSpam)/ float(a*self.priorSpam + b*self.priorHam)
        #print prob
        #si es spam
        if (typeL == "spam" or validate == False):
          if (prob >= self.threshold):
            success += 1
            if (validate == False):
                f.write('spam' + '\t' + message + '\n')
          total += 1 
          if (prob < self.threshold):
            if (validate == False):
              f.write('ham' + '\t' + message + '\n')
    if (validate == True):
      return float(success)/float(total)

classifier = DataClassifier("test_corpus2.txt")
training, cross, test = classifier.getData(classifier.separateData, 0.8, 0.1, 0.1)
#print rem_data
#print len(training)
data = cross
naive = NaiveBayes(training[0]+cross[0]+test[0], 1, 0.5)
#words = [line.strip() for line in open("stop_words.txt", 'r')]
naive.getDifferent()
print naive.diff
naive.prior(classifier.countHam, classifier.countSpam)
data = classifier.parseArray([line.strip() for line in open("input.txt", 'r')])
print "rendimiento " + str(naive.calcProb(data, naive.getMessage, False))
