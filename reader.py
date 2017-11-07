'''
Read an input root file, create an object containing a list of histograms
'''

import ROOT

types = ['TCanvas', 'TGraph', 'TH2D', 'TH2F', 'TH1D', 'TH1F']

class reader:
    def __init__(self, file):
        self.file = file
        self.graphs = []
        self.hist2D = []
        self.hist1D = []

    def open(self):
        self.rootFile = ROOT.TFile(self.file)

    def close(self):
        self.rootFile.Close()
        del self.rootFile

    def getObjects(self):
        ''' should be more elaborate. try - except?
        '''
        k = self.rootFile.GetListOfKeys()
        self.canvasList = [ self.rootFile.Get(a.GetName()) for a in k ]

    def getFromCanvas(self):
        for c in self.canvasList:
            objs = c.GetListOfPrimitives()
            self.getFromPrimitiveList(objs)

    def getFromPrimitiveList(self, objs)
        for o in objs:
            className = o.ClassName()
            if className == 'TGraph':
                self.graphs.append(o)
            elif className == 'TH2D' or className == 'TH2F':
                self.hist2D.append(o)
            elif className == 'TH1D' or className == 'TH1F':
                self.hist1D.append(o)
            elif className == 'TList' or className == 'TPad':
                pass 
            else:
                continue

    '''
    need iterative/recursive function that steps through all lists/pads until at the last layer
    '''
