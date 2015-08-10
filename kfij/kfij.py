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
    def factory(*args, **kwargs):
        '''
        You must set the factory equal to the class that the present class is mimicing, such as set or list.
        '''
        raise NotImplementedError('You must set the %s.kfij_factory.', self.__class__.__name__)

    def load_line(self, line):
        '''
        The load_line method should take a string line from a file and update the present
        object accordingly.
        '''
        raise NotImplementedError('You must set the %s.kfij_factory.', self.__class__.__name__)

    def dump(self, fp):
        '''
        You must set this to the function to a function that serializes the present
        object in a form that the load_line function can parse.
        '''
        raise NotImplementedError('You must set the %s.kfij_extend.', self.__class__.__name__)
        for x in self:
            fp.write(x + '\n')

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


