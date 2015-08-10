import logging
import os

class Set:
    '''
    Persist an append-only set-like structure to a file.
    The contents of the set must be str or bytes.
    '''
    def __init__(self, filename):
        '''
        :param str filename: File at which to save state
        '''

        if os.path.exists(filename):
            with open(filename, 'r') as fp:
                self._set = set(line.rstrip('\r\n') for line in fp)
        else:
            with open(filename, 'w') as fp:
                fp.write('')
            self._set = set()

        self._fp = open(filename, 'a')

    def add(self, x):
        '''
        :param str x: Item to be added to the set
        '''
        if not isinstance(x, str) or '\r' in key or '\n' in key:
            raise NotImplementedError('Can\'t handle this sort of value')

        # Filter
        if x not in self._x:
            self._set.add(key)
            self._fp.write(key + '\n')

    def clear(self):
    def copy(self):
        discard
    intersection_update
    pop
    remove
    symmetric_difference_update
    update

safe_func_names =  [
    'difference', 'union', 'intersection', 'symmetric_difference',
    'isdisjoint', 'issubset',
]
for func_name in safe_func_names:
    setattr(Set, func_name, lambda self, iterable: getattr(self._set, func_name)(iterable))
