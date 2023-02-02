class StrSet(object):
    def __init__(self, item=None):
        """
        Arguments:
        item: If item is not None, add `item` to the set.
        """
        self._set = {"": None}
        if item is not None:
            self._set[item] = None

    def add(self, item):
        self._set[item] = None

    def get(self):
        return self._set.keys()

    def union(self, incoming_set):
        result = StrSet()
        for k in self._set:
            result.add(k)
        for k in incoming_set._set:
            result.add(k)
        return result

    def __iter__(self):
        return self._set.keys().__iter__()
