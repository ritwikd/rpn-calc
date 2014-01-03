from argparse import ArgumentParser
from shlex import split

class rpcStack():
	def __init__(self):
		self.itemStack = []
	
	def itemPop(self):
		if (len(self.itemStack) > 0):
			tempVar = self.itemStack[0]
			del(self.itemStack[0])
			return tempVar
		else:
			print "No more items in stack."

	def itemIns(self, itemVal):
		self.itemStack.insert(0, itemVal)
		
class rpcCalc():
	def __init__(self):
		self.rpcStack = rpcStack()



argParser = ArgumentParser(description='Process a reverse-Polish notation equation.')

argParser.add_argument('eqn', metavar='item',  nargs='+', type=str, help='An item in a reverse-Polish notation equation.')

rpnEq = argParser.parse_args().eqn

print rpnEq
