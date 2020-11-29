# pcost.py
#
# Exercise 1.27
from report import read_portfolio

def portfolio_cost(filename):
    portfolio = read_portfolio(filename)
    cost = 0.0
    for p in portfolio:
        cost += round(p['shares'] * p['price'], 2)
    return cost
