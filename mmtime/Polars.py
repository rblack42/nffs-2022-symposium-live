import os
import numpy as np

DIR = 'data/airfoils/xfoil'

class Polars(object):

    def __init__(self, anames):
        for airfoil in anames:
            self.decode(airfoil)

    def decode(self, aname):
        afile = aname + '.pol'
        apath = os.path.join(DIR, afile)
        if os.path.isfile(apath):
            print("decoding:", afile)

            columns = [
                "alpha",
                "CL",
                "CD",
                "CDp",
                "CM",
                "xtr_upper",
                "xtr_lower"
            ]
            try:
                data = np.genfromtxt(
                    apath,
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
        dname = os.path.join(dpath, 'CDp.csv')
        CDp = data['CDp']
        with open(dname,'w') as fout:
            for i in range(len(alpha)):
                fout.write(f'{alpha[i]}, {CDp[i]}\n')



if __name__ == '__main__':
    airfoils = [
        'arc0401',

        'arc0301',
        'arc0201'
    ]
    p = Polars(airfoils)

