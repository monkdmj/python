"""[summary]

[description]
"""


def test_iter():
    """[summary]

    [description]
    """
    it = iter(range(20))
    while True:
        try:
            x = next(it)
            print(x)
        except StopIteration as e:
            print('Over!', e.value)
            break


def add(x, y, f):
    return f(x) + f(y)


def f(x):
    return x * x


def fn(x, y):
    return x * 10 + y


def char2num(s):
    return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7,
            '8': 8, '9': 9}[s]


def str2int(s):
    """[summary]

    [description]

    Arguments:
        s {[type]} -- [description]

    Returns:
        [type] -- [description]
    """
    from functools import reduce
    # return reduce(fn,lirst(map(char2num,s)))
    # return reduce(lambda x, y: x * 10 + y, map(char2num, s))
    return reduce(lambda x, y: x * 10 + y, map(lambda s: {'0': 0, '1': 1,
                                                          '2': 2, '3': 3,
                                                          '4': 4, '5': 5,
                                                          '6': 6, '7': 7,
                                                          '8': 8, '9': 9
                                                          }[s], s))


def normalize(name):
    return name[0].upper() + name[1:].lower()


def str2float(s):
    from functools import reduce
    intpart, decpart = s.split('.')
    decpart = decpart[::-1]
    return reduce(lambda x, y: x * 10 + y, map(char2num, intpart)) \
        + reduce(lambda x, y: x / 10 + y, map(char2num, decpart)) / 10

# help(str.split)
