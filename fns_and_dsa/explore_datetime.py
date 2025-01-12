#!/bin/python3

from datetime import datetime
from datetime import timedelta

def display_current_datetime():
	current_date = datetime.now()
	return current_date.replace(microsecond=0)

current_date = datetime.now()
formatted_current_date = current_date.strftime("%Y-%m-%d %H:%M:%S")
print("Current date and time: ", formatted_current_date)

number_of_days = int(input("Enter the number of days to add to the current date: "))

def calculate_future_date(a):
	return timedelta(days=number_of_days)

future_date = display_current_datetime() + calculate_future_date(number_of_days)
print(future_date.strftime("%Y-%m-%d"))
#Alternative to achieve same print outcome
#print("Future date: ",future_date.date()) 
