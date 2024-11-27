import functools
def decorated(func):
    """
    A decorator that prints a message when a function is called.
    """
    @functools.wraps(func)
    def decorated(num):
        print(f"Calling {func.__name__}")
        return func(num)

    return decorated

@decorated
def data(n):
    """
    A function that returns the square of a number.
    """
    return n ** 2

if __name__ == "__main__":
    inn = int(input("Enter a number: "))
    print(data(inn))