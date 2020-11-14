# mortgage.py
#
# Exercise 1.7

extra_payment = input('input extra payment:')
extra_payment_start_month = input('input extra start month:')
extra_payment_end_month = input('input extra end month:')

principal = 500000.0
rate = 0.05
init_payment = 2684.11
total_paid = 0.0
month = 0

extra_payment = int(extra_payment)
extra_payment_start_month = int(extra_payment_start_month)
extra_payment_end_month = int(extra_payment_end_month)

while principal > 0: 
    month = month + 1
    if month < extra_payment_start_month or month > extra_payment_end_month:
        payment = init_payment
    else:
        payment = init_payment + extra_payment
 
    if principal < payment:
        payment = principal
        principal = 0.0
    else:
        principal = round(principal * (1+rate/12) - payment, 2)
        
    total_paid = round(total_paid + payment, 2)
    print(month, total_paid, principal)

print('Total paid', total_paid)
print('Months', month)
