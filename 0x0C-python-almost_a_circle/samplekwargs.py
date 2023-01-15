def myfunc(*args, **kwargs):
    for key, value in kwargs.items():
        print(key, ":", value)


# x = None
# height = None
# y = None
# width = None
myfunc(x=1, height=2, y=3, width=5)
