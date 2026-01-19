a = 10
b = 25.5
c = "Python"
d = True

print(a, type(a))
print(b, type(b))
print(c, type(c))
print(d, type(d))

x = 20
y = 5

print("Addition:", x + y)
print("Subtraction:", x - y)
print("Multiplication:", x * y)
print("Division:", x / y)

num1 = input("Enter an integer: ")
num2 = input("Enter a float: ")

try:
    i = int(num1)
    f = float(num2)
    print("Integer value:", i)
    print("Float value:", f)
except:
    print("Invalid input")

value = 100
print(value, type(value))

value = "Hundred"
print(value, type(value))
