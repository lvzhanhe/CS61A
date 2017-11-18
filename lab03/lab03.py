"""Lab 3: Recursion and Tree Recursion"""


# Q1
def ab_plus_c(a, b, c):
    """Computes a * b + c.

    >>> ab_plus_c(2, 4, 3)  # 2 * 4 + 3
    11
    >>> ab_plus_c(0, 3, 2)  # 0 * 3 + 2
    2
    >>> ab_plus_c(3, 0, 2)  # 3 * 0 + 2
    2
    """
    if b == 0:
        return c
    return a + ab_plus_c(a, b - 1, c)


# Q2
def gcd(a, b):
    """Returns the greatest common divisor of a and b.
    Should be implemented using recursion.

    >>> gcd(34, 19)
    1
    >>> gcd(39, 91)
    13
    >>> gcd(20, 30)
    10
    >>> gcd(40, 40)
    40
    """
    a, b = max(a, b), min(a, b)
    if a % b == 0:
        return b
    else:
        return gcd(b, a % b)


# Q3
def hailstone(n):
    """Print out the hailstone sequence starting at n, and return the
    number of elements in the sequence.

    >>> a = hailstone(10)
    10
    5
    16
    8
    4
    2
    1
    >>> a
    7
    notes:
    n / 2 will return a float, while n // 2 will return a integer
    """
    if n == 1:
        print(1)
        return 1
    if n % 2 == 0:
        print(n)
        return 1 + hailstone(n // 2)
    else:
        print(n)
        return 1 + hailstone(3 * n + 1)
