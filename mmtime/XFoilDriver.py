DATPATH = 'data/airfoils'
from xfoil import XFoil
from xfoil.test import naca0012
xf = XFoil()
xf.airfoil = naca0012
xf.Re = 1e6
xf.max_iter = 40
xf.print = False
a,cl,cd,cm,cp = xf.aseq(-20,20,0.5)

np = len(a)
for i in range(np):
    print(a[i],cl[i],cd[i],cm[i],cp[i])
