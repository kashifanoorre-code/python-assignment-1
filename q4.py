import sys
integer=32
float1=32.5
complex1=4+5j
boolean=True
string="python"

print(integer)
print(type(integer))
print(float1)
print(type(float1))
print(complex1)
print(type(complex1))
print(boolean)
print(type(boolean))
print(string)
print(type(string))

print(sys.getsizeof(integer))
print(sys.getsizeof(float))
print(sys.getsizeof(complex))
print(sys.getsizeof(boolean))
print(sys.getsizeof(string))

print(complex1.real)
print(complex1.imag)
print(abs(complex1))

# Create two boolean variables
a = True
b = False

# AND operation
print("a and b =", a and b)

# OR operation
print("a or b =", a or b)

# NOT operation
print("not a =", not a)
print("not b =", not b)

num1=2
print(float(num1))
num2=3.78
print(int(num2))
num3='123'
print(int(num3))
num4=True
print(int(num4))
num5=12
print(complex(num5))