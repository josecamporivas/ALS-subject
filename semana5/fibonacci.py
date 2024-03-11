"""
Crea la función fibonacci utilizando programación dinámica
"""

class Fibonacci:
    def __init__(self):
        self.__cache = {0: [0], 1: [0, 1]}

    def fibonacci(self, n) -> list[int]:
        if n == 0:
            return self.__cache.get(0)

        if n == 1:
            return self.__cache.get(1)

        if n in self.__cache:
            return self.__cache.get(n)

        self.__cache[n] = self.fibonacci(n - 1) + [self.__cache.get(n - 1)[-1] + self.__cache.get(n - 1)[-2]]
        return self.__cache.get(n)

if __name__ == "__main__":
    fib = Fibonacci()
    print(fib.fibonacci(10))
    print(fib.fibonacci(15))
