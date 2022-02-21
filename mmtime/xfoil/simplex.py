import numpy as np
import os
from .model import Airfoil
DIR = '/Users/rblack/_dev/nffs-symposium/live-2022/mmtime/data/airfoils'


class Simplex(object):

    def __init__(self):
        self.camber = 5
        self.thickness = 1
        self.name = 'simplex'

    def _ns(self, n):
        """format name values with optional leading zero"""
        if n < 10:
            return "0" + str(n)
        return str(n)

    def getName(self):
        name = self.name
        camber = self._ns(self.camber)
        thickness = self._ns(self.thickness)
        return  f"{name}{camber}{thickness}"


    def airfoil(self, camber):
        self.camber = camber
        name = self.getName()

        dpath = os.path.join(DIR, name, name + '.dat')
        if not os.path.isfile(dpath):
            print("Data file not found:", dpath)
            return
        print("Loading data file:", dpath)
        with open(dpath,'r') as fin:
            lines = fin.readlines()
            nl = len(lines)
            print(nl, "lines loaded")
            x = []
            y = []
            for i in range(nl):
                l = lines[i]
                xs, ys = l.split()
                x.append(float(xs))
                y.append(float(ys))
            xp = np.array(x)
            yp = np.array(y)
        return Airfoil(x=xp,y=yp)


if __name__ == '__main__':
    s = Simplex()
    s.airfoil(5)
