def test():
    # locals()['v'] = x + 10
    # print(locals()['x'])
    # locals()['v'] = 1
    x = 15
    locals()['x'] = 1
    return locals()['x']

print(test())


def a(x):
    exec("locals()['x'] = 100")
    exec("locals()['y'] = 10")
    print(x)
    # print(y)
    return locals()['x']

print(a(10))
