from rpython.rlib.rrandom import Random
from rpython.rlib.rarithmetic import r_uint
import os

UINT32_MIN = 0
UINT32_MAX = 4294967295


class BaseRandom(object):

    def _get_uint32_byte(self):
        raise NotImplementedError

    def random(self):
        raise NotImplementedError

    def randrange(self, start, stop):
        # [start, stop)
        num_items = stop - start
        if num_items <= 0:
            raise ValueError("Invalid range.")
        if num_items == 1:
            return start
        elif num_items > (UINT32_MAX + 1):  # uint32 max can represent UINT32_MAX + 1 item
            raise ValueError("Range too big, maximum range is %d." % UINT32_MAX)
        # Discard remainder to try and make it uniform (Assuming `uint32_gen_fn()` is uniform)
        max_num = r_uint(UINT32_MAX - ((UINT32_MAX + 1) % num_items))
        u32_rand_num = self._get_uint32_byte()
        while u32_rand_num > max_num:
            u32_rand_num = self._get_uint32_byte()
        rand_num = r_uint(u32_rand_num % num_items)
        return rand_num + start

    def randint(self, a, b):
        # [a, b]
        return self.randrange(a, b + 1)

    def choice(self, seq):
        idx = self.randrange(0, len(seq))
        return seq[idx]


class RRandom(BaseRandom):
    def __init__(self, seed):
        self._rng = Random(seed)

    def _get_uint32_byte(self):
        return self._rng.genrand32()

    def random(self):
        # [0.0, 1.0]
        return self._rng.random()


class StdInRandom(BaseRandom):
    STDIN_FD = 0
    READ_N_BYTES = 4

    def _get_uint32_byte(self):
        num = 0
        for i, b in enumerate(os.read(StdInRandom.STDIN_FD, StdInRandom.READ_N_BYTES)):
            num += ord(b) << (8 * i)
        return r_uint(num)
