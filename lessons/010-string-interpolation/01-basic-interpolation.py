"""
s - string
d and i - int
f - float
x and X - hexadecimal (ABCDEF0123456789)
"""

name = "Alex"
heigth = 1.78
weigth = 68.500

interpolation="%s is %.2fm tall and wheigths %.2fkg" % (name, heigth, weigth)

print(interpolation)

number = 10

print("The hexadecimal of %d is %04x" % (number, number))
print("The hexadecimal of %d is %04X" % (number, number))