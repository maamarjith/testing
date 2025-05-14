print ("Hi User! Welcome Back")
print("Let us create some sample project")
print("Simple Calculator")



choice = int(input("1 for addition, 2 for multiplication,3 for substraction & 0 for exit "))
while(True):
    if choice ==1:
        num1 = int(input("Enter the value: "))
        num2 = int(input("Enter the value: "))
        print(f"Sum of {num1} + {num2} = {num1+num2}")
    elif choice == 2:
        num1 = int(input("Enter the value: "))
        num2 = int(input("Enter the value: "))
        print(f"Sum of {num1} * {num2} = {num1*num2}")
    elif choice == 3:
        num1 = int(input("Enter the value: "))
        num2 = int(input("Enter the value: "))
        print(f"Sum of {num1} - {num2} = {num1-num2}")
    elif choice == 0:
       print("Bye, see you again")
       break
    else:
        print("Invalid input, Please try again")

