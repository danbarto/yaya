'''
Read an input root file, create an object containing a list of histograms
'''

import ROOT

types = ['TCanvas', 'TGraph', 'TH2D', 'TH2F', 'TH1D', 'TH1F']

class rootReader:
    def __init__(self, file):
        self.file = file
        self.graphs     = []
        self.hist2D     = []
        self.hist1D     = []
        self.canvasList = []
        self.boxes      = []
        self.errors     = []

        self.walk()

    def open(self):
        self.rootFile = ROOT.TFile(self.file)

    def close(self):
        self.rootFile.Close()
        del self.rootFile

    def getObjects(self):
        ''' should be more elaborate. try - except?
        '''
        k = self.rootFile.GetListOfKeys()
        return [ self.rootFile.Get(a.GetName()) for a in k ]
        #self.canvasList += [ self.rootFile.Get(a.GetName()) for a in k ]

    def getFromCanvas(self, canvasList):
        self.canvasList += canvasList
        for c in canvasList:
            objs = c.GetListOfPrimitives()
            self.getFromPrimitiveList(objs)

    def getFromPrimitiveList(self, objs):
        for o in objs:
            className = o.ClassName()
            if className == 'TGraph':
                self.graphs.append(o)
            elif className == 'TH2D' or className == 'TH2F':
                self.hist2D.append(o)
            elif className == 'TH1D' or className == 'TH1F':
                self.hist1D.append(o)
            elif className == 'TBox':
                self.boxes.append(o)
            elif className == 'TGraphAsymmErrors':
                self.errors.append(o)
            elif className == 'TList':
                self.getFromPrimitiveList(o)
            elif className == 'TPad':
                self.getFromCanvas([o])
            else:
                continue

    def walk(self):
        print "\nOpening file %s"%self.file
        self.open()
        print "Searching for ROOT objects in file."
        firstCanvas = self.getObjects()
        self.getFromCanvas(firstCanvas)
        self.close()
        print "Done."

        for className in ["graphs", "hist2D", "hist1D", "boxes", "errors"]:
            collection = getattr(self, className)
            if len(collection)>0:
                print "\nFound the %s members of class %s:"%(len(collection),className)
                for c in collection:
                    print c.GetName()
