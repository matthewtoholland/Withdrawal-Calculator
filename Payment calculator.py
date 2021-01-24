import numpy as np
import numpy_financial as npf

"""
Python script for calculating annual deductions on an interest account to empty it"

"""

value = float(input("Initial Value: "))
interest = float(input("Annual Interest: "))
years = int(input("Years to withdraw: "))
residual =  float(input("Final Value: "))

annual = npf.pmt(interest, years, value, fv= -residual)

print("£ {:.2f} per annum".format(abs(annual)))
amount = value

for year in range(years):
    amount = (amount * (1+interest)) + annual
    print("Year {}: £{:.2f}".format(year + 1, amount))
