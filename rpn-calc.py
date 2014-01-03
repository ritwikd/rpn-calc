#All of the imports
from argparse import ArgumentParser
from shlex import split
from subprocess import call

try:
	rpnStack = []
	ops = "*/+-%"

	argParser = ArgumentParser(description='Process a reverse-Polish notation equation.')

	argParser.add_argument('eqn', metavar='item',  nargs='+', type=str, help='An item in a reverse-Polish notation equation.')

	rpnEq = argParser.parse_args().eqn[0]

	eqn = split(rpnEq)


	for i in range(len(eqn)):
		if (eqn[i] in ops):
			tempVar = 0
			if (eqn[i] == '+'):
				fItem = float(rpnStack.pop())
				sItem = float(rpnStack.pop())
				rpnStack.append(fItem + sItem)
			elif(eqn[i] == '-'):
				fItem = float(rpnStack.pop())
				sItem = float(rpnStack.pop())
				rpnStack.append(fItem - sItem)
			elif (eqn[i] == '/'):
				fItem = float(rpnStack.pop())
				sItem = float(rpnStack.pop())
				rpnStack.append(fItem / sItem)
			elif (eqn[i] == '*'):
				fItem = float(rpnStack.pop())
				sItem = float(rpnStack.pop())
				rpnStack.append(fItem * sItem)
			else:
				fItem = float(rpnStack.pop())
				sItem = float(rpnStack.pop())
				rpnStack.append(fItem % sItem)
				
		else:
			rpnStack.append(eqn[i])

	print rpnStack.pop()
except:
	print "Invalid equation."

