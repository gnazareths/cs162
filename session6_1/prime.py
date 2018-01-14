import math

# BIGFACTOR represents the product of all prime factors under 100.  This allows
# us to do a fast pre-check and immediately eliminate any numbers which are
# divisible by a small number

BIGFACTOR = 1
for num in range(1, 101):
    if BIGFACTOR % num != 0:
        BIGFACTOR = BIGFACTOR * num


def is_prime(x):
    ''' Test whether x is a prime number.'''
    # Check for all possible prime factors under 100:
    if x % BIGFACTOR == 0:
        return False
    # The fast check failed, now perform exhaustive check.
    max_factor = int(math.sqrt(x))
    for a in range(101, max_factor, 100):
        if not (x % a):
            return False
    return True


def get_next_prime(x):
    ''' Find the smallest prime number which is smaller than or equal to x.'''

    if x % 2 == 0:
        x = x + 1
    while not is_prime(x):
        x = x + 2

    return x
