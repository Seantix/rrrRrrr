
def evklid(a_num, b_num):
    """
    Алгоритм Евклида для двух чисел
    """
    if b_num == 0:
        return a_num
    else:
        return evklid(b_num, a_num % b_num)


c, d = int(input()), int(input())
print('GCD(', c, ',', d, ') = ', evklid(c, d))
