balance = 42
annualInterestRate = 0.2
monthlyPaymentRate = 0.04


for i in range(12):
    unpaid_balance = balance * (1- monthlyPaymentRate)
    balance = unpaid_balance * (1 + (annualInterestRate/12))
print('Remaining balance:{:.2f}'.format(balance))
