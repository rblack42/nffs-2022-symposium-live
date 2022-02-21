import math

class ReflexAirfoil(object):

    def __init__(self, C, XC, R, XR, T):
        """save airfoil parameters, set basic controls"""
        self.C = C
        self.XC = XC
        self.R = R
        self.XR = XR
        self.T = T
        self.nx = 125
        self.accuracy = 0.000001
        self.maxLEangle = 12

        # basic camberline setup
        self.genBSpline()
        self.genCamberLine()
        self.getSlopes()


    def _ns(self, n):
        """format name values with optional leading zero"""
        if n < 10:
            return "0" + str(n)
        return str(n)

    def getName(self):
        nc = self._ns(self.C)
        nxc = self._ns(self.XC)
        nr = self._ns(self.R)
        nxr = self._ns(self.XR)
        nt = self._ns(self.C)
        return  f"BEZ{nc}{nxc}{nr}{nxr}{nt}"

    def genCamberLine(self):
        """generate basic bspline camber line"""
        cx = 3*(self.x1-self.x0)
        bx = 3*(self.x2-self.x1)-cx
        ax = self.x3-self.x0-cx-bx
        cy = 3*(self.y1-self.y0)
        by = 3*(self.y2-self.y1)-cy
        ay = self.y3-self.y0-cy-by

        # generate point lists
        x = []
        y = []
        dx = 1/self.nx
        for m in range(self.nx + 1):
            tm = m * dx
            x.append(ax*tm**3+bx*tm**2+cx*tm+self.x0)
            y.append(ay*tm**3+by*tm**2+cy*tm+self.y0)
        self.xp = x
        self.yp = y

    def genBSpline(self):
        """calculate bspline control points"""
        c = self.C/100
        xc = self.XC/100
        r = self.R/100
        xr = self.XR/100
        t = self.T/100

        # ndary conditions
        self.x0 = t/2
        self.y0 = 0.0
        self.x3 = 1.0
        self.y3 = 0.0

        # initial guesses for control points
        self.x1 = xc
        self.y1 = c
        self.x2 = xr
        self.y2 = r

        for h in range(10):
            test = 0
            k = 0
            # y1 adjust loop
            while test == 0:
                k = k + 1
                self.genCamberLine()
                if abs(max(self.yp)-c) < self.accuracy:
                    test = 1
                    #print("y1 converged at:", self.y1)
                elif max(self.yp) > c:
                    self.y1 = self.y1-(max(self.yp)-c)/2
                elif max(self.yp) < c:
                    self.y1 = self.y1+(c-max(self.yp))/2
                if k > 1000:
                    test = 1
                    print("Infinite loop, no converge on y1!")

            test = 0
            k = 0
            # y2 adjust loop
            while test == 0:
                k = k + 1
                self.genCamberLine()
                if abs(r+min(self.yp)) < self.accuracy:
                    test = 1
                    #print("y2 converged at:", self.y2)
                elif min(self.yp) > -r:
                    self.y2 = self.y2-(min(self.yp)+r)/2
                elif min(self.yp) < -r:
                    self.y2 = self.y2+(-r-min(self.yp))/2
                if k > 1000:
                    test = 1
                    print("Infinite loop, no converge on y2!")

            val=max(self.yp) # Find max element in yp
            j = self.yp.index(val)
            test = 0
            k = 0
            # x1 adjust loop
            while test == 0:
                k = k + 1
                self.genCamberLine()
                if abs(self.xp[j]-xc) < self.accuracy:
                    test = 1
                    #print("x1 converged at:", self.x1)
                elif self.xp[j] > xc:
                    self.x1 = self.x1-(self.xp[j]-xc)/2
                elif self.xp[j] < xc:
                    self.x1 = self.x1+(xc-self.xp[j])/2
                if k > 1000:
                    test = 1
                    print("Infinite loop, no converge on x1!")

            val=min(self.yp) # Find min element in yp
            i = self.yp.index(val)
            test = 0
            k = 0
            # x2 adjust loop
            while test == 0:
                k = k + 1
                self.genCamberLine()
                if abs(self.xp[i]-xr) < self.accuracy:
                    test = 1
                    #print("x2 converged at:", self.x2)
                elif self.xp[i] > xr:
                    self.x2 = self.x2-(self.xp[i]-xr)/2
                elif self.xp[i] < xr:
                    self.x2 = self.x2+(xr-self.xp[i])/2
                if k > 1000:
                    test = 1
                    print("Infinite loop, no converge!")

    def getSlopes(self):
        # generate current camber line
        self.genCamberLine()
        # calculate slope list
        dydx = []
        for i in range(self.nx+1):
            if i == 0:
                dy = (self.yp[1]-self.yp[0])
                dx = (self.xp[1]-self.xp[0])
            elif i == self.nx:
                dy = (self.yp[self.nx]-self.yp[self.nx-1])
                dx = (self.xp[self.nx]-self.xp[self.nx-1])
            else:
                dy = (self.yp[i+1]-self.yp[i-1])
                dx = (self.xp[i+1]-self.xp[i-1])
            dydx.append(dy/dx)
        self.dydx = dydx
        self.alphaLE = math.atan(self.dydx[0])
        return self.xp, dydx

    def getLE(self):
        nptot = round(180/self.maxLEangle)
        np1 = round((((math.pi/2) - math.atan(self.dydx[0])) / (math.pi)) * nptot)
        np2 = round((((math.pi/2) + math.atan(self.dydx[0])) / (math.pi)) * nptot)

        # generate top LE points
        alpha = math.pi/2 + self.alphaLE
        dalpha = (math.pi/2 - self.alphaLE)/np1
        xtople = []
        ytople = []
        xbotle = []
        ybotle = []

        xt = self.xp[0]
        yt = self.yp[0]
        r = self.T/100/2
        for i in range(np1+1):
            xt = self.x0 + r * math.cos(alpha)
            yt = self.y0 + r * math.sin(alpha)
            xtople.append(xt)
            ytople.append(yt)
            alpha += dalpha

        # generate bottom LE points
        alpha = 3*math.pi/2 + self.alphaLE
        dalpha = (math.pi/2 + self.alphaLE)/np2
        for i in range(np2+1):
            xb = self.x0 + r * math.cos(alpha)
            yb = self.y0 + r * math.sin(alpha)
            xbotle.append(xb)
            ybotle.append(yb)
            alpha -= dalpha
        return xtople, ytople, xbotle, ybotle

    def getCamberPoints(self):
        # generate normal points along camber line
        xtop = []
        ytop = []
        xbot = []
        ybot = []
        r = self.T/100/2
        for i in range(self.nx-4):
            alpha = math.pi/2 + math.atan(self.dydx[i])
            xc = self.xp[i]
            yc = self.yp[i]
            xt = xc + r * math.cos(alpha)
            yt = yc + r * math.sin(alpha)
            xtop.append(xt)
            ytop.append(yt)
            alpha += math.pi
            xb = xc + r * math.cos(alpha)
            yb = yc + r * math.sin(alpha)
            xbot.append(xb)
            ybot.append(yb)
        return xtop,ytop,xbot,ybot


    def getTE(self):
        t = self.T/100
        r = t/2
        # set trailing edce distribution
        aa = r/25 - r
        cc = r
        xtopte = []
        ytopte = []
        xbotte = []
        ybotte = []

        for i in range(5+1):
            j = self.nx - 5 + i
            xx = i*0.2
            tt = aa*xx**2 + cc
            alpha = math.atan(self.dydx[j]) + math.pi/2
            xc = self.xp[j]
            yc = self.yp[j]
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

    def writeAirfoilFile(self):
        name = self.getName()
        with open(f"data/airfoils/{name}.dat",'w') as fout:

            # load all points
            xtl,ytl,xbl,ybl = self.getLE()
            xtb,ytb,xbb,ybb = self.getCamberPoints()
            xtt,ytt,xbt,ybt = self.getTE()

            # display upper TE points
            nb = len(xtt)
            for i in range(nb):
                j = nb-i-1
                x = xtt[j]
                if x < self.accuracy:
                    x = 0.0
                y = ytt[j]
                if abs(y) < self.accuracy:
                    y = 0.0
                fout.write("     {0:10.6f}   {1:10.6f}\n".format(x,y))

            # display upper body points
            nb = len(xtb)
            for i in range(1,nb):
                j = nb-i-1
                x = xtb[j]

                if x < self.accuracy:
                    x = 0.0
                y = ytb[j]
                if abs(y) < self.accuracy:
                    y = 0.0
                fout.write("     {0:10.6f}   {1:10.6f}\n".format(x,y))

            # display upper LE points
            for i in range(1,len(xtl)):
                x = xtl[i]
                if x < self.accuracy:
                    x = 0.0
                y = ytl[i]
                if abs(y) < self.accuracy:
                    y = 0.0
                fout.write("     {0:10.6f}   {1:10.6f}\n".format(x,y))

            nb = len(xbl)
            for i in range(1,nb):
                j = nb - i - 1
                x = xbl[j]
                if x < self.accuracy:
                    x = 0.0
                y = ybl[j]
                if abs(y) < self.accuracy:
                    y = 0.0
                fout.write("     {0:10.6f}   {1:10.6f}\n".format(x,y))


            #display lower body points
            for i in range(1,len(xbb)):
                x = xbb[i]
                if x < self.accuracy:
                    x = 0.0
                y = ybb[i]
                if abs(y) < self.accuracy:
                    y = 0.0
                fout.write("     {0:10.6f}   {1:10.6f}\n".format(x,y))

            # display lower TE points
            for i in range(1,len(xbt)):
                x = xbt[i]
                if x < self.accuracy:
                    x = 0.0
                y = ybt[i]
                if abs(y) < self.accuracy:
                    y = 0.0
                fout.write("     {0:10.6f}   {1:10.6f}\n".format(x,y))

    def getAirfoilPoints(self):
        # load all points
        xtl,ytl,xbl,ybl = self.getLE()
        xtb,ytb,xbb,ybb = self.getCamberPoints()
        xtt,ytt,xbt,ybt = self.getTE()
        xu = xtl + xtb + xtt
        yu = ytl + ytb + ytt
        xl = xbl + xbb + xbt
        yl = ybl + ybb + ybt
        return xu,yu,xl,yl



if __name__ == '__main__':
    ra = ReflexAirfoil(5,25,1,85,1)
    xt,xb,yt,yb = ra.getTE()
    xt,yt,xb,yb = ra.getCamberPoints()
    ra.writeAirfoilFile()
