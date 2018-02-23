'''

'''

class read2DHist:
    def __init__(self, hist, is2D=False):
        self.hist       = hist
        self.name       = hist.GetName()
        self.x_title    = hist.GetXaxis().GetTitle()
        self.y_title    = hist.GetYaxis().GetTitle()
        self.x_axis     = self.hist.GetXaxis()
        self.y_axis     = self.hist.GetYaxis()
        self.errors     = False
        if is2D: self.z_title    = hist.GetZaxis().GetTitle()

        self.getTable()

    def getBins(self, axis):
        return [ (round(axis.GetBinLowEdge(i+1),2), round(axis.GetBinUpEdge(i+1),2)) for i in range(axis.GetNbins()) ]

    def getContent(self):
        self.content = {}
        for i in range(self.x_axis.GetNbins()):
            #self.content.append(self.hist.GetBinContent(i+1))
            for j in range(self.y_axis.GetNbins()):
                self.content[(i,j)] = self.hist.GetBinContent(i+1, j+1)

    def getIndependent(self, name="placeholder", units="GeV", start_x = 0, start_y = 0, stop_x = 0, stop_y = 0):
        s = '\nindependent_variables:\n- header: {name: %s, units: %s}\n  values:'%(name, units)
        for i, x in enumerate(self.x_bins):
            for j, y in enumerate(self.y_bins):
                if i >= start_x and j >= start_y and i < len(self.x_bins)-stop_x and j < len(self.y_bins)-stop_y and self.content[(i,j)] > 0  and self.content[(i,j)] < 1000:
                    s += "\n  - value: %.2f"%x[1]
        print s
        s = '\nindependent_variables:\n- header: {name: %s, units: %s}\n  values:'%(name, units)
        for i, x in enumerate(self.x_bins):
            for j, y in enumerate(self.y_bins):
                if i >= start_x and j >= start_y and i < len(self.x_bins)-stop_x and j < len(self.y_bins)-stop_y and self.content[(i,j)] > 0  and self.content[(i,j)] < 1000:
                    s += "\n  - value: %.2f"%y[1]
        print s


    def getDependent(self, name=False, units="count", start_x = 0, start_y = 0, stop_x = 0, stop_y = 0):
        name = name if name else self.name
        s = '- header: {name: %s, units: %s}\n  values:'%(name, units)
        for x in range(start_x, len(self.x_bins)-stop_x):
            for y in range(start_y, len(self.y_bins)-stop_y):
                if self.content[(x,y)] > 0 and self.content[(x,y)] < 1000:
                    s += '\n  - value: %.4f'%self.content[(x,y)]
        print s

    def getTable(self):
        self.x_bins     = self.getBins(self.x_axis)
        self.y_bins     = self.getBins(self.y_axis)
        self.getContent()

