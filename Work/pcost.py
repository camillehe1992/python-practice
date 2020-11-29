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

def main(argv):
    if len(argv) != 2:
        raise SystemExit('filename must be provided')
    cost = portfolio_cost(argv[1])
    print(f'Total cost: {cost}')

if __name__ == '__main__':
    import sys
    main(sys.argv)
