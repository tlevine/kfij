import tempfile, os

import pytest

from .. import List, Set

@pytest.mark.parametrize('Class, method_name', [(List, 'append'), (Set, 'add')])
def test_flush_writes(Class, method_name):
    with tempfile.NamedTemporaryFile() as tmp:
        for letter in 'abcde':
            old_size = os.stat(tmp.name).st_size
            getattr(Class(tmp.name), method_name)(letter)
            new_size = os.stat(tmp.name).st_size
            assert old_size + 2 == new_size

@pytest.mark.parametrize('Class', (List, Set))
def test_contains(Class):
    with tempfile.NamedTemporaryFile() as tmp:
        tmp.file.write(b'a\nb\nc\nd\ne\n')
        tmp.file.flush()
        for letter in 'abcde':
            assert letter in Class(tmp.name)
