from functools import wraps

def unlocked(func):
    @wraps(func)
    def f(self, *args, **kwargs):
        if self._lock:
            raise EnvironmentError('%s is locked' % repr(self))
        return func(self, *args, **kwargs)
    return f

class Kfij:
    '''
    Persist objects of an existing class to a file. It is safe to access the same
    instance from multiple threads. It is unsafe to get any more concurrent than that.

    Use the enable_safe_funcs and enable_destructive_funcs to stupidly copy methods
    from the class that you are persisting. The safe functions should not update the
    present object. The destructive functions should update the present object, and
    they rewrite the entire corresponding file every time they are called.

    You probably don't need to rewrite the entire file every time, so you should
    write your own versions of functions that don't need to do this.
    '''
    @unlocked
    def __init__(self, filename, *args, **kwargs):
        '''
        If the filename exists, *args and **kwargs must be empty.

        If the filename exists, the new object is populated with the
        data in the file.

        If *args and **kwargs are set, they get passed to self.factory,
        and the result overwrites the contents of the file.

        Either way, updates to the new object flow to the file.

        :param str filename: File at which to save state
        :raises EnvironmentError: If the file already exists and any *args or **kwargs are set
        '''
        self._lock = True

        if os.path.exists(filename) and len(args) + len(kwargs) > 0:
            raise EnvironmentError('If the file already exists, no *args or **kwargs may be set.')

        if os.path.exists(filename):
            with open(filename, 'r') as fp:
                self._cache = self.load(fp)
        else:
            self._cache = self.factory(*args, **kwargs)
            with open(filename, 'w') as fp:
                self.dump(fp)

        self._fp = open(filename, 'a')
        self._lock = False

    @staticmethod
    def factory(*args, **kwargs):
        '''
        You must set the factory equal to the class that the present class is mimicing, such as set or list.
        '''
        raise NotImplementedError('You must set the %s.kfij_factory.', self.__class__.__name__)

    def load(self, fp):
        '''
        This must be a static method that takes a file pointer, parses the format created by
        the dump function, and updates the present object with the data from the file. Assume
        that the present object is empty before load is called.
        '''
        raise NotImplementedError('You must set %s.load.', self.__class__.__name__)

    def dump(self, fp):
        '''
        You must set this to the function to a function that serializes the present
        object in a form that the load function can parse.
        '''
        raise NotImplementedError('You must set %s.dump.', self.__class__.__name__)

    @classmethod
    def apply_destructive_funcs(Class, *func_names):
        for func_name in func_names:

            f = getattr(self._cache, func_name)

            @wraps(f)
            @unlocked
            def g(self, *args, **kwargs):
                self._lock = True
                self._fp.close()

                os.remove(self._fp.name)
                f(*args, **kwargs)

                self._fp = open(self._fp.name, 'a')
                self.dump(self._fp)

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
        
class Set(Kfij):
    factory = set
    def load(self, fp):
        for line in fp:
            self.add(line.rstrip('\r\n'))
    def dump(self, fp):
        for x in self:
            fp.write(x + '\n')
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
