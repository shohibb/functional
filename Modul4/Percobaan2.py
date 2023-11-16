def uppercase_decorator(function):
    def wrapper():
        func = function()
        return func.upper()

    return wrapper


def say_hi():
    return "hy there"


decorate = uppercase_decorator(say_hi)
print(decorate())
