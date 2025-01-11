#!/bin/python3

def perform_operation(num1, num2, operation):
	match operation:
		case 'add':
			return num1 + num2
		case 'subtract':
			return num1 - num2
		case 'multiply':
			return num1 * num2
		case 'divide':
			if num2 == 0:
				print("Numerator cannot be 0.")
				num2= float(input("Enter the second number: "))
			else:
				return num1 / num2
		case _:
			return "Invalid"

