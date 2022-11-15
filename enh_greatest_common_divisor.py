from math import floor

def evklid_enhanced(a_num, b_num):
    """
    Расширенный алгоритм Евклида для 2 чисел
    """
    if a_num == 0:
        x = 0
        y = 1
        return [x, y]
    else:
        d = evklid_enhanced(b_num % a_num, a_num)
        x = d[1] - floor(b_num/a_num) * d[0]
        y = d[0]
        return [x, y]


c, d = int(input()), int(input())
solve = evklid_enhanced(c, d)
gcd = c*solve[0] + d*solve[1]
print(str(solve[0]) + ' * ' + str(c) + ' + ' + str(solve[1]) + ' * ' + str(d) + ' = ' + str(solve[0]*c + solve[1]*d))
