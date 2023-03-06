from numpy import array, concatenate


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

