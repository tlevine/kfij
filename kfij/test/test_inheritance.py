import tempfile, itertools

import pytest

from .. import Kfij, List, Set

# @pytest.mark.randomize(func, ncalls=10)

def testcases(*Classes):
    for Class in Classes:
        method_names = set(dir(Class)) - set(dir(Kfij)) - {'__iter__', '__reversed__'}
        yield from itertools.product([Class], method_names, [tuple(), ('abc',)])

@pytest.mark.parametrize('Class, method_name, args', testcases(List, Set))
def test_method_call(Class, method_name, args):
    with tempfile.NamedTemporaryFile() as tmp:
        tmp.close()

        kfij = Class(tmp.name)
        normal = Class.factory()

        f = getattr(kfij, method_name)
        try:
            expected = getattr(normal, method_name)(*args)
        except Exception as e:
            with pytest.raises(type(e)):
                f(*args)
        else:
            assert f(*args) == expected

