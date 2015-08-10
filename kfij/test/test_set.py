import tempfile, itertools

import pytest

from ..set import Set

# @pytest.mark.randomize(func, ncalls=10)

method_calls = itertools.product(dir(Set), [tuple(), ('abc',)])

@pytest.mark.parametrize('method_name, args', method_calls)
def test_method_call(method_name, args):
    with tempfile.NamedTemporaryFile() as tmp:
        kfij = Set(tmp.name)
        normal = set()

        assert getattr(kfij, method_name)(*args) == normal(*args)
