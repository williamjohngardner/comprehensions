def add(*args):
    for arg in args:
        sum += arg

    return sum


test = add(1, 2, 3)
print(test)