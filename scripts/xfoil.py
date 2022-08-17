import subprocess
import os
from pathlib import Path

DATADIR = '../mmtime/data/airfoils'


class XFOIL(object):

    def __init__(self, airfoil, re, iter):
        self.re = re
        self.iter = iter
        self.airfoil = airfoil

    def launch(self):
        self.fout = open('tmpout','wb')
        self.fin = open('tmpout','r')
        ps = subprocess.Popen('xfoil', 
                stdin=subprocess.PIPE,
                stdout=self.fout,
                stderr=self.fout)
        self.ps = ps

    def command(self, cmd):
        print(cmd)
        self.ps.stdin.write(f'{cmd.strip()}\n'.encode('utf-8'))
        self.ps.stdin.flush()
        out = self.fin.read()
        print(out)

    def read(self):
        print(self.ps.stdout.readline().decode('utf-8').strip())
    def run(self):
        af = self.airfoil
        cmd = f'load {DATADIR}/{af}/{af}.dat'
        self.command(cmd)
        self.command(af)
        self.command('plop')
        self.command('G F')
        self.command('')
        self.command('oper')
        iter = self.iter
        self.command(f'iter {iter}')
        re = self.re
        self.command(f'visc {re}')
        self.command('pacc')
        outfile = f'{af}_RE{re}.pol'
        self.command('run.pol')
        self.command('')
        self.command('aseq')
        self.command('-20')
        self.command('0')
        self.command('2')
        self.command('aseq')
        self.command('2')
        self.command('20')
        self.command('2')
        self.command('pacc')
        print(os.listdir('.'))
        self.command('')
        self.command('quit')
        print(os.listdir())
        #if os.path.isfile('run.pol'):
        #   Path('run.pol').rename(f'{DATADIR}/{af}/{outfile}')
        #else:
        #    print("file not found",'run.pol')

    def quit(self):
        self.ps.kill()
        self.fout.close()
        self.fin.close()

if __name__ == '__main__':

    xf = XFOIL('flat0001', 3000, 200)
    xf.launch()
    xf.run()
    xf.quit()
            
