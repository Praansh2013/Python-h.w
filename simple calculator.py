print("Enter number a and b, I will do operations on them")
def operatations(a,b):
    if choice=="*" or choice=="x":
        print("The product of a and b is: ",a*b)
    elif choice=="/" or choice=="÷":
        print("The division of a and b is: ",a/b)
    elif choice=="-":
        print("The subtract of a and b is: ",a-b)
    elif choice=="+":
        print("The addition of a and b is: ",a+b)

a=int(input("Enter number a: "))
b=int(input("Enter number b: "))
choice=(input("Enter your choice in the sign: "))



operatations(a,b)