"""
@name Matrix
@author Tom Linssen
@module SimilarityMatrix
@version 1.0.0
"""

from collections import OrderedDict
from PubMed import PubMed
from openFile import openFile
import csv


class SimilarityMatrix():
    """This module makes a similarity matrix from the primary and secondary file.
    The similarity by PMID's is created by a primary search term with another term from the secondary file.
    """
    sim = OrderedDict()

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
        for p in getPrimary[0]:
            print p
            sim = []
            for s in getSecondary:
                query =  str(p+" AND "+s)
                ids = self.PubMed.searchPMID(query)
                sim.append(str(ids).replace("'",""))
            self.sim[p]=sim
        topList = getSecondary
        topList.insert(0,"")
        self.makeCSV("sim",self.sim,topList)
        print "Sim matrix created"

    def makeCSV(self,file_name, data, topList):
        """ Writes data to make a CSV file

        :param file_name: A string of the name of the CSV file
        :param data: A dictionary of the data (similarity PMID's)
        :param topList: A list at the top of the CSV file, with the secondary terms and first an empty cell for layout
        :return: A CSV file
        """
        file_name = file_name+".csv"
        w = csv.writer(open(file_name, "w"))
        w.writerow(topList)
        for key, val in data.items():
            row = list(val)
            row.insert(0,key)
            w.writerow(row)

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


#test_start()