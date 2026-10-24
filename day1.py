a = float(input())
b = float(input())
operator = input("operator (+, -, *, //, / ):  ")

if operator == "+":
    result = a+b
elif operator == "-":
    result = a-b
elif operator == "//":
    result = a//b
elif operator == "*":
    result = a*b
elif operator == "/":
    if b == 0:
           print("error")
    else:
           print(a/b)
else:
    print("Unknown operator")



