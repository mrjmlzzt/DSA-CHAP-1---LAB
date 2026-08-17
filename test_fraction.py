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

    
    
