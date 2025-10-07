calculate = 1 
ops = {"+": (lambda x,y: x+y), "-": (lambda x,y: x-y), "*": (lambda x,y: x*y), "/": (lambda x,y: x/y)}

while calculate != 0:
    num1 = int(input("input first number: "))
    num2 = int(input("input second number: "))
    operator = input("input operator ('*,/,+,-'): ")
    print(ops[operator](num1,num2))
    calculate = int(input("Continue? (0 to stop): "))

    