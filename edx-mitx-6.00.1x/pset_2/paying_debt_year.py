#! usr/bin/python3

def paying_debt_year(balance, annualInterestRate, monthlyPaymentRate):
    """
    Function to calculate the outstanding balance to be paid after 1 year.
    Returns: remaining balance
    """
    for i in range(1, 13):
        paid = balance * monthlyPaymentRate
        new_balance = balance - paid
        monthly_interest = new_balance * (annualInterestRate/12)
        balance = new_balance + monthly_interest
        if i == 12:
            print("Remaining Balance: %.2f" % balance)


paying_debt_year(484, 0.2, 0.04)