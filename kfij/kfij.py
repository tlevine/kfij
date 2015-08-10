from functools import wraps

class Kfij:
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

    @classmethod
    def set_appender(Class, func_name):
        Class._kfij_appender = func_name

    @classmethod
    def apply_destructive_funcs(Class, *func_names):
        getattr(self._set)
        os.remove
        close fp

    @classmethod
    def apply_safe_func(Class, *func_names):
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

