import random

# Hello world
print("Hello world!")

# Variables
x = 1
f = 4.5
name = "ALS"
in_class = True

# Random
print(random.randint(1, 10))

# Types
print(type(x))
print(type(f))
print(type(name))
print(type(in_class))

int(True)  # bool to int
float(True)  # bool to float
str(True)  # bool to string

bool(1)  # int to bool
float(22)  # int to float
str(33)  # int to string

bool(1.0)  # float to bool
int(5.9)  # float to int, return 5
round(5.9)  # float to int, return 6
str(5.9)  # float to string

bool("hola")  # string to bool, return True
bool("")  # string to bool, return False
int("22")  # string to int
float("22.6")  # string to float

# Decisions
if x > 0:
    print(f"x is positive: {x=}")
elif x == 0:
    print(f"x is zero: {x=}")
else:
    print(f"x is negative: {x=}")

# Loops
# range([lim inf], lim sup, [increment])
for i in range(10):  # [1, 10)
    print(i)

while x < 10:
    x += 1
    print(x)

# Exercise 1: Fibonacci
a, b = 0, 1
for i in range(10):
    print(a)
    a, b = b, a + b

# Exercise 2: FizzBuzz
for i in range(1, 41):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)
