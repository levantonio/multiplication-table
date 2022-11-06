a = int(input("введите целое число 1 : "))
b = int(input("введите целое число 2 : "))
c = input("введите оператор /,*,-,+ : ")
if c == "/":
    if b == 0:
        print("На ноль делить нельзя!!!!")
    else:
        print(a, '/', b, '=', a/b)
if c == '*':
    print(a, "*", b, '=', a*b )
if c == '+':
    print(a, "+", b, '=', a+b )
if c == '-':
    print(a, "-", b, '=', a-b )