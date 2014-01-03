from argparse import ArgumentParser
from shlex import split
from subprocess import call
import sys
		
class rpnCalc():
	def __init__(self):
		self.rpnStack = []
		self.ops = "*/+-%"
		self.eqn = []
	
	def setEqn(self, rpnEq):
		self.eqn = rpnEq
		
	def processEqn(self):
		for i in range(len(self.eqn)):
			if (self.eqn[i] in self.ops):
				tempVar = 0
				if (self.eqn[i] == '+'):
					fItem = float(self.rpnStack.pop())
					sItem = float(self.rpnStack.pop())
					self.rpnStack.append(fItem + sItem)
				elif(self.eqn[i] == '-'):
					fItem = float(self.rpnStack.pop())
					sItem = float(self.rpnStack.pop())
					self.rpnStack.append(fItem - sItem)
				elif (self.eqn[i] == '/'):
					fItem = float(self.rpnStack.pop())
					sItem = float(self.rpnStack.pop())
					self.rpnStack.append(fItem / sItem)
				elif (self.eqn[i] == '*'):
					fItem = float(self.rpnStack.pop())
					sItem = float(self.rpnStack.pop())
					self.rpnStack.append(fItem * sItem)
				else:
					fItem = float(self.rpnStack.pop())
					sItem = float(self.rpnStack.pop())
					self.rpnStack.append(fItem % sItem)
					
			else:
				self.rpnStack.append(self.eqn[i])
		return self.rpnStack.pop()
				

argParser = ArgumentParser(description='Process a reverse-Polish notation equation.')

argParser.add_argument('eqn', metavar='item',  nargs='+', type=str, help='An item in a reverse-Polish notation equation.')

rpnEq = argParser.parse_args().eqn[0]

rpnInst = rpnCalc()
rpnInst.setEqn(split(rpnEq))

x = rpnInst.processEqn()

print x
