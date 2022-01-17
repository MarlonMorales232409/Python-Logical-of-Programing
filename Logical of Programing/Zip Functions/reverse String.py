import math

fruits = ['apples', 'bananas', 'oranges']
prices = [0.99, 0.55, 0.70]
items = [3, 5, 6]

zipped = list(zip(fruits, prices, items))

for (fruit, price, item) in zipped:
    print(f'{fruit} at {price} cents by {item} will be { math.floor(price * item)} dollars')
