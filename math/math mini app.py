import math
from math_utils import *

def line():
    print("=" * 40)

while True:
    line()
    print("🧮 MATH MINI APP")
    line()
    print("1. Square Root")
    print("2. Factorial")
    print("3. Power")
    print("4. GCD")
    print("5. LCM")
    print("6. Log")
    print("7. Trigonometry")
    print("8. Distance")
    print("9. Exit")
    line()

    choice = input("👉 Enter your choice: ")

    line()

    if choice == "1":
        num = int(input("Enter number: "))
        print("Result:", sqrt_value(num))

    elif choice == "2":
        num = int(input("Enter number: "))
        print("Result:", factorial_value(num))

    elif choice == "3":
        a = int(input("Enter base: "))
        b = int(input("Enter power: "))
        print("Result:", power(a, b))

    elif choice == "4":
        a = int(input("Enter first number: "))
        b = int(input("Enter second number: "))
        print("GCD:", gcd_value(a, b))

    elif choice == "5":
        a = int(input("Enter first number: "))
        b = int(input("Enter second number: "))
        print("LCM:", lcm_value(a, b))

    elif choice == "6":
        num = int(input("Enter number: "))
        print("Log:", log_value(num))

    elif choice == "7":
        angle = int(input("Enter angle in degrees: "))
        print("Sin:", sin_value(angle))
        print("Cos:", cos_value(angle))
        print("Tan:", tan_value(angle))

    elif choice == "8":
        x1 = int(input("x1: "))
        y1 = int(input("y1: "))
        x2 = int(input("x2: "))
        y2 = int(input("y2: "))
        print("Distance:", distance_between_points([x1, y1], [x2, y2]))

    elif choice == "9":
        print("🚪 Exiting...")
        break

    else:
        print("❌ Invalid choice")

    input("\nPress Enter to continue...")