from functools import reduce

items = [1, 2, 3, 4, 5]
squared = []
for i in items:
    squared.append(i**2)

print('squared: {}'.format(squared))

new_squared = list(map(lambda x: x**2, items))
print('new_squared: {}'.format(new_squared))

def multiply(x):
    return x*x

def add(x):
    return x+x

funcs = [multiply, add]
for i in range(5):
    value = list(map(lambda x: x(i), funcs))
    print(value)

number_list = range(-5, 5)
less_than_zero = list(filter(lambda x: x < 0, number_list))
print(less_than_zero)

product = 1
list_data = [1, 2, 3, 4]
for num in list_data:
    product = product * num
print('product: {}'.format(product))

new_product = reduce((lambda x, y: x * y), list_data)
print('new_product: {}'.format(new_product))
