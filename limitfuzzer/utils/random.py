from rpython.rlib.rrandom import Random
from rpython.rlib.rarithmetic import r_uint32, r_ulonglong, r_int
import time

_TIMESTAMP_MULTIPLIER = 1000000
UINT32_MIN = 0
UINT32_MAX = 4294967295


class RRandom(object):
    def __init__(self, seed=None):
        if seed is None:
            seed = r_ulonglong(time.time() * _TIMESTAMP_MULTIPLIER)
        self._rng = Random(seed)

    def random(self):
        # [0.0, 1.0]
        return self._rng.random()

    def randrange(self, start, stop):
        # [start, stop)
        num_items = stop - start
        if num_items <= 0:
            raise ValueError("Invalid range.")
        if num_items == 1:
            return start
        elif num_items > (UINT32_MAX + 1):  # uint32 max can represent UINT32_MAX + 1 item
            raise ValueError("Range too big, maximum range is %d." % UINT32_MAX)
        # Discard remainder to try and make it uniform (Assuming `genrand32()` is uniform)
        max_num = r_uint32(UINT32_MAX - ((UINT32_MAX + 1) % num_items))
        u32_rand_num = self._rng.genrand32()
        while u32_rand_num > max_num:
            u32_rand_num = self._rng.genrand32()
        rand_num = r_int(u32_rand_num % num_items)
        return rand_num + start

    def randint(self, a, b):
        # [a, b]
        return self.randrange(a, b + 1)

    def choice(self, seq):
        idx = self.randrange(0, len(seq))
        return seq[idx]


# Initialise a new instance on import
random = RRandom()
