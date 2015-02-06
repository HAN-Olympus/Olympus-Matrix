"""
@name
@author Tom Linssen
@module TkinterGUI
@version 1.0.0
"""


from Tkinter import *
import tkMessageBox
from SimilarityMatrix1VS1 import SimilarityMatrix1VS1
from BinaryMatrix import BinaryMatrix

class Example(Frame):
  
    def __init__(self, parent):
        Frame.__init__(self, parent, background="white")
        self.SimilarityMatrix1VS1 = SimilarityMatrix1VS1()
        self.BinaryMatrix = BinaryMatrix()
        self.parent = parent
        self.parent.title("CRACKeLITe MATRIX")
        self.pack(fill=BOTH, expand=1)
        self.centerWindow()
        self.messageWindow()
        
    def centerWindow(self):
        # Center the window/ GUI in the middle of the screen
        w = 530
        h = 450
        sw = self.parent.winfo_screenwidth()
        sh = self.parent.winfo_screenheight()
        x = (sw - w)/2
        y = (sh - h)/2
        self.parent.geometry('%dx%d+%d+%d' % (w, h, x, y))
        
    def messageWindow(self):
        # Adding and placing buttons and text fields.
        textP = Text(self)
        self.textP = textP
        self.textP.insert(INSERT, "mating\nScoliosis\nrectum\n1-bromopropane OR n-propyl bromide")
        textS = Text (self)
        self.textS = textS
        self.textS.insert(INSERT, "elegans\ndecene\noxazolidine")
        self.textS.configure(background='grey')
        self.textP.configure(background='grey')
        self.textP.pack()
        self.textP.place(x=10,y=10, height=390, width=250)
        self.textS.place(x=270,y=10, height=390, width=250)
        runSIMButton = Button(self, text="Create Similarity Matrix", command = lambda: self.makeSimilarity())
        runBINButton = Button(self, text="Create Binary Matrix", command= lambda: self.makeBinary())
        runSIMButton.place(bordermode= INSIDE, x = 10, y =405)
        runBINButton.place(bordermode= INSIDE, x = 185, y =405)
   
    def getText(self):
        # Retrieve text from text fields
        Primary =  self.textP.get("1.0","100.0")
        Secundary = self.textS.get("1.0","100.0")
        Plist = str(Primary).split("\n")
        Slist = str(Secundary).split("\n")
        self. primaryList = Plist [:-1]
        self.secondaryList = Slist [:-1]
        self.givePopUpStart()


    def makeSimilarity(self):
        # Connecting to similarityMatrix1VS1.py
        self.getText()
        SIMREADY = self.SimilarityMatrix1VS1.makeDicts(self.primaryList, self.secondaryList)
        if SIMREADY == True:
            self.givePopUpFinished("similarity")

    def makeBinary(self):
        # Connecting to binaryMatrix.py
        self.getText()
        BINREADY = self.BinaryMatrix.makeBinaryMatrix(self.primaryList, self.secondaryList)
        if BINREADY == True:
            self.givePopUpFinished("binary")

    def givePopUpStart(self):
        #Popup when script is executing
        tkMessageBox.showinfo("Patience", "This could take a while")
    def givePopUpFinished(self, matrixType):
        #Popup when script is ready
        tkMessageBox.showinfo("READY", "The "+str(matrixType)+" matrix is created in the current folder")

def main():
    #defines the root
    root = Tk()
    app = Example(root)
    root.mainloop()


if __name__ == '__main__':
    main()
