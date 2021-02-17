# Problem 2 - Paying Debt Off in a Year

# Now write a program that calculates the minimum fixed monthly payment needed in order pay off a credit card balance within 12 months. By a fixed monthly payment, we mean a single number which does not change each month, but instead is a constant amount that will be paid each month.

# In this problem, we will not be dealing with a minimum monthly payment rate.

# The following variables contain values as described below:

# balance - the outstanding balance on the credit card

# annualInterestRate - annual interest rate as a decimal

# The program should print out one line: the lowest monthly payment that will pay off all debt in under 1 year, for example:

# Lowest Payment: 180 
# Assume that the interest is compounded monthly according to the balance at the end of the month (after the payment for that month is made). The monthly payment must be a multiple of $10 and is the same for all months. Notice that it is possible for the balance to become negative using this payment scheme, which is okay. A summary of the required math is found below:

# Monthly interest rate = (Annual interest rate) / 12.0
# Monthly unpaid balance = (Previous balance) - (Minimum fixed monthly payment)
# Updated balance each month = (Monthly unpaid balance) + (Monthly interest rate x Monthly unpaid balance)




# Define a function that calculate the remaining balance after 12 months
def remaining_balance(balance, annualInterestRate, fixed_payment):
    unpaid_balance = balance
    for i in range(1,12):
        unpaid_balance -= fixed_payment
        remaining_balance = unpaid_balance * (1 + (annualInterestRate/11))
        #print(remaining_balance)
    return remaining_balance
# initial fixed payment amount    
fixed_payment = 0.0

# The main loop to determine the required fixed_payment in order to reach zero balance or less by end of year
while remaining_balance(balance, annualInterestRate, fixed_payment) > 0:
    fixed_payment += 10.0
    remaining_balance(balance, annualInterestRate, fixed_payment)
    
print('Lowest Payment:{:.2f}'.format(fixed_payment))
    

