import csv
import matplotlib.pyplot as plt
import numpy as np
import os
from pathlib import Path
from scipy import interpolate
from scipy.signal import savgol_filter
import numpy as np

def get_points(filename):
    x = []
    y = []
    with open(filename,'r') as fin:
        raw_data = csv.reader(fin,delimiter=',')
        for row in raw_data:
            x.append(float(row[0]))
            y.append(float(row[1]))
    return np.array(x), np.array(y)

def show_curve(x,y,title,xlabel,ylabel):
    plt.plot(x,y)
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.show()

def show_curve2(x,y1,y2,lab1,lab2,title,xlabel,ylabel):
    plt.plot(x,y1,label=lab1)
    plt.plot(x,y2,label=lab2)
    plt.title(title,fontsize=15)
    plt.xlabel(xlabel,fontsize=13)
    plt.ylabel(ylabel,fontsize=13)
    plt.show()

def fit_curve(x, y, smooth=False): # using a cubic spline
    if smooth:
        smooth_y = savgol_filter(y, 21, 3)
        fit = interpolate.CubicSpline(x,smooth_y)
    else:
        fit = interpolate.CubicSpline(x,y)
    return fit

def load_curve(filename, smooth=True):
    """Load a csv file and return curve function with optional smoothing"""
    filepath = dirname / filename
    c_x, c_y = get_points(filepath)
    fit = fit_curve(c_x, c_y, smooth)
    return fit

def transform(xcg,ycg, alpha, xp, yp):
    rad = alpha * np.pi/180
    xt = xp - xcg
    yt = yp - ycg
    x = xt * np.cos(rad) + yt * np.sin(rad)
    y = -xt * np.sin(rad) + yt * np.cos(rad)
    return x,y

if __name__ == '__main__':


    arc3dir = datadir / 'airfoils' / 'arc3'

    cl_data = arc3dir / 'Cl-3%-arc.csv'
    cd_data = arc3dir / 'Cd-3%-arc.csv'
    cm_data = arc3dir / 'Cm-3%-arc.csv'

    Cl_x, Cl_y = get_points(cl_data)
    Cd_x, Cd_y = get_points(cd_data)
    Cm_x, Cm_y = get_points(cm_data)
    print(Cl_x)
    print(Cl_y)
    Cm_x, Cm_y = get_points(cm_data)
    show_curve(Cl_x, Cl_y, 'Lift Coefficient', "alpha", "Cl")
    show_curve(Cd_x, Cd_y, 'Drag Coefficient', "alpha", "Cd")
    show_curve(Cm_x, Cm_y, 'Moment Coefficient', "alpha", "Cm")
    ClFunc = fit_curve(Cl_x, Cl_y)
    CdFunc = fit_curve(Cd_x, Cd_y)
    CmFunc = fit_curve(Cm_x, Cm_y)
    apts = np.linspace(Cl_x[0], Cl_x[-1], 50);
    ClFit = ClFunc(apts)
    CdFit = CdFunc(apts)
    CmFit = CmFunc(apts)
    show_curve(apts, ClFit, 'Lift Coefficient', "alpha", "Cl")
    show_curve(apts, CdFit, 'Drag Coefficient', "alpha", "Cd")
    show_curve(apts, CmFit, 'Moment Coefficient', "alpha", "Cm")
