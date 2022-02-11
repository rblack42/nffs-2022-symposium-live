import math

class ArcAirfoil(object):

    def __init__(self, C, T):
        """save airfoil parameters, set basic controls"""
        self.camber = C
        self.thickness = T
        self.nx = 125
        self.accuracy = 0.000001
        self.maxLEangle = 12

        # basic camber line setup
        self.genArc()
        self.genLE()

    def _ns(self, n):
        """format name values with optional leading zero"""
        if n < 10:
            return "0" + str(n)
        return str(n)

    def getName(self):
        nc = self._ns(self.camber)
        nt = self._ns(self.thickness)
        return  f"ARC{nc}{nt}"

    def genArc(self):
        """generate basic circular arc camber line"""
        c = self.camber/100     # camber
        t = self.thickness/100  # thickness
        ch = 1.0 - t/2             # chord (adjusted for round LE)
        radius = ch**2/(8.0 * c) + c/2
        theta = 2*math.atan(2*c/ch)
        sweep = 2 *  theta
        xc = t/2 + ch/2
        yc = c - radius
        # generate point lists
        xu = []
        xm = []
        xl = []
        yu = []
        ym = []
        yl = []
        nx = self.nx
        da = (sweep)/nx
        r = t/2
        self.r = r
        aa = r/25 - r
        cc = r
        for i in range(nx + 1):
            angle = theta - i * da
            x = xc - radius * math.sin(angle)
            y = yc + radius * math.cos(angle)
            if i > nx-5:
                j = nx - 5 - i
                xx = j*0.2
                tt = aa*xx**2 + cc
            else:
                tt = r
            dx = tt * math.sin(angle)
            dy = tt * math.cos(angle)
            xu.append(x - dx)
            xm.append(x)
            xl.append(x + dx)
            yu.append(y + dy)
            ym.append(y)
            yl.append(y - dy)
        self.theta = theta
        self.xu = xu
        self.xm = xm
        self.xl = xl
        self.yu = yu
        self.ym = ym
        self.yl = yl


    def genLE(self):
        maxLEangle = 12
        theta = self.theta
        r = self.r
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

        x = self.xm[0]
        y = self.ym[0]

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
        self.xule = xule
        self.yule = yule
        self.xlle = xlle
        self.ylle = ylle

    def writeAirfoilFile(self):
        name = self.getName()
        with open(f"data/airfoils/{name}.dat",'w') as fout:

            # load all points
            xule = self.xule
            yule = self.yule
            xlle = self.xlle
            ylle = self.ylle
            xu = self.xu
            yu = self.yu
            xl = self.xl
            yl = self.yl

            # display upper points
            nb = len(xu)
            for i in range(nb):
                j = nb-i-1
                x = xu[j]
                if x < self.accuracy:
                    x = 0.0
                y = yu[j]
                if abs(y) < self.accuracy:
                    y = 0.0
                fout.write("     {0:10.6f}   {1:10.6f}\n".format(x,y))

            # display upper LE points
            for i in range(1,len(xule)):
                x = xule[i]
                if x < self.accuracy:
                    x = 0.0
                y = yule[i]
                if abs(y) < self.accuracy:
                    y = 0.0
                fout.write("     {0:10.6f}   {1:10.6f}\n".format(x,y))

            # write lower LE points
            nb = len(xlle)
            for i in range(1,nb):
                j = nb - i - 1
                x = xlle[j]
                if x < self.accuracy:
                    x = 0.0
                y = ylle[j]
                if abs(y) < self.accuracy:
                    y = 0.0
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
    ra = ArcAirfoil(5, 1)
    ra.genArc()
    ra.writeAirfoilFile()
