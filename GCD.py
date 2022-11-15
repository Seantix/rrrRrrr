
def evklid(a, b):
    if b == 0:
        return a
    else:
        return evklid(b, a % b)


a, b = int(input()), int(input())
print('GCD(', a, ',', b, ') = ', evklid(a, b))
