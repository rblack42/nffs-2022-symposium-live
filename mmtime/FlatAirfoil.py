import numpy as np


class FlatAirfoil(object):

    def __init__(self):
        self.camber = 0.05
        self.npoints = 100
        self.thickness = 0.01

    def set_npoints(self, npoints):
        self.npoints = npoints

    def set_camber(self, camber):
        self.camber= 0

    def set_thickness(self, thickness):
        self.thickness = thickness/100

    def get_camber_line(self):
        x = np.linspace(0.0, 1.0, self.npoints)
        y = np.zeros(self.npoints)
        return x,y
