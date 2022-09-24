try:
    x = int(input("x: "))
    y = int(input("y: "))
except ValueError:
    print("Invalid input.")
    exit(1)

try:
    result = x / y
except ZeroDivisionError:
    print("Error: cannot devide to zero.")
    exit(1)

print(f"result = {result}")
