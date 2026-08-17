from fraction import Fraction

passed = 0
total = 5


def report(number, status, description, detail):
    """Print one result line, aligned in four columns."""
    print(f"{number}. {status:<16}{description:<34}{detail}")


def check(number, description, expected, produce):
    """Run one check and print a single line for it."""
    global passed
    try:
        actual = produce()
    except NotImplementedError as missing:
        report(number, "not written yet", description, str(missing))
        return
    except Exception as error:
        report(number, "ERROR", description, f"{type(error).__name__}: {error}")
        return
    if str(actual) == str(expected):
        passed += 1
        report(number, "pass", description, f"got {actual}")
    else:
        report(number, "FAIL", description, f"expected {expected}, got {actual}")


def rejects_zero_denominator():
    try:
        Fraction(1, 0)
    except ValueError:
        return "refused"
    except NotImplementedError:
        raise
    return "accepted"


check(1, "Fraction(2, 4) stored simplified", "1/2", lambda: Fraction(2, 4))
check(2, "Fraction(6, 8) stored simplified", "3/4", lambda: Fraction(6, 8))
check(3, "1/2 add 1/3", "5/6", lambda: Fraction(2, 4).add(Fraction(1, 3)))
check(4, "1/2 equals 2/4", "True", lambda: Fraction(2, 4) == Fraction(1, 2))
check(5, "zero denominator", "refused", rejects_zero_denominator)

print(f"\n{passed} of {total} checks passing.")