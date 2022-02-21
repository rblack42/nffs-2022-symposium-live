import os
import csv
import numpy as np
from scipy.signal import savgol_filter
from scipy import interpolate



class AirfoilMgr(object):

    def __init__(self):
        self.here = os.path.abspath(os.path.dirname(__file__))
        self.catalog = self._getCatalog()
        self.selected = None

    def _getCatalog(self):
        self.datadir = os.path.join(self.here, 'data/coefdata')
        files = []
        for file in os.listdir(self.datadir):
            d = os.path.join(self.datadir, file)
            if os.path.isdir(d):
                files.append(file)
        return files

    def showAirfoils(self):
        print(self.catalog)

    def selectAirfoil(self, name):
        if not name in self.catalog:
            print("Illegal airfoil")
            return
        print("Selected:", name)
        self.selected = name

    def fit_curve(self, x, y, smooth=False): # using a cubic spline
        if smooth:
            smooth_y = savgol_filter(y, 11, 3)
            fit = interpolate.CubicSpline(x,smooth_y)
        else:
            fit = interpolate.CubicSpline(x,y)
        return fit

    def loadData(self,re):
        name = self.selected
        print("Loading",self.selected)
        cpath = os.path.join(self.datadir,name,re)
        cfiles = os.listdir(cpath)
        for c in cfiles:
            if c.startswith('.'): continue
            fname = os.path.join(cpath, c)
            print("\tLoading", c)
            prefix = c[0:2]
            x = []
            y = []
            with open(fname,'r') as fin:
                raw_data = csv.reader(fin,delimiter=',')
                for row in raw_data:
                    x.append(float(row[0]))
                    y.append(float(row[1]))
            dx = np.array(x)
            dy = np.array(y)
            fit = self.fit_curve(dx, dy, True)
            if prefix == 'CL':
                clfit = fit
            elif prefix == 'CD':
                cdfit = fit
            elif prefix == 'CP':
                cpfit = fit
            else:
                cmfit = fit
        return clfit, cdfit, cmfit, cpfit




if __name__ == '__main__':
    a = AirfoilMgr()
    a.showAirfoils()
    a.selectAirfoil('arc0401')
    cl, cd, cm = a.loadData()
    print(cl(5), cd(5), cm(5))



