"""
@name Matrix
@author Tom Linssen
@module openFile
@version 1.0.0
"""

class openFile():
    """ This module opens two files and makes a list of the terms"""
    def getPrimary(self):
        """ Get the primary terms

        :return: A list of the primary terms
        """

        fileName = "Corbion_compounds.txt"
        primary = self.openFile(fileName)
        return primary

    def getSecondary(self):
        """ Get the secondary terms

        :return: A list of the secondary terms
        """
        fileName = "Corbion_terms.txt"
        secondary = self.openFile(fileName)
        return secondary

    def openFile(self, fileName):
        """Get a list of terms from the file

        :param fileName: A string with the file name
        :return:A list of the terms read from the file
        """
        list = []
        file = open(fileName, "r")
        for line in file:
            line = line.strip("\n")
            line = line.strip("\t").replace("\t"," ")
            if line is not "":
                list.append(line)
        return list

    def specifyControls(self):
        pass

    def specifyInput(self):
        pass

    def specifyOutput(self):
        pass