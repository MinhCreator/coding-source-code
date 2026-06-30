from fractions import Fraction
x4 = 0.12
x3 = 27/121 + 3/7*x4
x2 = -(19/4) + 5/4*x3 - 13/4*x4
x1 = 9/4 - 3/4*x3 - 1/4*x4
print(Fraction(x1), Fraction(x2), Fraction(x3), Fraction(x4))