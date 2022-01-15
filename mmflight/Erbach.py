import math
import sys
import os

class Erbach(object):

    def __init__(self):
        self.win_angle = 2
        self.stab_angle = -2
        self.data_dir = './data'
        self.airfoil = 'mcbride-b7'
        self.model = 'erbach'

        cwd = os.path.dirname(__file__)
        print("cwd",cwd)
        dpath = os.path.abspath(os.path.join(cwd,'data','airfoils'))
        mpath = os.path.abspath(os.path.join(cwd,'data','models'))
        self.model_dir = mpath
        self.data_dir = dpath
        print("Data Dir:", self.data_dir)

    def set_airfoil(self, name):
        """set up to use named airfoil"""
        name = name.lower() # just in case
        (fils,  = os.path.walk(self.adir)
        print(a)

    def set_model(self, name='erbach'):
        """load model design data"""
        self.AW = 150          # WING AREA IN SQ. INCHES
        self.SW = self.AW/144  # WING AREA IN SW. FEET
        self.WC  = 5.5         # WING CHORD IN INCHES
        self.WI = 2            # WING INCIDENCE, DEGREES
        self.WH = 3            # WING HEIGHT IN INCHES
        self.W =0.070          # OVERALL WEIGHT IN OUNCE
        self.WT = self.W/16    # overall weight in pounds
        self.PCW = 0.40        # RATIO OF STAB AREA TO WING AREA.
        self.TA = 17.0         # wing MAC to stab MAC


    def normal(self,n,d):
        """Erbach's code used this scheme to limit display digits"""
        f = 10**n
        d1 = d * f
        d1 = int(d1)
        d1 = d1/f
        return d1

    def set_coefficients(self):
        """set lift and drag coefficients for selected airfoil"""
        self.CLw = self.CL[self.jw]
        self.CLs = self.CL[self.js]
        self.CDw = self.CD[self.jw]
        self.CDs = self.CD[self.js]

    def set_alignment(self,wa, sa):
        self.wing_angle = wa
        self.stab_angle = sa
        self.js  =  int(self.stab_angle/2+1)
        self.jw =  int(self.wing_angle/2+1)
        self.WI = self.wing_angle - self.stab_angle
        self.set_coefficients()
        # these values depend on alignment only
        self.set_velocity()
        self.set_power()


    def set_velocity(self):
        """ using current wing and stab angles, calculate velocity"""
        self.VE = (self.WT/(0.00119*self.SW*(self.CLw+self.PCW*self.CLs)))**0.5

    def get_velocity(self):
        return self.VE


    def set_power(self):
        """calculate power for level flight"""
        self.set_velocity()
        VE = self.VE
        self.AWL=self.CLw*self.SW*(0.00119)*VE*VE*16
        self.BWD=self.CDw*self.SW*(0.00119)*VE*VE*16
        self.CTL=self.CLs*self.SW*self.PCW*(0.00119)*VE*VE*16
        self.DTD=self.CDs*self.SW*self.PCW*(0.00119)*VE*VE*16
        self.P = self.VE*(self.BWD+self.DTD)*12

    def get_power(self):
        return self.P

    def get_moment(self,cg):
        """calculate pitching moment"""
        R = self.stab_angle * math.pi/180.0
        DW = self.WC*(cg - 0.25)
        TA = self.TA
        WH = self.WH

        EWLA=WH*math.sin(R)-DW*math.cos(R)
        FWDA=WH*math.cos(R)-DW*math.sin(R)
        GTLA=(TA-DW)*math.cos(R)
        HTDA=(TA-DW)*math.sin(R)

        JMWL=-self.AWL*EWLA
        KMWD=+self.BWD*FWDA
        LMTL=-self.CTL*GTLA
        MMTD=-self.DTD*HTDA
        CM = JMWL+KMWD+LMTL+MMTD
        return CM

    def run(self):
        self.set_coefficients()
        self.velocity()
        self.power()
        self.moment(0.5)

        print("{0:2.1f} DEG. WING INCIDENCE FOR THIS RUN".format(self.WI))
        print("{0:2.1f} deg. body/stab  angle  of attack".format(self.stab_angle))
        print("{0:3.1f} DEG. WING ANGLE OF ATTACK".format(self.WI+self.stab_angle))
        print("{0:3.1f}% STAB AREA".format(self.PCW*100))

        VE = self.normal(2,self.VE)
        power = self.normal(4,self.power)

        print("{0:3.2f} FT/SEC CALC. VELOCITY".format(VE))

        # CALC. POWER FOR THIS ANG.ATTACK
        print("{0:1.3f} IN OZ/SEC POWER REQUIRED".format(power))

        # show moment
        moment = self.normal(4,self.moment)
        print("{0:1.3f} Moment".format(moment))


if __name__ == '__main__':
    e = Erbach()
    #e.set_model('base')
    #e.set_airfoil('basic')
    #e.set_alignment(2, -2)
    #print("velocity:",e.get_velocity())
    #print("power:",e.get_power())
    #for i in range(8):
    #   cg = 0.3 + i*0.1
    #    print("\tcg: {0:3.1f} moment: {1:6.3f}".format(cg,e.get_moment(cg)))

