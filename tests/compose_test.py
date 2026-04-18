from decimal import DivisionByZero
from functools import reduce
from typing import Generator, TypeVar, Generic, Iterable

T = TypeVar("T")


def pipe(*functions):
    def apply(data: Iterable[T] | Generator[T, None, None]):
        return reduce(lambda x, func: func(x), functions, data)

    return apply

def starting_addition(x):
    print(result := x + 10)
    return result

def add(x):

    print(result:= 5 +x)
    return result

def _log(x):
    print(x)
    return x

def divide(x):
    y = 2
    print(result := x/y)
    return result



def comp():
    def _func(x, y):
        return y(x)

    return reduce(_func, (starting_addition, add, _log, divide), -20)


if __name__ == "__main__":
    comp()
