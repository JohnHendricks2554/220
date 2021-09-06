"""
Name: John Hendricks
interest.py

Problem: Receiving user input, calculate the monthly interest charge on a credit card account.

Certification of authenticity:
I certify that this assignment is entirely my own work

"""

def main():
    ann_int_rate = eval(input("Please enter the annual interest rate: "))
    num_days_period = eval(input("Please enter the number of days in the billing cycle: "))
    prev_net_balance = eval(input("Please enter the previous net balance: "))
    payment_amount = eval(input("Please enter the payment amount received: "))
    day_of_payment = eval(input("Please enter the number of days payment made: "))

    avg_daily_charge = (prev_net_balance * num_days_period)

    avg_daily_charge -= (payment_amount * (num_days_period - day_of_payment))
    avg_daily_charge = avg_daily_charge / num_days_period

    monthly_int_rate = (ann_int_rate / 12)
    dec_monthly_rate = monthly_int_rate / 100
    monthly_charge = avg_daily_charge * dec_monthly_rate
    rounded_monthly = round(monthly_charge, 2)

    print(rounded_monthly)
