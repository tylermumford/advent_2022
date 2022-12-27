# Written to be run by pytest

import math
import pytest

class TestConvert:
    def testFirstExample(self):
        d = toDecimal("20")
        assert d == 10

    def testSecondExample(self):
        d = toDecimal("2=")
        assert d == 8

    @pytest.mark.parametrize(
            "s,expect",
            [("2=-01", 976),
             ("1-0---0", 12345),
             ("1121-1110-1=0", 314159265)])
    def testMoreToDecimal(self, s, expect):
        d = toDecimal(s)
        assert expect == d

    def _toSnafuParameters():
        yield (0, "0")
        yield (1, "1")
        yield (2, "2")
        yield (3, "=")
        yield (4, "-")
        yield (5, "10")
        yield (6, "11")
        yield (7, "12")
        yield (8, "2=")
        yield (10, "20")
        yield (25, "100")
        yield (976, "2=-01")
        yield (12345, "1-0---0")
        yield (314159265, "1121-1110-1=0")

    @pytest.mark.parametrize("decimal,expect", _toSnafuParameters())
    def testToSnafu(self, decimal, expect):
        s = toSnafu(decimal)
        assert s == expect, f"Expected {decimal}->'{expect}', but got '{s}'"

def toSnafu(n):
    "Converts n (decimal) to a SNAFU string."

    if n == 0: return "0"

    # digits, as numbers, in order from least significant to most
    digits = []

    # Convert to base 5, with regular digits

    while n:
        count = n % 5
        digits.append(count)
        n = n // 5

    # Convert the digits to SNAFU

    singleDigit = len(digits) == 1
    for i, digit in enumerate(digits):
        if digit in [3, 4, 5] and not singleDigit:
            if i + 1 == len(digits): digits.append(0)
            digits[i + 1] += 1

    symbols = {
            0: 0,
            1: 1,
            2: 2,
            3: "=",
            4: "-",
            5: 0,    # 5 can occur if something carries into a 4
    }

    digits.reverse()
    print(digits)
    digits = [symbols[d] for d in digits]
    digits = [str(d) for d in digits]
    return "".join(digits)

def powersOfFive():
    i = 0
    while True:
        yield 5 ** i


def toDecimal(snafu):
    "Converts a SNAFU string to a number."
    result = 0
    snafu = reversed(snafu)
    for i, digit in enumerate(snafu):
        place = 5 ** i
        if digit == "0": modifier = 0
        if digit == "1": modifier = 1
        if digit == "2": modifier = 2
        if digit == "=": modifier = -2
        if digit == "-": modifier = -1
        result = result + (place * modifier)

    return result

