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
    

