class Counter:
    def __init__(self, func):
        self.func = func
        self.count = 0

    def __call__(self, *args, **kwargs):
        self.count += 1
        return self.func(*args, **kwargs)

# foo = Counter(foo)
# foo()

# Counter(foo)()


@Counter
def foo(a):
    return a


for i in range(10):
    foo(1)

print(type(foo).__name__)
print(foo.count)  # 10


from tenacity import wait_fixed
print(wait_fixed)