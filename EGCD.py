from math import floor

def evklid_enhanced(a, b):
    if a == 0:
        x = 0; y = 1
        return [x, y]
    else:
        d = evklid_enhanced(b % a, a)
        x = d[1] - floor(b/a) * d[0]
        y = d[0]
        return [x, y]


a, b = int(input()), int(input())
solve = evklid_enhanced(a, b)
gcd = a*solve[0] + b*solve[1]
print(str(solve[0]) + ' * ' + str(a) + ' + ' + str(solve[1]) + ' * ' + str(b) + ' = ' + str(solve[0]*a + solve[1]*b))

