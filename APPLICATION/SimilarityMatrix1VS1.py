"""
@name Matrix
@author Tom Linssen
@module SimilarityMatrix1VS1
@version 1.0.0

"""

from PubMed import PubMed

from collections import OrderedDict
import csv
import time
import ast

class SimilarityMatrix1VS1():
    pri = OrderedDict()
    sec = OrderedDict()


    def __init__(self):
        self.PubMed = PubMed()

    def makeDicts(self, primary, secondary):
        #makes dictionaries
        totalLenPri = len(primary)
        counterPri = 0
        print "searching Primary List"
        for p in primary:
            try:
                self.pri[p] = self.PubMed.searchPMID(p)
                counterPri +=1
                print str(counterPri)+"/"+str(totalLenPri)
            except:
                time.sleep(2)
                continue
        #self.savePrimaryDictionary()


        totalLenSec = len(secondary)
        counterSec = 0
        print "searching secondary List"
        for s in secondary:
            try:
                self.sec[s] = self.PubMed.searchPMID(s)
                counterSec +=1
                print str(counterSec)+"/"+str(totalLenSec)
            except:
                time.sleep(2)
                continue
        #self.saveSecondaryDictionary()

        bool = self.makeSimilarity()
        return bool


    def makeSimilarity(self):
        # makes similarity
        if bool(self.sec) != False:

            topList = []
            for key in self.sec:
                topList.append(key)
        else:
            #topList = self.openFile.getSecondary()
            print "error"

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
        return True

    def makeCSV(self, data):
        #makes CSV file
        fileName = "Similarity_Matrix"
        fileName = fileName+".csv"
        w = csv.writer(open(fileName, "a"))
        w.writerow(data)

    def savePrimaryDictionary(self):
        #Saving primary dictionary to free memory
        f = open("primaryDictionary.txt", "a")
        for key, val in self.pri.items():
            f.write( str(key)+"\t"+str(val)+"\n")
        print "Saved Primary Dictionary"

    def saveSecondaryDictionary(self):
        #Saving secondary dictionary to free memory
        f = open("secondaryDictionary.txt", "a")
        for key, val in self.sec.items():
            f.write( str(key)+"\t"+str(val)+"\n")
        print "Saved Secondary Dictionary"


    def FileToDict(self):
        # used for saving the dictionary if it became too big
        fileNameP = "Dict-genes-Celegans.txt"
        f = open(fileNameP)
        for line in f:
            line = line.strip("\n").split("\t")
            self.pri[line[0]]= ast.literal_eval(line[1])

        fileNameS = "Dict-Developmental- Biology.txt"
        f1 = open(fileNameS)
        for line1 in f1:
            line1 = line1.strip("\n").split("\t")
            self.sec[line1[0]]= ast.literal_eval(line1[1])

        print "Dictionaries are ready"











