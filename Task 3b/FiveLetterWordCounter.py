import fileinput
import sys
from collections import Counter

def main():
	input_string = getInputString()
	cnt = Counter()
	index = 0
	while(index < len(input_string)-4):
		cnt[input_string[index:index+5]] += 1
		index += 1
	print cnt

def getInputString():
	input_string = ""
	for line in fileinput.input():
		input_string = input_string + line
	return input_string

if __name__ == '__main__':
	main()