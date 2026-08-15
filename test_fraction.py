from fraction import Fraction

f1 = Fraction(2, 4)
if str(f1) == "1/2":
    print("pass Fraction(2, 4) stored simplified got 1/2")
else:
    print("fail Fraction(2, 4)")

f2 = Fraction(6, 8)
if str(f2) == "3/4":
    print("pass Fraction(6, 8) stored simplified got 3/4")
else:
    print("fail Fraction(6, 8)")

try:
    Fraction(1, 0)
    print("fail zero denominator was accepted")
except ValueError:
    print("pass zero denominator got refused")

f3 = Fraction(1, 2)
f4 = Fraction(1, 3)
result = f3.add(f4)

if str(result) == "5/6":
    print("pass 1/2 add 1/3 got 5/6")
else:
    print("fail 1/2 add 1/3")
    
    
