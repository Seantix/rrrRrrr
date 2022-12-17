"""Вывод n-ого элемента последовательности числа Фибоначчи"""

import itertools
from typeguard import typechecked


class Fib:
    """По объектам этого класса можно итерироваться
       и получать числа Фибоначчи"""

    class FibIter:
        """Внутренний класс — итератор"""

        @typechecked
        def __init__(self) -> None:
            self.i: int = 0
            self.prev1 = self.prev2 = 1

        @typechecked
        def __next__(self) -> int:
            if self.i > 1:
                self.prev2 += self.prev1
                self.prev2, self.prev1 = self.prev1, self.prev2
                self.i += 1
                return self.prev1
            else:
                self.i += 1
                return 1

    def __iter__(self):
        """Создать и вернуть итератор"""
        return Fib.FibIter()


f_inf: Fib = Fib()

fib_amount: int = int(input('Введите количество членов последовательности Фибоначчи:'))
assert fib_amount > 0, 'Введите положительное число!'

for i, f in zip(
    itertools.count(1),
    itertools.islice(f_inf, fib_amount)
):
    print(i, f)
