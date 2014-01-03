#All of the imports
from argparse import ArgumentParser
from shlex import split
from subprocess import call

#Try to do this so errors are not thrown
try:
	#Reverse Polish notation stack
	rpnStack = []
	#List of all acceptable operators
	ops = "*/+-%^"

	#Parsing command line arguments and splitting them into individual elements
	argParser = ArgumentParser(description='Process a reverse-Polish notation equation.')
	argParser.add_argument('eqn', metavar='item',  nargs='+', type=str, help='An item in a reverse-Polish notation equation.')
	rpnEq = argParser.parse_args().eqn[0].replace('(', '').replace(')', '').replace('[', '').replace(']', '')\
	.replace('{', '').replace('}', '')
	eqn = split(rpnEq)
	
	#Converting all non-operator elements into floats.
	for i in range(len(eqn)):
		if (eqn[i] not in ops):
			eqn[i] = float(eqn[i])

	
	#Reverse Polish notation algorithm
	for i in range(len(eqn)):
		#Check if item is operator
		if (str(eqn[i]) in ops):
			#Pop two variables to operate on
			fItem = rpnStack.pop()
			sItem = rpnStack.pop()
			
			#Perform corresponding operation and put back in stack
			if (eqn[i] == '+'):
				rpnStack.append(fItem + sItem)
			elif(eqn[i] == '-'):
				rpnStack.append(fItem - sItem)
			elif (eqn[i] == '/'):
				rpnStack.append(sItem / fItem)
			elif (eqn[i] == '*'):
				rpnStack.append(fItem * sItem)
			elif (eqn[i] == '^'):
				rpnStack.append(fItem ** sItem)
			else:
				rpnStack.append(fItem % sItem)
				
		else:
			#Put number in stack
			rpnStack.append(eqn[i])

	#Pop stack because the only element left should be the answer
	print rpnStack.pop()
	
except:
	#Tell user that the equation is invalid
	print "Invalid equation."

