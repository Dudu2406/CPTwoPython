#Activity question 1

class questionone:
    testdata = [10,15,20,30]
    
    @classmethod
    def run_code(cls):
        print (f"List values: {cls.testdata}")
        
        ave = sum(cls.testdata) / len(cls.testdata)
        print (f"The average of {cls.testdata} is: {ave}")

#Activity  question 2
class person:
    def __init__(self, name, age):
        self.age = age
        self.name = name


class questiontwo:
    def __init__(self):
        self.new_person = []

    def run_code(self):
        self.new_person.append(person("Kurt", 15))
        self.new_person.append(person("Carl", 23))
        self.new_person.append(person("JK", 45))
        self.new_person.append(person("James", 60))
        self.new_person.append(person("Kelvin", 39))
        self.new_person.append(person("Haze", 18))
        self.new_person.append(person("Gaze", 10))
        self.new_person.append(person("Soap", 20))
        self.new_person.append(person("Price", 23))
        self.new_person.append(person("Mcqueen", 80))
        self.new_person.append(person("Bascreveil", 50))
        
        loop_check = 0

        ageinput = int(input("Enter an Age: "))
        print (f"Person with the lower age than {ageinput}:")
        for i in self.new_person:
            if i.age < ageinput:
                print (f"Name: {i.name} Age: {i.age}")
                loop_check += 1
                
#activity question 3
class questionthree:
    def __init__(self, list1, list2):
        self.new_list1 = list1
        self.new_list2 = list2

    def run_code(self):
        print("Test data:")
        self.new_list1 = [1, 20, 3, 6, 8, 9, 10, 7, 12, 21, 18]
        self.new_list2 = [10, 2, 30, 15, 8, 21, 13, 18, 28, 25, 16]
    
        print (f"List 1: {self.new_list1}")
        print (f"List 2: {self.new_list2}")
        print ("All same numbers on both Lists:",)
        for i in self.new_list1:
            if i in self.new_list2:
                print (i)

def activityweekeleven():
    qOne = questionone()
    qOne.run_code()
    qTwo = questiontwo()
    qTwo.run_code()
    qThree = questionthree([], [])
    qThree.run_code()

if __name__ == "__main__":
    activityweekeleven()
    