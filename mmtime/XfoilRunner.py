# test3 - xfoil driver
# used ideas from https://github.com/hoburg/pyxfoil

import pexpect
import os
from datetime import datetime as dt

DATADIR = os.path.abspath(
        os.path.join(
            os.path.dirname(__file__),
            'data/airfoils'
        )
)


class XfoilRunner(object):

    def __init__(self,airfoil, re, iter):
        self.airfoil = airfoil
        self.re = re
        self.iter = iter
        self.cwd = os.getcwd()
       
        # set working directory to airfoil data directory
        workdir = os.path.join(DATADIR,airfoil)
        os.chdir(workdir)

        # set up logging
        logdir = workdir + '/logs/'
        os.makedirs(logdir, exist_ok=True)

        # timestamp each log file
        nowstr = dt.strftime(dt.now(), '%Y_%m_%d_%H%M%S')
        logfile = open(logdir + 'XFOIL' + nowstr + '.log','w')

        # launch xfoil and wait for the prompt
        self.proc = pexpect.spawn('xfoil', 
                logfile = logfile, 
                encoding='utf-8')
        self.proc.expect('c>')

        # turn off graphics display
        self.send('PLOP')
        self.send('G F')
        self.send('')

    def send(self, cmd, resulting_prompt='c>'):

        self.proc.sendline(cmd)
        self.proc.expect(resulting_prompt)


    def quit(self):
        self.proc.sendline('QUIT')
        self.proc.close()
        os.chdir(self.cwd)

    def set_airfoil(self):
        af = self.airfoil
        self.send('load ' + af + '.dat', resulting_prompt='s>')
        self.send(self.airfoil)

    def gen_polar(self, minaoa=-20, maxaoa=20, aoastep=2, re=3000):
        print("Generating polar for " + self.airfoil)
        polar_name = f'{self.airfoil}_RE{self.re}.pol'
        if os.path.isfile(polar_name):
            os.remove(polar_name)
        self.send('OPER')
        self.send('ITER 200')
        self.send('VISC ' + str(self.re))
        self.send('PACC', resulting_prompt='s>')
        self.send(polar_name, resulting_prompt='s>')
        self.send('')
        self.send('ASEQ', resulting_prompt='r>')
        self.send(str(minaoa), resulting_prompt='r>')
        self.send(str(maxaoa), resulting_prompt='r>')
        self.send(str(aoastep))
        self.send('PACC')
        self.send('')


if __name__ == '__main__':
    xf = XfoilRunner('flat0001',3000,200)
    xf.set_airfoil()
    xf.gen_polar()
    xf.quit()
