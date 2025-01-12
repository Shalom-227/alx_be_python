#!/bin/python3

import datetime

def display_current_datetime():
	current_date = datetime.datetime.now()
	return current_date.replace(microsecond=0)

print("Current date and time: ", display_current_datetime())

number_of_days = int(input("Enter the number of days to add to the current date: "))

def calculate_future_date(a):
	return datetime.timedelta(days=number_of_days)

future_date = display_current_datetime() + calculate_future_date(number_of_days)
print("Future date: ",future_date.date())
