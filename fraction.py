from math import gcd

class Fraction:
    """A fraction kept in simplified form."""

    def __init__(self, numerator, denominator):
        if denominator == 0:
             raise ValueError('denominator cannot be zero')

        common = gcd(numerator, denominator)
        self._numerator = numerator // common
        self._denominator = denominator // common

    def add(self, other):
        n = self._numerator * other._denominator + other._numerator * self._denominator
        d = self._denominator * other._denominator
        return Fraction(n, d)

    def __str__(self):
        return f"{self._numerator}/{self._denominator}"