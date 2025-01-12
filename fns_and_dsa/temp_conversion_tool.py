#!/bin/bash

FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

temperature = int(input("Enter the temperature to convert: "))
temperature_convention = input("Is this temperature in Celsius or Fahrenheit? (C/F): ")

def convert_to_celsius(fahrenheit):
	C = FAHRENHEIT_TO_CELSIUS_FACTOR * (fahrenheit - 32)
	return C

def convert_to_fahrenheit(celsius):
	F = CELSIUS_TO_FAHRENHEIT_FACTOR *  celsius + 32
	return F

if temperature_convention == 'F':
	print(f"{temperature}°F is {convert_to_celsius(temperature)}°C")
elif temperature_convention == 'C':
	print(f"{temperature}°C is {convert_to_fahrenheit(temperature)}°F")
else:
	print("Enter valid temperature and unit")
