def is_sqrt(number):
    x = number
    y = (x + number // x) // 2
    while y < x:
        x = y
        y = (x + number // x) // 2
    return x


def isqrt(n):
    return int(n**.5)


def fermat(n, timeout=False):
    """
    Try Fermat Attack on the input n
    """
    a = is_sqrt(n)
    b2 = a ** 2 - n
    b = isqrt(n)
    count = 0
    while b ** 2 != b2:
        a += 1
        b2 = a ** 2 - n
        b = isqrt(b2)
        count += 1
    p = a + b
    q = a - b
    assert n == p * q
    return p, q
