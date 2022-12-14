"""Вывод n-ого элемента последовательности числа Фибоначчи"""

import itertools
from typeguard import typechecked


class Fib:
    """По объектам этого класса можно итерироваться
       и получать 6 чисел Фибоначчи"""

    class FibIter:
        """Внутренний класс — итератор"""

        @typechecked
        def __init__(self) -> None:
            self.i: int = 0
            self.fibs: list[int] = [1, 1]

        @typechecked
        def __next__(self) -> int:
            self.fibs.append(self.fibs[-1] + self.fibs[-2])
            j: int = self.i
            self.i += 1
            return self.fibs[j]

    def __iter__(self):
        """Создать и вернуть итератор"""
        return Fib.FibIter()


f_inf = Fib()

fib_amount = int(input('Введите количество членов последовательности Фибоначчи:'))
assert fib_amount > 0, 'Введите положительное число!'

for i, f in zip(
    itertools.count(1),
    itertools.islice(f_inf, fib_amount)
):
    print(i, f)
