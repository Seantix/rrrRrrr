# программа решает СЛУ методом Гаусса и выдает решения

from package.gauss import *

# массивы записываем через array, чтобы numpy был доволен

a = array([                                                   
    [1.5, 2.0, 1.5, 2.0],
    [3.0, 2.0, 4.0, 1.0],
    [1.0, 6.0, 0.0, 4.0],
    [2.0, 1.0, 4.0, 3.0]
], dtype=float)

b = array([5, 6, 7, 8], dtype=float) 

solution = vector_gauss(a, b)

print(solution)
