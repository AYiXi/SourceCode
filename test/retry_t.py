import types

from tenacity import retry, TryAgain
import sys

print(sys.stdin)


@retry
def f():
    print(__name__)
    raise TryAgain('try again')


a = lambda i: i + 1
print(isinstance(f, types.FunctionType))
print(isinstance(print, types.BuiltinMethodType))

if __name__ == "__main__":
    pass
    # f()
