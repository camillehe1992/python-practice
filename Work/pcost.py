# pcost.py
#
# Exercise 1.27

f = open('Data/portfolio.csv', 'rt')
headers = next(f)
cost = 0.0
for line in f:
    row = line.split(',')
    cost = int(row[1]) * float(row[2]) + cost
print('Total cost', cost)
