'''

'''

class readHist:
    def __init__(self, hist, is2D=False):
        self.hist       = hist
        self.name       = hist.GetName()
        self.x_title    = hist.GetXaxis().GetTitle()
        self.y_title    = hist.GetYaxis().GetTitle()
        self.x_axis     = self.hist.GetXaxis()
        self.y_axis     = self.hist.GetYaxis()
        if is2D: self.z_title    = hist.GetZaxis().GetTitle()

    def getBins(self, axis):
        return [ (axis.GetBinLowEdge(i+1), axis.GetBinUpEdge(i+1)) for i in range(axis.GetNbins()) ]

    def getContent(self):
        self.content = {}
        for i in range(self.x_axis.GetNbins()):
            for j in range(self.y_axis.GetNbins()):
                self.content[(i,j)] = self.hist.GetBinContent(i+1, j+1)

    def getTable(self):
        self.x_bins     = self.getBins(self.x_axis)
        self.y_bins     = self.getBins(self.y_axis)
        self.getContent()
