import subprocess
import os


AIRFOIL = "FLAT01"

DATADIR = "./data/xfoil"

class Xfoil(object):

    def start(self):
        """start xfoil process, set stdin for input""" 
        ps = subprocess.Popen('xfoil', stdin=subprocess.PIPE)
        self.ps = ps

    def command(self, cmd):
        """send commamd to xfoil"""
        txt = bytes(cmd, 'utf-8')
        print(txt)
        self.ps.stdin.write(txt + b'\n')

    def graphics(self, flag):
        if not flag:
            print("no plots will be generated")
            self.command("PLOP")
            self.command("G F")
            self.command("")

    def operating(self, re, iters):
        print("Set operating paramaters")
        self.command("OPER")
        self.command("VISC")
        self.command("%d" % re)
        self.command("ITER %d" % iters)

    def polar(self):
        print("generate polar data file")
        polarfile = "%s.pol" % AIRFOIL
        if os.path.isfile(polarfile):
            os.remove(polarfile)

        self.command("PACC")
        self.command(polarfile)
        self.command("")
        self.command("ASEQ")
        self.command("-20")
        self.command("20")
        self.command("2")
        self.command("PACC")
        self.command("")

    def load_airfoil(self, airfoil):
        print("load airfoil data file")
        self.command("LOAD")
        self.command("%s/%s.dat" % (DATADIR,AIRFOIL))
        self.command(AIRFOIL)


if __name__ == '__main__':
    xf = Xfoil()
    xf.start()
    xf.load_airfoil("FLAT01")
    xf.graphics(False)
    xf.operating(3000,500)
    xf.polar()
    print("terminating...")
    xf.command("QUIT")

