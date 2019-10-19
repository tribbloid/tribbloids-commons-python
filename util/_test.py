from dataclasses import dataclass

from tribbloids_commons.util import lazy

nn = 0


@lazy
def fn1():
    global nn
    nn = nn + 1
    return nn


@dataclass
class HasFn2(object):
    nn = 0

    @lazy
    def fn2(self):
        self.nn = self.nn + 1
        return self.nn


def test_lazy():

    vs1 = [fn1 for i in range(0, 5)]
    assert vs1 == [1, 1, 1, 1, 1]

    c = HasFn2()
    vs2 = [c.fn2 for i in range(0, 5)]
    assert (vs2 == [1, 1, 1, 1, 1])
