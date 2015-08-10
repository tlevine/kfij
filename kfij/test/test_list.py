import tempfile

from .. import List

def test_reversed():
    with tempfile.NamedTemporaryFile() as tmp:
        tmp.close()
        observed = list(reversed(List(tmp.name, range(10))))
    assert observed == list(reversed(range(10)))
