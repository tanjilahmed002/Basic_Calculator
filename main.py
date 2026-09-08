from functions import add,sub,mul,div,mod,pow

def calculator():
    num1=float(input("enter your number 1 :"))
    num2=float(input("enter your number 2 :"))
    return num1,num2

while True:
    print("\n===== CALCULATOR =====")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Modulus")
    print("6. Power")
    print("7. Exit")

    option=input("enter your choice :")
    if option == "7":
        print("Exit the Calculator")
        break
    elif option in ["1","2","3","4","5","6"]:
        a,b=calculator()
        if option=="1":
            print("Addition :",add(a,b))
        elif option=="2":
            print("substraction :",sub(a,b))
        elif option=="3":
            print("Multipication :",mul(a,b))
        elif option=="4":
            print("Division :",div(a,b))
        elif option=="5":
            print("Modulus :",mod(a,b))
        elif option=="6":
            print("Power :",pow(a,b))
    else:
        print("invalid choice!try again")

