from .kfij import Kfij

class Set(Kfij):
    factory = set
    def load(self, fp):
        for line in fp:
            self.add(line.rstrip('\r\n'))
    def dump(self, fp):
        for x in self:
            fp.write(x + '\n')

    def add(self, x):
        '''
        :param str x: Item to be added to the set
        '''
        if not isinstance(x, str) or '\r' in x or '\n' in x:
            raise NotImplementedError('Can\'t handle this sort of value')

        # Filter
        if x not in self.cache:
            self.cache.add(x)
            self.fp.write(x + '\n')

Set.enable_safe_funcs('copy', 'isdisjoint', 'issubset',
                      'difference', 'union', 'intersection', 'symmetric_difference',
                      '__contains__', '__len__',
                      '__sub__', '__rsub__',
                      '__and__', '__or__',
                      '__rand__', '__ror__', '__rxor__',
                      '__ge__', '__gt__', '__le__', '__lt__', '__eq__')
Set.enable_destructive_funcs('clear', 'pop', 'remove',
                             'intersection_update',
                             'symmetric_difference_update',
                             'update')
