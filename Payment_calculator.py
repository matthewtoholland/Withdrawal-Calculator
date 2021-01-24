import numpy as np
import numpy_financial as npf

"""
Python script for calculating annual deductions on an interest account to empty it"

"""

value = float(input("Initial Value: £"))
residual =  float(input("Final Value: £"))
interest = float(input("Annual Interest: "))
years = int(input("Years to withdraw: "))

#Calculates the annual deduction
annual = npf.pmt(interest, years, value, fv= -residual)

#Prints the annual deduction
print("£ {:.2f} per annum".format(abs(annual)))
amount = value

#displays the annual balance until the final value is reacehd
for year in range(years):
    amount = (amount * (1+interest)) + annual
    print("Year {}: £{:.2f}".format(year + 1, amount))
