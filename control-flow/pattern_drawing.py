#!/bin/python3

size =int(input("Enter the size of the pattern: "))
row = 0
while row < size:
	row = row + 1
	for _ in range(size):
		print("*",end ='')
	print('')
