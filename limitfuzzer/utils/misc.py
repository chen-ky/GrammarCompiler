def max_(iterable):
    length = len(iterable)
    assert length > 0
    curr_max = iterable[0]
    i = 1
    while i < length:
        item = iterable[i]
        if item > curr_max:
            curr_max = item
        i += 1
    return curr_max


def min_(iterable):
    length = len(iterable)
    assert length > 0
    curr_min = iterable[0]
    i = 1
    while i < length:
        item = iterable[i]
        if item < curr_min:
            curr_min = item
        i += 1
    return curr_min
