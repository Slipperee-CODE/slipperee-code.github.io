def digit_distance(n):
    """Determines the digit distance of n.

    >>> digit_distance(3)
    0
    >>> digit_distance(777) # 0 + 0
    0
    >>> digit_distance(314) # 2 + 3
    5
    >>> digit_distance(31415926535) # 2 + 3 + 3 + 4 + ... + 2
    32
    """
    if n // 10 == 0:
        return 0

    distance = abs(n % 10 - n % 100 // 10)

    distance += digit_distance(n // 10)
    return distance