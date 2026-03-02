#02/23/26

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
'''age = int(input("Enter your age: "))
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
    print("You are an adult")'''
    

#03/2/26

#example 1

'''num = -67 
result = "Positive" if  num > 0 else "False"

print(f"result:{result}")'''

#example 2
'''numberOne = int(input("Enter a number: "))
numberTwo= int(input("Enter a second number: "))

result = numberOne if numberOne < numberTwo else numberTwo

print(f"{result}")'''

#example 3

''' 
len()=find
find=find
rfind=reverse find
capitalize()=Capitalization
upper()=uppercase
lower()=lowercase
isdigit()=check if its a digit
isalpha=check if its an alphanumeric
count()=count how many characters
replace()=replacea character with a  different character
'''

#text = input("Enter a word:")
#resykt - len(text)
#result = text.find("p")
#result = text.rfind("p")
#result = text.capitalize()
#result = text.upper()
#result = text.lower()
#result = text.isdigit()
#result = text.isalpha()
#result = text.count("b")
#result = text.replace("WAH", "WAWAAWA")
#print(result)
#print(f"Total characters for text is: {len(text)}")

#userName = input ("Enter a username: ")

#userName.isalpha()
#userName.find(" ")
#userName.count(userName)

#if len(userName) <= 12 and userName.find(" ") == -1 and userName.isalpha() == True:
    #print("Username is valid")

'''if len(userName) > 12:
    print("Username is too long")

elif not userName.find(" ") == -1:
    print("Username cannot contain spaces")

elif not userName.isalpha() == True:
    print("Username must be alphanumeric")
else:
    print("Username is valid") '''    
    

#Example 4

#text = "College of innovation and integrated technology"

#char = text[::2]
#print(char)

ccnum = "1267-2546-7674-9672"

ccnum1 = ccnum[15:]
print(f"Credit card number: xxxx-xxxx-xxxx-{ccnum1}")

rchar = ccnum[18::-1]
print(f"Credit card number in reverse: {rchar}")

