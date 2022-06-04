import numpy as np
import math

class FlatAirfoil(object):

    def __init__(self,T):
        self.npoints = 125
        self.thickness = T
        self.accuracy = 0.0000001
        self.LEangle = 15

        # generate basic flat plate
        self.genPlate()
        self.genLE()
    
    def _ns(self, n):
        """format name values with optional leading zero"""
        if n < 10:
            return "0" + str(n)
        return str(n)

    def set_npoints(self, npoints):
        self.npoints = npoints

    def set_thickness(self, thickness):
        self.thickness = thickness/100

    def get_camber_line(self):
        x = np.linspace(0.0, 1.0, self.npoints)
        y = np.zeros(self.npoints)
        return x,y

    def getName(self):
        nc = self._ns(self.thickness)
        return f"FLAT{nc}"

    def genPlate(self):
        a = -3.125
        t = self.thickness/100
        b = t/2
        nx = self.npoints
        dx = (1-b)/nx
        xu = []
        xm = []
        xl = []
        yu = []
        ym = []
        yl = []
        r = t/2
        for i in range(nx + 1):
            x = b + i * dx
            if i > nx-6:
                # trailing edge arc
                j = i - (nx - 6) -1
                xx = j*dx
                tt = a*xx**2 + b
            else:
                tt = b
            dy = tt
            xu.append(x)
            xm.append(x)
            xl.append(x)
            yu.append(dy)
            ym.append(0)
            yl.append(-dy)
        self.xu = xu
        self.xm = xm
        self.xl = xl
        self.yu = yu
        self.ym = ym
        self.yl = yl

    def genLE(self):
        xule = []
        yule = []
        xlle = []
        ylle = []

        nptot = round(180/self.LEangle)
        np1 = int(nptot/2)
        np2 = nptot-np1
        # upper LE points
        t = self.thickness/100
        r = t/2
        alpha = 90
        for i in range(np1+1):
            xalpha = alpha * math.pi/180.0
            x = r * math.cos(xalpha)
            y = r * math.sin(xalpha)
            xule.append(x) 
            yule.append(y)
            alpha = alpha + self.LEangle
        # lower LE points
        alpha = 270
        for i in range(np2+1):
            xlle.append(xule[i])
            ylle.append(-yule[i])
        self.xule = xule
        self.yule = yule
        self.xlle = xlle
        self.ylle = ylle
        print(xule,yule)

    def writeAirfoilFile(self):
        name = self.getName()
        with open(f"data/xfoil/{name}.dat",'w') as fout:

            # load all points
            xule = self.xule
            yule = self.yule
            xlle = self.xlle
            ylle = self.ylle
            xu = self.xu
            yu = self.yu
            xl = self.xl
            yl = self.yl

            # write upper points from te forward
            nb = len(xu)
            for i in range(nb):
                j = nb-i-1
                x = xu[j]
                y = yu[j]
                fout.write("     {0:10.6f}   {1:10.6f}\n".format(x,y))

            # display upper LE points
            for i in range(1,len(xule)):
                x = xule[i] + self.thickness/200
                y = yule[i]
                fout.write("     {0:10.6f}   {1:10.6f}\n".format(x,y))

            # write lower LE points
            nb = len(xlle)
            for i in range(1,nb):
                j = nb - i - 1
                x = xlle[j] + self.thickness/200
                #if x < self.accuracy:
                #    x = 0.0
                y = ylle[j]
                #if abs(y) < self.accuracy:
                #    y = 0.0
                fout.write("     {0:10.6f}   {1:10.6f}\n".format(x,y))

            #display lower body points
            for i in range(1,len(xl)):
                x = xl[i]
                if x < self.accuracy:
                    x = 0.0
                y = yl[i]
                if abs(y) < self.accuracy:
                    y = 0.0
                fout.write("     {0:10.6f}   {1:10.6f}\n".format(x,y))



if __name__ == '__main__':
    # generate flat airfoil for analysis
        T = 1
        ra = FlatAirfoil(T)
        ra.genPlate()
        ra.writeAirfoilFile()

