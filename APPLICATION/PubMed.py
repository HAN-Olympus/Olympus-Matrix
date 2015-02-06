"""
@name Matrix
@author Tom Linssen
@module PubMed
@version 1.0.0
"""
from Bio import Entrez

class PubMed():
    """ This module allows for retrieval of medical articles ID's from the Entrez API"""
    def __init__(self):
        Entrez.email = "olympus@gmail.com"
        #limit = 10**6
        #self.limit = limit

    def searchPMID(self,query):
        """ Get pudmed ids by a search term.

        :param query: A search term, constructed by BinaryMatrix.py or SimilarityMatrix.py
        :return: A list of PMID's, default to 10^6
        """
        handle = Entrez.esearch(db="pubmed", term = query, retmax = 10**6)
        record = Entrez.read(handle)
        idlist = record["IdList"]
        return idlist

    def specifyControls(self):
        controls = {
            #"searchterm" : Text("searchterm", value="", label="Search term"),
            #"limit" : Integer("limit", value=0, label="Limit")
        }
        return controls

    def specifyInput(self):
        return None

    def specifyOutput(self):
        pass
        #articleCollection = Collection(Article)
        #log = Log()
        #output = {
        #    "errors":[log],
        #    "result":[articleCollection]
        #}
        #return output


