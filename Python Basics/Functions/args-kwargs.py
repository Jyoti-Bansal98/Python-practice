## *args (multiple arguments)       Jab tumhe pata nahi kitne arguments aayenge
def add(*args):
    print(args)

add(2,43,42,9)    # args = tuple


def sum(*args):
    total = 0

    for num in args:
        total += num
    return total

print(sum(23,244,22))

# use case: Dynamic number of inputs


## **kwargs (keyword arguments)    key-value input handle karta hai
def details(**kwargs):
    print(kwargs)

details(name= 'Jyoti', age= 21)    # kwargs = dictionary

def print_details(**kwargs):
    for key, value in kwargs.items():
        print(key, value)

print_details(name="Aman", age=20)


## combine both
def demo(*args, **kwargs):
    print(args)
    print(kwargs)

demo(1, 2, 3, name="Aman")


