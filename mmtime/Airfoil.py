import numpy as np
import os
import scipy
import math

from .SimplexAirfoil import SimplexAirfoil
from .CircularAirfoil import CircularAirfoil
from .FlatAirfoil import FlatAirfoil


class Airfoil(object):

    def __init__(self, name, chord, camber, thickness, npoints):
        """generate thin airfoil for xfoil testing"""
        self.chord = chord
        self.camber = camber
        self.thickness = thickness
        self.le_radius = self.thickness/100*self.chord/2
        self.name = name.lower()
        self.npoints = npoints

        # set selected airfoil
        if self.name == 'simplex':
            self.airfoil = SimplexAirfoil()
        elif self.name == 'circular':
            self.airfoil = CircularAirfoil()
        else:
            self.airfoil = FlatAirfoil()

        # initialize airfoil ohject
        self.airfoil.set_npoints(self.npoints)
        self.airfoil.set_camber(self.camber)
        self.airfoil.set_le_radius(self.le_radius)
        self.airfoil.set_chord(self.chord)
        self.xc, self.yc = self.airfoil.get_camber_line()
        self.dydx = self.get_camber_slopes()

    def get_camber_line(self):
        return self.airfoil.get_camber_line()

    def get_slopes(self):
        return self.dydx

    def get_surface(self):
        """return upper and lower point lists for thin airfoil of spec thickness"""
        xu = []
        yu = []
        xl = []
        yl = []

        for i in range(self.npoints-5):
            theta = self.dydx[i]
            alpha = math.pi/2 + theta
            x = self.xc[i]
            y = self.yc[i]
            r = self.le_radius
            dx = r * math.cos(alpha)
            dy = r * math.sin(alpha)
            xu.append(x + dx)
            xl.append(x - dx)
            yu.append(y + dy)
            yl.append(y - dy)
        return xu,yu,xl,yl

    def get_camber_slopes(self):
        # calculate slope list
        dydx = []
        nx = self.npoints
        for i in range(self.npoints):
            if i == 0:
                dy = (self.yc[1]-self.yc[0])
                dx = (self.xc[1]-self.xc[0])
            elif i == nx-1:
                dy = (self.yc[nx-1]-self.yc[nx-2])
                dx = (self.xc[nx-1]-self.xc[nx-2])
            else:
                dy = (self.yc[i+1]-self.yc[i-1])
                dx = (self.xc[i+1]-self.xc[i-1])
            slope = math.atan(dy/dx)
            dydx.append(slope)
        return dydx

    def get_le(self):
        maxLEangle = 12
        theta = self.dydx[0]
        r = self.le_radius
        nptot = round(180/maxLEangle)
        np1 = round(((math.pi/2 - theta) / math.pi) * nptot)
        np2 = round(((math.pi/2 + theta) / math.pi) * nptot)

        # generate top LE points
        alpha = math.pi/2 + theta
        dalpha = (math.pi/2 - theta)/np1
        xule = []
        yule = []
        xlle = []
        ylle = []

        x = self.xc[0]
        y = self.yc[0]
        for i in range(np1+1):
            xule.append(x + r * math.cos(alpha))
            yule.append(y + r * math.sin(alpha))
            alpha += dalpha

        # generate bottom LE points
        alpha = 3*math.pi/2 + theta
        dalpha = (math.pi/2 + theta)/np2
        for i in range(np2+1):
            xlle.append(x + r * math.cos(alpha))
            ylle.append(y + r * math.sin(alpha))
            alpha -= dalpha
        return xule, yule, xlle, ylle

    def get_te(self):
        r = self.le_radius
        # set trailing edce distribution
        aa = r/25 - r
        cc = r
        xtopte = []
        ytopte = []
        xbotte = []
        ybotte = []

        for i in range(5+1):
            j = self.npoints - 6 + i
            xx = i*0.2
            tt = aa*xx**2 + cc
            alpha = math.atan(self.dydx[j]) + math.pi/2
            xc = self.xc[j]
            yc = self.yc[j]
            xt = xc + tt * math.cos(alpha)
            yt = yc + tt * math.sin(alpha)
            xtopte.append(xt)
            ytopte.append(yt)
            alpha += math.pi
            xb = xc + tt * math.cos(alpha)
            yb = yc + tt * math.sin(alpha)
            xbotte.append(xb)
            ybotte.append(yb)
        return xtopte, ytopte, xbotte, ybotte

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


    def gen_xfoil_data_file(self,data_dir):
        """generate xfoil data file"""
        self.foil_dir = data_dir
        accuracy = 0.00001

        af = self.getName()
        afpath = os.path.join(data_dir,af)
        os.makedirs(afpath, exist_ok=True)
        dfile = f'{afpath}/{af}.dat'
        print("Generating:", dfile)
        with open(dfile,'w') as fout:

            # load all points
            xtl,ytl,xbl,ybl = self.get_le()
            xtb,ytb,xbb,ybb = self.get_surface()
            xtt,ytt,xbt,ybt = self.get_te()

            # display upper TE points
            nb = len(xtt)
            for i in range(nb):
                j = nb-i-1
                x = xtt[j]
                if x < accuracy:
                    x = 0.0
                y = ytt[j]
                if abs(y) < accuracy:
                    y = 0.0
                fout.write("     {0:10.6f}   {1:10.6f}\n".format(x,y))

            # display upper body points
            nb = len(xtb)
            for i in range(1,nb):
                j = nb-i-1
                x = xtb[j]

                if x < accuracy:
                    x = 0.0
                y = ytb[j]
                if abs(y) < accuracy:
                    y = 0.0
                fout.write("     {0:10.6f}   {1:10.6f}\n".format(x,y))

            # display upper LE points
            for i in range(1,len(xtl)):
                x = xtl[i]
                if x < accuracy:
                    x = 0.0
                y = ytl[i]
                if abs(y) < accuracy:
                    y = 0.0
                fout.write("     {0:10.6f}   {1:10.6f}\n".format(x,y))

            nb = len(xbl)
            for i in range(1,nb):
                j = nb - i - 1
                x = xbl[j]
                if x < accuracy:
                    x = 0.0
                y = ybl[j]
                if abs(y) < accuracy:
                    y = 0.0
                fout.write("     {0:10.6f}   {1:10.6f}\n".format(x,y))


            #display lower body points
            for i in range(1,len(xbb)):
                x = xbb[i]
                if x < accuracy:
                    x = 0.0
                y = ybb[i]
                if abs(y) < accuracy:
                    y = 0.0
                fout.write("     {0:10.6f}   {1:10.6f}\n".format(x,y))

            # display lower TE points
            for i in range(1,len(xbt)):
                x = xbt[i]
                if x < accuracy:
                    x = 0.0
                y = ybt[i]
                if abs(y) < accuracy:
                    y = 0.0
                fout.write("     {0:10.6f}   {1:10.6f}\n".format(x,y))
            print('done...')
            fout.close()

if __name__ == '__main__':
    af = Airfoil('simplex',1,2,1,51)
    af.gen_xfoil_data_file('data/airfoils')
