# Andrew Zhou
# Calculator Program - Final Project

from datetime import datetime
import math

# ---Methods---

def get_time():
    now = datetime.now()

    if (now.hour > 12) and (now.minute < 10):
        print("The Time is: " + '%s:0%s' % (abs(now.hour - 12), now.minute) + ' PM,' + ' %s/%s/%s' % (now.month, now.day, now.year))
    elif (now.hour > 12) and (now.minute > 10):
        print("The Time is: " + '%s:%s' % (abs(now.hour - 12), now.minute) + ' PM,' + ' %s/%s/%s' % (now.month, now.day, now.year))
    elif (now.hour < 12) and (now.minute < 10):
        print("The Time is: " + '%s:0%s' % (abs(now.hour), now.minute) + ' AM,' + ' %s/%s/%s' % (now.month, now.day, now.year))
    else:
        print("The Time is: " + '%s:%s' % (abs(now.hour), now.minute) + ' AM,' + ' %s/%s/%s' % (now.month, now.day, now.year))

    print("")

def addition(num1, num2):
    return num1 + num2

def subtraction(num1, num2):
    return num1 - num2

def multiplication(num1, num2):
    return num1 * num2

def division(dividend, divisor):
    return float(dividend / divisor)

def int_division(dividend, divisor):
    return int(dividend // divisor)

def modular(num, mod):
    return num % mod

def exponential(num, exponent):
    i = 0
    final = num
    if exponent == 1:
        return num
    elif exponent == 0:
        return 1
    else:
        while i < exponent - 1:
            final *= num
            i += 1
        return final

def square_root(num):
    return math.sqrt(num)

# Area Formulas

def area_quad(length, height):
    if length == height:
        return exponential(length, 2)
    else:
        return length * height

def area_quad_diag(diag1, diag2):
    return (diag1 * diag2) / 2

def area_triangle(base, height):
    return (base * height) / 2

def area_trapezoid(base1, base2, height):
    bases = base1 + base2
    return (bases * height) / 2

def area_circle(radius):
    return math.pi * exponential(radius, 2)

# Special Formulas

def circ_circle(length, diam_check):
    if diam_check:
        return math.pi * length
    elif not diam_check:
        return (math.pi * length) * 2

# Interactive Methods

def calculator(op):
    if op == "a":
        num1 = float(input("Please input the first number: "))
        num2 = float(input("Please input the second number: "))
        print(addition(num1, num2))
    elif op == "s":
        num1 = float(input("Please input the first number: "))
        num2 = float(input("Please input the second number: "))
        print(subtraction(num1, num2))
    elif op == "m":
        num1 = float(input("Please input the first number: "))
        num2 = float(input("Please input the second number: "))
        print(multiplication(num1, num2))
    elif op == "d":
        num1 = float(input("Please input the dividend: "))
        num2 = float(input("Please input the divisor: "))
        print(division(num1, num2))
    elif op == "id":
        num1 = float(input("Please input the dividend: "))
        num2 = float(input("Please input the divisor: "))
        print(int_division(num1, num2))
    elif op == "mod":
        num1 = int(input("Please input the number: "))
        num2 = int(input("Please input the mod: "))
        print(modular(num1, num2))
    elif op == "sq":
        num = float(input("Please input the dividend: "))
        print(square_root(num))

    # Special Formulas

    elif op == "circum":
        print("Are you using the diameter? (type 'y' or 'n')")
        check = input()

        if check == "y":
            num = float(input("Please input the diameter: "))
            print(circ_circle(num, True))
        elif check == "n":
            num = float(input("Please input the radius: "))
            print(circ_circle(num, False))
        else:
            print("ERROR: invalid input")
            calculator("circum")

    # Area Formulas

    elif op == "quad":
        num1 = float(input("Please input the length: "))
        num2 = float(input("Please input the height: "))
        print(area_quad(num1, num2))
    elif op == "quadd":
        num1 = float(input("Please input the first diagonal: "))
        num2 = float(input("Please input the second diagonal: "))
        print(area_quad_diag(num1, num2))
    elif op == "tri":
        num1 = float(input("Please input the base length: "))
        num2 = float(input("Please input the height: "))
        print(area_triangle(num1, num2))
    elif op == "trap":
        num1 = float(input("Please input the first base: "))
        num2 = float(input("Please input the second base: "))
        num3 = float(input("Please input the height: "))
        print(area_trapezoid(num1, num2, num3))
    elif op == "circ":
        num1 = float(input("Please input the radius: "))
        print(area_circle(num1))
    else:
        print("ERROR: invalid input")

def user_input():
    print("LIST OF OPERATIONS:\n")
    print("MATHEMATICAL OPERATIONS")
    print(" a: Addition\n s: Subtraction\n m: Multiplication\n d: Division\n id: Integer Division\n mod: Modular Arithmetic\n sq: Square Root\n")
    print("SPECIAL FORMULAS")
    print(" circum: Circle - Circumference \n")
    print("AREA FORMULAS")
    print(" quad: Quadrilateral Area (no Trapezoids)\n quadd: Square and Rhombus Diagonal Area\n tri: Triangle Area\n trap: Trapezoid Area\n circ: Circle - Area\n")

    user = input("Please choose a mathematical operation: ")
    calculator(user)

def restart():
    print("Do you want to restart the calculator? (type 'y' or 'n')")
    restart_check = input()

    if restart_check == "y":
        print("\t------CALCULATOR------\n")
        get_time()
        user_input()
        restart()
        
    else:
        print("Thank you for using the PyCalculator!")

# ---Main Code---

print("\t------CALCULATOR------\n")

get_time()

user_input()

restart()
