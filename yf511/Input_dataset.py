import numpy as np
import re
import sys
#To get users' input for positions value with three invalid input, positived, listed and positioned.
def prompt_positions():
	
	
	try :
		input_positions = raw_input('Please choose List of the shares to buy in parallel:[1, 10, 100, 1000]?\n')
	
	except(KeyboardInterrupt,EOFError):
		sys.exit();

    
	if input_positions == 'quit':
		sys.exit();

	try:
		return get_list(input_positions)

	except InvalidPosition:
		print 'please choose from 1, 10, 100, 1000 for your positions.'
		return prompt_positions()
	
	except InvalidInteger:
		print 'Please input positive integers for positions.'
		return prompt_positions()

	except InvalidList:
		print 'Invalid list input.'
		return prompt_positions()


#To get users' input for trials value with three invalid input, positived and integer.
def prompt_ntrials():
	
	try:
		input_ntrials = raw_input('Number of trials want to try? \n')

	except(KeyboardInterrupt,EOFError):
		sys.exit();
	if input_ntrials == 'quit':
		sys.exit();
	
	try:
		return get_num(input_ntrials) 
		
	except InvalidInteger:
		print 'Please input positive integers for ntrials.'
		return prompt_ntrials()

# Selfdefined Exceptions with various invalid input
class InvalidList(Exception):
	def __str__(self):
		return 'Invalid list input.'

class InvalidInteger(Exception):
	def __str__(self):
		return 'Please input positive integers.'

class InvalidPosition(Exception):
	def __str__(self):
		return 'Please choose position from 1, 10, 100, and 1000.'

def get_list(input_str):#make the input into list format
	input_list = []
	if input_str[0] == '[' and input_str[-1] == ']':
		input_str = input_str.replace(" ","")
		input_str = input_str[1:-1]
		input_str_split = input_str.split(',')
		for i in input_str_split:
			if i.isdigit():
				intnew = int(i)
			else:
				raise InvalidInteger()

			if (intnew==1 or intnew==10 or intnew==100 or intnew==1000):
				input_list.append(intnew)
				
			else:
				raise InvalidPosition()	

		return input_list
	else:
		raise InvalidList()

def get_num(input_str):#make the input into integer
	if input_str.isdigit():
		input_int = int(input_str)
	else:
		raise InvalidInteger()

	return input_int


