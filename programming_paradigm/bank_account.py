#!/bin/Python3

class BankAccount:
	initial_balance = 0
	def __init__(self, account_balance):
		self.__account_balance = account_balance

	def deposit(self, amount):
		self.__account_balance = BankAccount.initial_balance + amount

	def withdraw(self, amount):
		if self.__account_balance >= amount:
			self.__account_balance = BankAccount.initial_balance - amount
			return self.__account_balance

	def display_balance(self):
		print(f"Current Balance: ${self.__account_balance}")

