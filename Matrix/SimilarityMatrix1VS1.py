from PubMed import PubMed
from openFile import openFile
from collections import OrderedDict
import csv
import time
import ast



class SimilarityMatrix1VS1():
    pri = OrderedDict()
    sec = OrderedDict()


    def __init__(self):
        self.PubMed = PubMed()
        self.openFile = openFile()

    def makeDicts(self):

        primary = self.openFile.getPrimary()
        secondary = self.openFile.getSecondary()

        totalLenPri = len(primary)
        counterPri = 0
        for p in primary:
            try:
                self.pri[p] = self.PubMed.searchPMID(p)
                counterPri +=1
                print str(counterPri)+"/"+str(totalLenPri)
            except:
                time.sleep(2)
                continue
        #self.savePrimaryDictionary()

        """
        totalLenSec = len(secondary)
        counterSec = 0
        for s in secondary:
            try:
                self.sec[s] = self.PubMed.searchPMID(s)
                counterSec +=1
                print str(counterSec)+"/"+str(totalLenSec)
            except:
                time.sleep(2)
                continue
        #self.saveSecondaryDictionary()

        #self.makeSimilarity()
        """
    def makeSimilarity(self):

        if bool(self.sec) != False:

            topList = []
            for key in self.sec:
                topList.append(key)
        else:
            topList = self.openFile.getSecondary()

        topList.insert(0,"")
        self.makeCSV(topList)

        print "Creating CSV"
        counter = 0
        for kpri,vpri in self.pri.items():
            line = []
            line.append(kpri)
            counter +=1
            print str(counter)+"/"+str(len(self.pri))
            for ksec, vsec in self.sec.items():
                set1 = set(vpri)
                set2 = set(vsec)
                match = set1&set2
                line.append(list(match))
            self.makeCSV(line)
        print "CSV created"

    def makeCSV(self, data):
        fileName = "Similarity_Matrix"
        fileName = fileName+".csv"
        w = csv.writer(open(fileName, "a"))
        w.writerow(data)

    def savePrimaryDictionary(self):
        f = open("primaryDictionary.txt", "a")
        for key, val in self.pri.items():
            f.write( str(key)+"\t"+str(val)+"\n")
        print "Saved Primary Dictionary"

    def saveSecondaryDictionary(self):
        f = open("secondaryDictionary.txt", "a")
        for key, val in self.sec.items():
            f.write( str(key)+"\t"+str(val)+"\n")
        print "Saved Secondary Dictionary"


    def createTest(self):
        f = open ("secondaryDictionary.txt", "r")
        f1 = open("secondaryDictionary_small.txt", "a+")
        counter = 0
        for line in f:
            counter +=1
            f1.write(line)
            if counter == 2:
                break
    def FileToDict(self):
        f = open("primaryDictionary.txt")
        for line in f:
            line = line.strip("\n").split("\t")
            self.pri[line[0]]= ast.literal_eval(line[1])


        f1 = open("secondaryDictionary.txt")
        for line1 in f1:
            line1 = line1.strip("\n").split("\t")
            self.sec[line1[0]]= ast.literal_eval(line1[1])

        print "Dictionaries are ready"




    def start(self):
        #self.makeDicts()
        #print self.pri
        #self.pri.clear()
        self.FileToDict()

        self.makeSimilarity()





def test_start():
    sim1VS1 = SimilarityMatrix1VS1()
    sim1VS1.start()

test_start()







