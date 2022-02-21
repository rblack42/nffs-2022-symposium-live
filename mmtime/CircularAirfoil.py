import math
import numpy as np


class CircularAirfoil(object):

    def __init__(self):
        self.camber = 0.05
        self.npoints = 100
        self.thickness = 0.01

    def set_npoints(self, npoints):
        self.npoints = npoints

    def set_camber(self, camber):
        self.camber = camber/100

    def set_thickness(self, thickness):
        self.thickness = thickness/100

    def get_camber_line(self):
        x = np.linspace(0.0,1.0, self.npoints)
        y = []

        # set up arc adjusted for thickness le radius
        ch = 1.0 - self.thickness/2
        self.radius = ch**2/(8.0 * self.camber) + self.camber/2
        self.theta = 2 * math.atan(2 * self.camber/ch)
        self.sweep = 2 * self.theta

        # generate points at equal angles
        nx = self.npoints
        da = self.sweep/(nx-1)
        x = []
        y = []
        xc = self.thickness/2 + ch/2
        yc = self.camber - self.radius

        a0 = math.pi/2 + self.theta
        for i in range(nx):
            angle = a0 - i * da
            x.append(xc + self.radius * math.cos(angle))
            y.append(yc + self.radius * math.sin(angle))
        return np.array(x),np.array(y)


if __name__ == '__main__':
    ca = CircularAirfoil()
    ca.set_camber(4.0)
    ca.set_npoints(101)
    x,y = ca.get_camber_line()
    for i in range(len(x)):
        print(i, x[i], y[i])



