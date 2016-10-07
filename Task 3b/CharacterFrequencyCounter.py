import fileinput
import sys
from collections import Counter

def main():
	input_string = getInputString()
	cnt = Counter(input_string)
	print cnt

def getInputString():
	input_string = ""
	for line in fileinput.input():
		input_string = input_string + line
	return input_string

if __name__ == '__main__':
	main()