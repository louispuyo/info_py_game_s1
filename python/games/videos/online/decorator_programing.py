

def stargaze(func):
    def inner(*args, **kwargs):
        print(f"function {func.__name__} is called ...")
        print(30*">")
        # print()
        print(func(*args, **kwargs))
        # print()
        print("<<<<<<<<<<<<<")
    return inner

def preatier(func):
    def inner(*args, **kwargs):
        print(f"function {func.__name__} is called ...")
        print(30*"*")
        print()
        print(func(*args, **kwargs))
        print()
        print("end ...")
    return inner

@stargaze
@preatier
def simple(arg):
    return arg


# simple(10)
# eval
# 


print(__file__)
