'''

'''

class read1DHist:
    def __init__(self, hist, is2D=False):
        self.hist       = hist
        self.name       = hist.GetName()
        self.x_title    = hist.GetXaxis().GetTitle()
        self.y_title    = hist.GetYaxis().GetTitle()
        self.x_axis     = self.hist.GetXaxis()
        self.y_axis     = self.hist.GetYaxis()
        self.errors     = False
        if is2D: self.z_title    = hist.GetZaxis().GetTitle()

    def getBins(self, axis):
        return [ (axis.GetBinLowEdge(i+1), axis.GetBinUpEdge(i+1)) for i in range(axis.GetNbins()) ]

    def getContent(self):
        self.content = []
        for i in range(self.x_axis.GetNbins()):
            self.content.append(self.hist.GetBinContent(i+1))
            #for j in range(self.y_axis.GetNbins()):
            #    self.content[(i,j)] = self.hist.GetBinContent(i+1, j+1)

    def getIndependent(self, name="placeholder", units="GeV"):
        s = '\nindependent_variables:\n- header: {name: %s, units: %s}\n  values:'%(name, units)
        for x in self.x_bins:
            #print x
            s += "\n  {low: %s, high: %s}"%x
        print s

    def getDependent(self, name="process", units="1"):
        s = '- header: {name: %s, units: %s}\n  values:'%(name, units)
        for i,y in enumerate(self.content):#sorted(self.content.keys()):
            s += '\n  - value: %s'%y
            if self.errors:
                s += '\n    errors:'
                if type(self.errors[i]) == type(1.):
                    s += '\n    - {symerror: %s, label: total}'%self.errors[i]
                else:
                    s += '\n    - {asymerror: {plus: %s, minus: -%s}, label: total}'%self.errors[i]
        print s

    def getTable(self):
        self.x_bins     = self.getBins(self.x_axis)
        #self.y_bins     = self.getBins(self.y_axis)
        self.getContent()

    def mergeBoxes(self, listOfBoxes):
        self.errors = []
        if len(listOfBoxes) == len(self.x_bins):
            for i,b in enumerate(listOfBoxes):
                low, high = b.GetY1(), b.GetY2()
                #print low, high
                #print low
                #print low>high
                #low, high = (b.GetY1(), b.GetY2() if b.GetY1() > b.GetY2() else b.GetY2(), b.GetY1())
                low, high = abs(self.content[i] - low), abs(self.content[i]- high)
                low = low*1.2
                symmetric = False
                if (low-high)/low < 0.01: symmetric = True
                if symmetric:
                    self.errors.append(low)
                else:
                    self.errors.append((high,low))
        else:
            raise("NotImplementedError", "Number of boxes is different from number of bins!")
