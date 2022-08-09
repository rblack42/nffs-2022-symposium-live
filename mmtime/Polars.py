import os
import numpy as np
from xfoil import XFoil
from xfoil.test import naca0012
from xfoil.simplex import Simplex

DIR = 'data/airfoils'

class Polars(object):

    def __init__(self, anames):
        self.anames = anames

    def decode(self):
        for aname in self.anames:
            self._decode(aname)

    def decode_one(self, aname):
        afile = aname + '.pol'
        apath = os.path.join(DIR, aname, afile)
        print("decoding: %s" % apath)
        if os.path.isfile(apath):
            print("decoding:", afile)

            columns = [
                "alpha",
                "CL",
                "CD",
                "CDp",
                "CM",
            ]
            try:
                data = np.genfromtxt(
                    apath,
                    names = columns,
                    skip_header=12,
                    usecols=np.arange(len(columns))
                ).reshape(-1, len(columns))
            except OSError:
                data = np.array([]).reshape(-1, len(columns))
            has_valid_outputs = len(data) != 0
            data_clean = {
                k: data[:, index] if has_valid_outputs else np.array([])
                for index, k in enumerate(columns)
            }
            self.gen_csv(aname,data_clean)

    def gen_csv(self, aname, data):
        dpath = os.path.join('data/airfoils', aname)
        os.makedirs(dpath, exist_ok=True)
        alpha = data['alpha']
        # create CL file
        dname = os.path.join(dpath, 'CL.csv')
        CL = data['CL']
        print("Writing CL file:", dpath)
        with open(dname,'w') as fout:
            for i in range(len(alpha)):
                fout.write(f'{alpha[i]}, {CL[i]}\n')
        # create CD file
        dname = os.path.join(dpath, 'CD.csv')
        CD = data['CD']
        with open(dname,'w') as fout:
            for i in range(len(alpha)):
                fout.write(f'{alpha[i]}, {CD[i]}\n')
        # create CM file
        dname = os.path.join(dpath, 'CM.csv')
        CM = data['CM']
        with open(dname,'w') as fout:
            for i in range(len(alpha)):
                fout.write(f'{alpha[i]}, {CM[i]}\n')
        # create CDp file
        dname = os.path.join(dpath, 'CP.csv')
        CP = data['CDp']
        with open(dname,'w') as fout:
            for i in range(len(alpha)):
                fout.write(f'{alpha[i]}, {CP[i]}\n')


    def _aname(self, aname):
        thickness = int(aname[-2:])
        camber = int(aname[-4:-2])
        name = aname[:-4]
        return name, camber, thickness

    def gen_polars(self):
        for aname in self.anames:
            dpath = os.path.join(DIR,aname,aname+'.dat')
            if not os.path.isfile(dpath):
                print("No data file:", dpath)
                continue
            print("Generating polars for", aname)
            name, camber, thickness = self._aname(aname)
            xf = XFoil()
            s = Simplex()
            xf.airfoil = s.airfoil(camber)
            xf.Re = 3000
            xf.max_iter = 40
            xf.print = False
            a,cl,cd,cm,cp = xf.aseq(-20,20,0.5)
            data = {}
            data['alpha'] = a
            data['CL'] = cl
            data['CD'] = cd
            data['CM'] = cm
            data['CP'] = cp
            self.gen_csv(aname,data)


if __name__ == '__main__':
    airfoils = [
        'flat0001',
        #'simplex0201',
        #'simplex0301',
        #'simplex0401',
        #'simplex0501',
        #'simplex0601',
    ]
    p = Polars(airfoils)
    p.decode_one("flat0001")

