#!/usr/local/bin/python

result = []
candidates = range(3, 1000)
base = 2
product = base

while candidates:
    while product < 1000:
        if product in candidates:
            candidates.remove(product)
        product = product + base
    result.append(base)
    base = candidates[0]
    product = base
    del candidates[0]
result.append(base)
print result
