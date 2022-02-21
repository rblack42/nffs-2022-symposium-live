import math
import numpy as np


class SimplexAirfoil(object):

    def __init__(self):
        """save airfoil parameters, set basic controls"""
        self.camber = 5  # percent chord
        self.npoints = 51
        self.chord = 1.0
        self.le_radius = 0  # percent chord


    def set_npoints(self, npoints):
        self.npoints = npoints

    def set_camber(self, camber):
        self.camber = camber

    def set_le_radius(self, radius):
        """set le radius as percentage of chord"""
        self.le_radius = radius

    def set_chord(self, chord):
        """set airfoil chord without le adjust"""
        self.chord = chord

    def get_camber_line(self):

        """return list of points on camber line. camber is in percentage"""
        print("generating simplex camberline")
        npoints = self.npoints
        camber = self.camber
        le_radius = self.le_radius
        chord = self.chord - le_radius
        alpha = 1.554 * camber * math.pi/180
        k = 1/math.tan(alpha)
        print(alpha,k)
        print(chord, camber, le_radius, npoints)

        # generate airfoil points
        roa = np.linspace(0,chord,npoints)/chord
        roa[0] = 0.0000001  # avoid infinity in ln(0)
        psi = np.pi * np.tan(alpha/2) * np.log(roa)
        rho = chord * np.exp(psi / np.tan(alpha))
        x = rho * np.cos(psi)
        if le_radius > 0:
            x = x + le_radius  # adjust si TE is at chord
        y = rho * np.sin(-psi)
        return x,y

if __name__ == '__main__':
    ra = SimplexAirfoil()
    ra.set_npoints(26)
    ra.set_chord(2)
    ra.set_le_radius(0)
    xc, yc = ra.get_camber_line()
    for i in range(len(xc)):
        print(i,xc[i],yc[i])

