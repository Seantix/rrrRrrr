from numpy import array, concatenate
from numpy.linalg import norm
from numpy.linalg import solve as solve_out_of_the_box

a = array([
    [1.5, 2.0, 1.5, 2.0],
    [3.0, 2.0, 4.0, 1.0],
    [1.0, 6.0, 0.0, 4.0],
    [2.0, 1.0, 4.0, 3.0]
], dtype=float)

b = array([5, 6, 7, 8], dtype=float)


def vector_gauss(a, b):
    ab = concatenate((a, array([b]).T), axis=1)
    d = len(ab)

    # прямой

    for i in range(d):
        ab_ii = ab[i, i]
        ab[i] = ab[i] / ab_ii
        for j in range(i+1, d):
            ab[j] = ab[j] - ab[i] * ab[j, i]


    # обратный
    for i in range(d - 1, -1, -1):
        temp_sum = 0
        for j in range(i+1, d):
            temp_sum += ab[j] * ab[i, j]
        ab[i] = ab[i] - temp_sum


    x = ab[:, -1]
    return x



solution = vector_gauss(a, b)
oob_solution = solve_out_of_the_box(a, b)

print(solution)
print("Макс отклонение компоненты решения:", norm(solution-oob_solution, ord=1))
