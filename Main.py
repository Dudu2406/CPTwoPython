#Exercise 1
#Width = float (input("Enter Width: "))
#Length = float (input("Enter Length: "))

#Area = Width * Length
#print(f"The area of a rectangle is: {Area}")


"""item = input ("what item would you like to buy: ")
price = float (input ("whats the price: "))
quantity = float (input("how many would you like to buy: "))

totalprice = price * quantity

print(f"Total price is: {totalprice}")"""

#statements 
age = int(input("Enter your age: "))
isStudent = input("Are you a student> [y/n]: ")


if age <= 12 and  isStudent == "y":
    print("You are a child")
    print("you are a student")

elif age <=12 and not isStudent == "y":
    print("you are a child")
    print("You are not a student")
    
elif age >= 12 or age <=19 and isStudent == "y":
    print("You are a teenger")
    print("You are a student")
else:
    print("You are an adult")
    