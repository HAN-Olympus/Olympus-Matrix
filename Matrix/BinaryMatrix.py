"""
@name Matrix
@author Tom Linssen
@module BinaryMatrix
@version 1.0.0
"""

from collections import OrderedDict
from PubMed import PubMed
from openFile import openFile
import csv

class BinaryMatrix():
    """ This module This module makes a binary matrix from the primary and secondary file.
    The similar PMID's are opposite to the terms from the primary and secondary file.
    """
    bin = OrderedDict()

    def __init__(self):
        self.PubMed = PubMed()
        self.openFile = openFile()

    def makeBinaryMatrix(self):
        """ Combines the terms from the primary and secondary file.
        Search PubMed

        :return:A CSV file from makeCSV()
        """
        getPrimary = self.openFile.getPrimary()
        getSecondary = self.openFile.getSecondary()
        totalLen =len(getPrimary)*len(getSecondary)
        counterTime = 0
        counterPrimary = 0
        topList = getPrimary+getSecondary
        for p in getPrimary:
            print str(getPrimary.index(p))+"/"+str(len(getPrimary))
            for s in getSecondary:
                if " or " in s or " OR " in s:
                    query = p+" AND ("+s+")"
                else:
                    query =  str(p+" AND "+s)
                #print query

                ids = self.PubMed.searchPMID(query)
                #print ids
                for id in ids:
                    self.makeBinTable(counterPrimary,s,id,topList)
                counterTime +=1
                #perc = (((counterTime)/(totalLen))*100)
                #print perc

            counterPrimary+=1

        self.splitCSV(topList)

    def makeBinTable(self,primaryIndex, term, id, topList):
        """

        :param primaryIndex: A int index of the primary term list
        :param term: 
        :param id: A single PubMed id
        :param topList: A list at the top of the CSV file,with primary and secondary terms
        :return:
        """
        zeroList = []
        for i in range(len(topList)):
            zeroList.append(0)
        indexPrimary = primaryIndex
        indexTerm = topList.index(term)
        if id in self.bin.keys():
            zeroList = self.bin[id]
            zeroList[indexPrimary]= 1
            zeroList[indexTerm]= 1
            self.bin[id]= zeroList
        else:
            zeroList[indexPrimary]= 1
            zeroList[indexTerm]= 1
            self.bin[id] = zeroList

    def makeCSV(self,file_name, data, topList):
        """ Writes data to make a CSV file

        :param file_name: A string of the name of the CSV file
        :param data: A dictionary of the data (binary matrix containing 0's and 1's)
        :param topList: A list at the top of the CSV file, with primary and secondary terms and first an empty cell for layout
        :return: A CSV file
        """
        file_name = file_name+".csv"
        w = csv.writer(open(file_name, "w"))
        w.writerow(topList)
        for key, val in data.items():
            row = list(val)
            row.insert(0,key)
            w.writerow(row)

    def splitCSV(self, topList):
        """ Split the OrderDict in chunks of 45000 to write it in a CSV file

        :param topList: A list at the top of the CSV file, with the secondary terms and first an empty cell for layout
        :return: A OrderDict split in chunks of 45000
        """

        maxKeys = 45000
        fileCounter = 0
        topList.insert(0,"")
        print len(self.bin)
        for i in range (0,len(self.bin.keys()), maxKeys):
            fileCounter +=1
            fileName = "CRACKeLITe"
            #fileName = "Corbion"
            fileNameList = "%s_Binary_Matrix_%i" % (fileName,fileCounter)
            dic = OrderedDict(self.bin.items()[i:i+maxKeys])
            self.makeCSV(fileNameList, dic, topList)
            print "CSV %i created" % fileCounter
        print "All CSVs created"



    def specifyControls(self):
        pass

    def specifyInput(self):
        pass

    def specifyOutput(self):
        pass

    def start(self):
        self.makeBinaryMatrix()


def test_start():
    pmo = BinaryMatrix()
    pmo.start()
test_start()