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

    @pytest.mark.parametrize(
            "d,expect",
            [
                (0, "0"),
                (1, "1"),
                (2, "2"),
                (10, "20"),
                (25, "100"),
            ])
           # [("2=-01", 976),
           #  ("1-0---0", 12345),
           #  ("1121-1110-1=0", 314159265)])
    def testToSnafu(self, d, expect):
        s = toSnafu(d)
        assert expect == s

def toSnafu(n):
    "Converts n (decimal) to a SNAFU string."
    if n == 0:
        return "0"

    tokens = []
    exponent = math.floor(math.log(n, 5))
    descending = range(exponent, -1, -1)
    divisors = [5 ** x for x in descending]

    for divisor in divisors:
        count, remain = divmod(n, divisor)
        print(f"{n} // {divisor} -> {count}, {remain}")
        if count > 0:
            tokens.append(str(count))
        else:
            tokens.append(str(remain))
            #break

        n = remain

        print(tokens)

    return "".join(tokens)


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

