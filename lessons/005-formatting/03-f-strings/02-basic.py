"""
d - int
f - float
	.<number of digits>f
x or X - hexadecimal
(character)(><^)(quantity)
> - left
< - rigth
^ - center
sign - + or -
Ex.: 0>-100,.1f
conversion flags - !r !s !a
"""

text = "ABC"
print(f"{text}")

# lpad
print(f"{text: >10}")
# rpad
print(f"{text: <10}")
# cpad
print(f"{text: ^10}")
# repr
print(f"{text!r}")

number_pi = 3.141592

print(f"{number_pi}")
print(f"{number_pi:.2f}")
print(f"{number_pi:.2f}")

number_hexa = 10

print(f"The hexadecimal of {number_hexa} is {number_hexa:04X}")