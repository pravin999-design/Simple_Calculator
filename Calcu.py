a = float(input("Enter the 1st Number To calculate \n"))
b = float(input("Enter The 2nd Number To Calculate\n"))

def Hello():
    print("\n -----------Welcome To Calculator-----------")
    print("Press 1 for Addition")
    print("Press 2 for Subtraction")
    print("Press 3 for Multiplication")
    print("Press 4 for Division")

def Add():
    print("The Addition is =", a + b)

def Sub():
    print("The Subtraction is =", a - b)

def Mul():
    print("The Multiplication is =", a * b)

def Div():
    if b != 0:
        print("The Division is =", a / b)
    else:
        print("Error: Division by zero is not allowed.")

Hello()

while True:
    choice = input("Please Enter The number (1-4)\n")

    if choice == "1":
        Add()
    elif choice == "2":
        Sub()
    elif choice == "3":
        Mul()
    elif choice == "4":
        Div()
    else:
        print("Entered number is Invalid, Please Try Again")
