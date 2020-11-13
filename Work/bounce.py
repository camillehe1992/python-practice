# bounce.py
#
# Exercise 1.5
total_height = 100
rate = 0.6
step = 1
height = 100
while step <= 10:
    print(step, round(height * rate, 4))
    step = step + 1
    height = height * rate

