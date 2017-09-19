from functools import reduce

items = ["uno", "dos", "tre", "cuatro"]

# lambda
total = reduce(lambda a, b: (0, a[1] + b[1]), items)[1]

print(total)


# equivalente
def combine(a, b):
    return 0, a[1] + b[1]


total = reduce(combine, items)[1]
print(total)
