from rpython.rlib import listsort


def _tuple_lt(a, b):
    return a[0] < b[0]


# Sort tuples using the first item in the tuples
# Example:
#   lst = [(3, ['<digit>', '<integer>']), (2, ['<digit>'])]
#   TupleSorter(lst).sort()
#   print lst
#
# Output:
#   [(2, ['<digit>']), (3, ['<digit>', '<integer>'])]
TupleSorter = listsort.make_timsort_class(lt=_tuple_lt)
