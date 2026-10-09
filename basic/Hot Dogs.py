import sys

custom_prices = []
for line in sys.stdin:
    custom_prices.extend(map(int, line.split()))

price_counts = [0] * 5001
max_price = 0

for price in custom_prices:
    price_counts[price] += 1
    max_price = max(max_price, price)

max_earnings = 0
optimal_price = 0
customers = 0

for price in range(max_price, 0, -1):
    customers += price_counts[price]
    earnings = customers * price

    if earnings >= max_earnings:
        max_earnings = earnings
        optimal_price = price

print(optimal_price)



