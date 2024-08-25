while True:
    print("enter your first number:")
    n=int(input())
    print("enter your second number")
    p=int(input())
    print("enter the operation to these numbers")
    a=input()
    if a=='+':
        print("the addition of two number is:",n+p)
    elif a=='-':
        if n>p:
            print("the subtration of two number is ",n-p)
        else:
            print("the subtraction of two number is",p-n)
    elif a=='*':
        print("the multiplication of two numbers is:",p*n)
    elif a=='/':
        print("the division of two numbers is:",n/p)
    else:
        print("invalid operation")
    print("if you want to stop  type yes otherwise no")
    f=input()
    if f=="yes":
        print("thanks for used the calculator")
        break
