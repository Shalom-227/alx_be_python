#!/bin/python3

income = input("Enter your monthly income: ");
income =int(income);

expenses =int(input("Enter your total monthly expenses: "));

Monthly_Savings = income - expenses;
Projected_Savings = (Monthly_Savings * 12 + (Monthly_Savings * 12 * 0.05));
print(f"Your monthly savings are ${Monthly_Savings}.");
print(f"Projected savings after one year, with interest, is: ${int(Projected_Savings)}."); 
