import logging
import os

class Set:
    '''
    Persist a set-like structure to a file.
    The contents of the set must be str or bytes.

    It is safe to access the same Set instance from
    multiple threads. It is unsafe to get any more
    concurrent than that.
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

    @classmethod
    def _apply_destructive_func(func_name):
        getattr(self._set)
        os.remove
        close fp

        

safe_func_names =  [
    'copy',
    'difference', 'union', 'intersection', 'symmetric_difference',
    'isdisjoint', 'issubset',
]
destructive_func_names = [
    'clear',
    'pop', 'remove',
    'intersection_update',
    'symmetric_difference_update',
    'update',
]

for func_name in safe_func_names:
    setattr(Set, func_name, lambda self, *args: getattr(self._set, func_name)(*args))
