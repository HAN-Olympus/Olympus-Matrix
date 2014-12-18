"""
@name Matrix
@author Tom Linssen
@module SimilarityMatrix
@version 1.0.0
"""

from PubMed import PubMed
from openFile import openFile
import csv
import time



class SimilarityMatrix():
    """This module makes a similarity matrix from the primary and secondary file.
    The similarity by PMID's is created by a primary search term with another term from the secondary file.
    """


    def __init__(self):
        self.PubMed = PubMed()
        self.openFile = openFile()

    def makeSimilarityMatrix(self):
        """ Combines the terms from the primary and secondary file.
        Search PubMed

        :return: A CSV file from makeCSV()
        """
        getPrimary = self.openFile.getPrimary()
        getSecondary = self.openFile.getSecondary()

        topList = list(getSecondary)
        topList.insert(0,"")
        self.makeCSV(topList)
        tried = 0
        for p in getPrimary:
            sim = []
            print str(getPrimary.index(p))+"/"+str(len(getPrimary))
            sim.insert(0,p)
            for s in getSecondary:
                if " or " in s or " OR " in s:
                    query = p+" AND ("+s+")"
                else:
                    query =  str(p+" AND "+s)
                #print query
                try:
                    ids = self.PubMed.searchPMID(query)

                except:
                    try:
                        time.sleep(5)
                        continue
                    except:
                        time.sleep(60*5)
                        continue


                sim.append(str(ids).replace("'",""))
            self.makeCSV(sim)
        print "Sim matrix created"

    def makeCSV(self, data):
        fileName = "Similarity_Matrix"
        fileName = fileName+".csv"
        w = csv.writer(open(fileName, "a"))
        w.writerow(data)

    def specifyControls(self):
        pass

    def specifyInput(self):
        pass

    def specifyOutput(self):
        pass

    def start(self):
        self.makeSimilarityMatrix()

def test_start():
    pmo = SimilarityMatrix()
    pmo.start()


test_start()