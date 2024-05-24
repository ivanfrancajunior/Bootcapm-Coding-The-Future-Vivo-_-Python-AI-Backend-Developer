# variables and data types

import math
students_count = 1000
rating = 4.99
is_published = True
course_name = "Python Programming"
x, y, z = 1, 2, 3

age: int = 20

# print(type(students_count))
print(id(age))


# strings and string methods

title = "Code the Future"
print(len(title))
print(title[0])
print(title[-1])  # last character


# parse from / to index
print(title[0:5])
print(title[:5])
print(title[0:])
print(title[:])

# escape characters
print("I'm a \"Python\" programmer")
print('I\'m a "Python" programmer')
print("I\'m a \"Python\" programmer")

# formatting strings
first = "John"
last = "Doe"
print("Hello, %s %s" % (first, last))
print("Hello, {} {}".format(first, last))
print(f"Hello, {first} {last}")  # most popular

# string methods
message = '  code the future with Vivo'
print(message.upper())
print(message.lower())
print(message.title())
print(message.title().strip())
print(message.find('the'))  # find a index of a string - 9
print(message[6:10])  # slice a string - the
print(message.replace('o', 'x'))
print("Vivo" in message)
print("Vivo" not in message)

# Numbers
ten: int = 10
ten_dot_five: float = 10.5
binary: int = 0b10  # bin(binary)
hexadecimal: int = 0x10  # hex(hexadecimal)
print(ten, ten_dot_five, binary, hexadecimal, sep=' | ')

# Operations
a: int = 10
b: int = 20
print(a + b)
print(a - b)
print(a * b)
print(a / b)  # float
print(a // b)  # int
print(a % b)
print(a ** b)

# number functions
PI = 3.14
print(round(PI))
print(abs(-PI))
print(math.ceil(PI))
print(math.floor(PI))

# type conversion
# a, b = '10', '20'
print(int(a) + int(b))

int(a)
float(b)
bool(a)
str(b)

# Falsy values
bool(None)
bool(False)
bool('')
bool(0)
bool(0.0)
bool([])

# conditional statements
a = 10
b = 20
c = 30
if a < b:
    print("a is less than b")
elif b < c:
    print("b is less than c")
else:
    print("b is greater than c")

# logical operators
name = 'any name'
if not name:  # not operator
    print("name is empty")
else:
    print(name)

age = 20
if age >= 18 and age < 21:  # and operator
    print("You have permission")
else:
    print("Not today buddy")

# ternary operator
message = "You have permission" if age >= 18 and age < 21 else "Not today buddy"
print(message)

# loops (for)
my_list = [1, 2, 3, 4, 5]
for i in my_list:
    print(i * 1.05)

for x in range(5):
    print(x, sep=',')

for y in range(8, 10):
    print(y, sep=',')

for z in range(0, 10, 2):  # step -> sets a interval for the loop (0, 2,4 ... 10)
    print(z, sep=',')

for s in range(10, 0,):
    if s >= 11:
        print(s)
else:
    print("Not found")

# while loop
# guess = 0
# answer = 0
# while guess != answer:
#     guess = int(input("Guess a number: "))
#     if guess > answer:
#         print("Too high")
#     elif guess < answer:
#         print("Too low")
#     else:
#         print("Correct!")


# functions

def increment(number: float, by: int = 1) -> float:
    return number + by


print(increment(2, 3))
print(increment(2))

# args and kwargs


def multyply(*numbers: int) -> int:
    total = 1
    for number in numbers:
        total *= number
    return total


print(multyply(1, 2, 3, 4, 5))


def save_user(**user):
    print(user)


save_user(id='qzyy98745621sdfd1', name="Tatioswalderson", age=3)


def greet(name):
    message_for_greet_fn = 'Good morning!'
    print(f"Hello {name}! {message_for_greet_fn}")


greet("Vivo")

# scopes

works = 'not works'


def works_only_inside():
    if True:
        works = 'works'
    print(works)


works_only_inside()
print(works)

# debugging


def multiply(*numbers):
    total = 1
    for number in numbers:
        total *= number
    return total


print("start")
print(multiply(1, 2, 3))
print("finish")

# fizzbuzz chall


def fizzbuzz(input: int) -> str:
    if input % 3 == 0 and input % 5 == 0:
        return 'FizzBuzz'
    if input % 3 == 0:
        return 'Fizz'
    if input % 5 == 0:
        return 'Buzz'
    return str(input)


print(fizzbuzz(3))
print(fizzbuzz(5))
print(fizzbuzz(6))
print(fizzbuzz(7))
print(fizzbuzz(10))
print(fizzbuzz(15))
print(fizzbuzz(45))
print(fizzbuzz(49))
