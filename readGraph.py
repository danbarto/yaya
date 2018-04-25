'''
Class for reading root TGraphs
'''
import ROOT


class readGraph:
    def __init__(self, hist, is2D=False):
        self.hist       = hist
        self.name       = hist.GetName()
        self.nPoints    = hist.GetN()

        self.getTable()

    def getBins(self, axis):
        return [ (round(axis.GetBinLowEdge(i+1),2), round(axis.GetBinUpEdge(i+1),2)) for i in range(axis.GetNbins()) ]

    def getContent(self):
        self.content = []
        for i in range(self.nPoints):
            x = ROOT.Double()
            y = ROOT.Double()
            self.hist.GetPoint(i, x, y)
            self.content.append((x,y))

    def getIndependent(self, name="placeholder", units="GeV", start_x = 0, start_y = 0):
        s = '\nindependent_variables:\n- header: {name: %s, units: %s}\n  values:'%(name, units)
        for p in self.content:
            if p[0]>0 and p[1]>0:
                s += "\n  - value: %.1f"%p[0]
        print s


    def getDependent(self, name=False, units="count", start_x = 0, start_y = 0):
        name = name if name else self.name
        s = '- header: {name: %s, units: %s}\n  values:'%(name, units)
        for p in self.content:
            if p[0]>0 and p[1]>0:
                s += "\n  - value: %.1f"%p[1]
        print s

    def getTable(self):
        self.getContent()

