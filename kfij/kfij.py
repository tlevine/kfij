from functools import wraps

class Kfij:
    '''
    Persist a set-like structure to a file.
    The contents of the set must be str or bytes.

    It is safe to access the same Set instance from
    multiple threads. It is unsafe to get any more
    concurrent than that.
    '''
    def __init__(self, filename, *args, **kwargs):
        '''
        :param str filename: File at which to save state
        '''

        if len(args) + len(kwargs) > 0:
            with open(filename, 'w') as fp:
                fp.write('')
        elif os.path.exists(filename):
            with open(filename, 'r') as fp:
                self._cache = self.factory(line.rstrip('\r\n') for line in fp)
        else:
            with open(filename, 'w') as fp:
                fp.write('')
            self._cache = self.kfij_factory()

        self._fp = open(filename, 'a')

    @staticmethod
    def kfij_factory(*args, **kwargs):
        '''
        You must set the factory equal to the class that the present class is mimicing, such as set or list.
        '''
        raise NotImplementedError('You must set the %s.kfij_factory.', self.__class__.__name__)

    def kfij_extend(self, old):
        '''
        You must set this to the function to a function that extends
        the present Kfij with the data from an old one.
        This is "extend" for sets and "update" for dicts, for example.
        '''
        raise NotImplementedError('You must set the %s.kfij_extend.', self.__class__.__name__)

    @classmethod
    def apply_destructive_funcs(Class, *func_names):
        for func_name in func_names:

            f = getattr(self._cache, func_name)

            @wraps(f)
            def g(self, *args, **kwargs):
                if self._lock:
                    raise EnvironmentError('%s is locked' % repr(self))

                self._lock = True
                self._fp.close()

                os.remove(self._fp.name)
                f(*args, **kwargs)

                self._fp = open(self._fp.name, 'a')

                for args in self._cache:
                    self.appender(*args)

                self._lock = False

                return output

            setattr(Class, func_name, g)

    @classmethod
    def apply_safe_funcs(Class, *func_names):
        for func_name in func_names:

            f = getattr(self._cache, func_name)

            @wraps(f)
            def g(self, *args, **kwargs):
                if self._lock:
                    raise EnvironmentError('%s is locked' % repr(self))
                return f(*args, **kwargs)

            setattr(Class, func_name, g)
        

safe_func_names =  [
    'copy',
    'difference', 'union', 'intersection', 'symmetric_difference',
    'isdisjoint', 'issubset',
]
destructive_func_names = [


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

