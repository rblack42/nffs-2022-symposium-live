import json
import os
import numpy as np
from scipy.interpolate import InterpolatedUnivariateSpline


class Curve(object):
    """process curves digitized with WebAppDigitizer"""

    def __init__(self):
        self.data_dir = '../data'

    def get_list_data(self, name):
        if name == 'CL':
            yd = [0.06, 0.135, 0.2, 0.25, 0.3, 0.35, 0.395, 0.44]
        else:
            yd = [0.008, 0.009, 0.01, 0.012, 0.014, 0.019, 0.024, 0.0335]
        xd = [-2.0, 0.0, 2.0, 4.0, 6.0, 8.0, 10.0, 12.0]
        return xd, yd

    def get_WAD_data(self, file_name):
        fn = os.path.join(self.data_dir, file_name)
        if not os.path.exists(fn):
            return [],[]
        with open(fn,'r') as fin:
            data = json.load(fin)

        points = data['datasetColl'][0]['data']
        x = []
        y = []
        for p in points:
            x.append(p['value'][0])
            y.append(p['value'][1])
        return x,y

    def fit_curve(self,xd,yd):
        """Return a curve fit function using spline interpolation"""
        xi = np.array(xd)
        yi = np.array(yd)
        x = np.linspace(-6, 20, 50)
        order = 1
        s = InterpolatedUnivariateSpline(xi, yi, k=order)
        return s


if __name__ == '__main__':
    c = Curve()
    xp, yp = c.get_WAD_data('circular-arc-3%-Cl.json')
    fit_a = c.fit_curve(xp,yp)
    xd,yd = c.get_list_data('CL')
    fit_b = c.fit_curve(xd,yd)
    print(fit_a(20))
    print(fit_b(20))

