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
	argParser.add_argument('--simple', help='Print the stack at each step.')
	endArgs =  argParser.parse_args()
	rpnEq = endArgs.eqn[0].replace('(', '').replace(')', '').replace('[', '').replace(']', '')\
	.replace('{', '').replace('}', '')

	verbosity = endArgs.simple
	eqn = split(rpnEq)
	
	#Converting all non-operator elements into floats.
	for i in range(len(eqn)):
		if (eqn[i] not in ops):
			eqn[i] = float(eqn[i])

	
	#Reverse Polish notation algorithm
	for i in range(len(eqn)):
		if (verbosity):
				print "Parsed element:" , eqn[i]
		#Check if item is operator
		if (str(eqn[i]) in ops):
			
			#Pop two variables to operate on
			fItem = rpnStack.pop()
			sItem = rpnStack.pop()
			
			#Perform corresponding operation and put back in stack
			if (eqn[i] == '+'):
				if (verbosity):
					print "Adding", fItem, "and", sItem
				rpnStack.append(fItem + sItem)
			elif(eqn[i] == '-'):
				if (verbosity):
					print "Subtracting", fItem, "and", sItem
				rpnStack.append(fItem - sItem)
			elif (eqn[i] == '/'):
				if (verbosity):
					print "Dividing", sItem, "and", fItem
				rpnStack.append(sItem / fItem)
			elif (eqn[i] == '*'):
				if (verbosity):
					print "Multiplying", fItem, "and", sItem
				rpnStack.append(fItem * sItem)
			elif (eqn[i] == '^'):
				if (verbosity):
					print "Raising", sItem, "to the power of", fItem
				rpnStack.append(sItem ** fItem)
			else:
				if (verbosity):
					print "Getting the remainder of", sItem, "divided by", fItem
				rpnStack.append(sItem % fItem)
				
		else:
			#Put number in stack
			rpnStack.append(eqn[i])
		if (verbosity):
			print rpnStack

	#Pop stack because the only element left should be the answer
	print rpnStack.pop()
	
except:
	#Tell user that the equation is invalid
	print "Invalid equation."

