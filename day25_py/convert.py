# Written to be run by pytest

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

def toSnafu(n):
    "Converts n (decimal) to a SNAFU string."

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

