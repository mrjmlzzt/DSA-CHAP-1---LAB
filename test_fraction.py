from fraction import Fraction

# Test 1
f1 = Fraction(2, 4)
if str(f1) == "1/2":
    print("pass Fraction(2, 4) stored simplified got 1/2")
else:
    print("fail Fraction(2, 4)")

# Test 2
f2 = Fraction(6, 8)
if str(f2) == "3/4":
    print("pass Fraction(6, 8) stored simplified got 3/4")
else:
    print("fail Fraction(6, 8)")

# Test 3: zero denominator
try:
    Fraction(1, 0)
    print("fail zero denominator was accepted")
except ValueError:
    print("pass zero denominator got refused")