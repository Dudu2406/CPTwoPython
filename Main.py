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

'''ccnum = "1267-2546-7674-9672"

ccnum1 = ccnum[15:]
print(f"Credit card number: xxxx-xxxx-xxxx-{ccnum1}")

rchar = ccnum[18::-1]
print(f"Credit card number in reverse: {rchar}")'''


#03/09/26

#Example 1

'''username = input("Enter a username: ")

while username == "":
    print("you didn't put your username")
    username = input("Enter a username: ")
    
print(f"Welcome {username}!!")''' 

'''number = int(input("Enter a number: "))

while number < 1 or number >20:
    if number < 1:
        print("Number should not be lower than 1")
        number = int(input("Enter a number: "))
    elif number > 20:
        print("Number should not be higher than 20")
        number = int(input("Enter a number: "))
        
print(f"Number is {number}")'''

'''favfood = input("Enter your favourite food(enter q to quit): ")

while not favfood =="q":
    print(f"your favourite food is {favfood}")
    favfood = input("Enter your favourite food(enter q to quit): ")

print("thank you for giving your favourite food")'''


'''for x in range (1,10):
    if x == 5:
        continue
    else:
        print(x, end="")'''
        
'''Fruits = ["Apple","Orange","Banana","Coconut"]
Fruits.append("pineapple")'''

#list on a loop
'''index = 0
while index <len(Fruits):
    print(Fruits[index])
    index += 1'''
    
'''for x in Fruits:
    print(f"Fruits: {Fruits}")'''
    
#Functions example:

'''def addition(num1, num2):
    sum = num1 + num2
    print (sum)
    
addition(50, 50)'''

'''def info(Name, Age, Country):
    print(Name)
    print(Age)
    print(Country)

info("Bogart", 15, "America")'''

class Student:
    
    student_count = 0
    total_GPA = 0
    
    def __init__(self, name, course, GPA):
        self.name = name
        self.course = course
        self.GPA = GPA
        Student.student_count += 1
        Student.total_GPA += GPA
        
        
    def get_data(self):
        print(f"My name is {self.name}")
        print(f"My Course is {self.course}")
        print(f"My GPA is {self.GPA}")
        
    '''@staticmethod
    def is_valid_course(course):
        valid_course = ["BSIS","BSCS","BSEMC"]
        for x in valid_course:
            if x == course:
                print("Course is valid")'''
                
    @classmethod
    def get_average_GPA(cls):
        ave = cls.total_GPA/ cls.student_count
        print(f"Average GPA of all students is {ave}")
        

        
student1 = Student("John", "BSIS", 3.8)
student2 = Student("Bogart", "BSCS", 5.5)
student3 = Student("Carl", "BSEMC", 2.8)

#\print(f"Student's name is {student1.name}, his course is {student1.course}, and his GPA is: {student1.GPA}")

#Student.is_valid_course(student1.course)



'''Student1 = Student("Bogart", "BSCS", 2.8)
Student1.get_data()
Student2= Student("Burat", "BSIT", 4.0)
Student2.get_data()'''