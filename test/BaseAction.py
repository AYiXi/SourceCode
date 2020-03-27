class BaseAction(object):
    """Base class for representing actions to take by retry object.

    Concrete implementations must define:
    - __init__: to initialize all necessary fields
    - REPR_ATTRS: class variable specifying attributes to include in repr(self)
    - NAME: for identification in retry object methods and callbacks
    """
    a = 1
    b = 2
    REPR_FIELDS = ('a', 'b')
    NAME = None

    def __repr__(self):
        state_str = ', '.join('%s=%r' % (field, getattr(self, field)) for field in self.REPR_FIELDS)
        return '%s(%s)' % (type(self).__name__, state_str)

    def __str__(self):
        print(self.__class__)
        return repr(self)

    def __exit__(self, exc_type, exc_val, exc_tb):
        pass



if __name__ == '__main__':
    ba = BaseAction()
    print(ba)
