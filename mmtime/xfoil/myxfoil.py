import subprocess
import os
import sys


class Xfoil(object):

	def __init__(self):
		pass

	def start(self):
		self.ps = None
		with open(os.devnull, "w") as fp:
			self.ps = subprocess.Popen(["xfoil"],
								stdin = subprocess.PIPE,
								stdout = fp,
								stderr = None,
								encoding = 'utf8')
		if self.ps is None:
			print("Cannot start Cfool")
			sys.exit(1)

	def xfcmd(self, cmd, echo = False):
		self.ps.stdin.write(cmd + '\n')
		if echo:
			print(cmd)

if __name__ == '__main__':
	xf = Xfoil()
	xf.start()
	xf.xfcmd('quit', echo=True)

		
