from .kfij import Kfij

class Set(Kfij):
    factory = set
    def load(self):
        for line in self.readlines():
            self.add(line)
    def dump(self):
        for x in self:
            self.writeline(x)
    def add(self, x):
        '''
        :param str x: Item to be added to the set
        '''
        # Filter
        if x not in self.cache:
            self.writeline(x)
            self.cache.add(x)

Set.enable_safe_funcs('copy', 'isdisjoint', 'issubset',
                      'difference', 'union', 'intersection', 'symmetric_difference',
                      '__contains__', '__len__', '__iter__',
                      '__sub__', '__rsub__',
                      '__and__', '__or__',
                      '__rand__', '__ror__', '__rxor__',
                      '__ge__', '__gt__', '__le__', '__lt__', '__eq__')
Set.enable_destructive_funcs('clear', 'pop', 'remove',
                             'intersection_update',
                             'symmetric_difference_update',
                             'update')
