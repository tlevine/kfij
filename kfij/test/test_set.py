import tempfile, itertools

import pytest

from ..kfij import Kfij
from ..kfijset import Set

# @pytest.mark.randomize(func, ncalls=10)

method_calls = itertools.product(set(dir(Set)) - set(dir(Kfij)), [tuple(), ('abc',)])

@pytest.mark.parametrize('method_name, args', method_calls)
def test_method_call(method_name, args):
    with tempfile.NamedTemporaryFile() as tmp:
        tmp.close()

        kfij = Set(tmp.name)
        normal = set()

        f = getattr(kfij, method_name)
        try:
            expected = getattr(normal, method_name)(*args)
        except Exception as e:
            with pytest.raises(type(e)):
                f(*args)
        else:
            assert f(*args) == expected

