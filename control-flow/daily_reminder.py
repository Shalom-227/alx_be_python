#!/bin/python3

task=input("Enter your task: ")
priority=input("Priority (high/medium/low): ")
time_bound=input("Is it time-bound? (yes/no): ")

match priority:
	case "high":
		message = f"Reminder: '{task}' is a high priority task" 
	case "medium":
		message = f"Reminder: '{task}' is a medium priority task"
	case "low":
		message = f"Reminder: '{task}' is a low priority task" 
	case _:
		print(f"Invalid input. Enter priority level (high/medium/low")
if time_bound == 'yes':
	print(f"{message} that requires immediate attention today!")
else:
	print(f"{message}. Consider completing it when you have free time.")
