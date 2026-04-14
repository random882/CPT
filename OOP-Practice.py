# It starts by defining a class called PersonalInformation which defines the way objects are created from that class.
# Address, age, phone, and name are the attributes created and the instances of persons  act as the object of which these attributes are attached to. PersonalInformation acts as a ' blueprint ' and says that every object of that class will contain
# a name, address, age, and phone. Functions are then made to handle the information of the class, set_name and it's sister functions are all used to directly control how the data within the object are changed. (encapsulation)
# The set functions modify the Data within the object for example self.__name = name would make whatever value name is at the time the function is ran would be what __name is,
# The get functions are used to then retrieve the data stored inside of the object, the program flows in a pretty standard way.
# User enters their information -> functions directly store the data inside of the object -> get functions then retrieve this data which is then printed by the program

# Variables used for input:
# name, address, age, phone
# Output Data: 
# name, address, age, phone number
# Processing:
# The program processes data by creation objects of the PersonalInformation class storing the inputs of the user within the objects attributes using the set functions. The store data is then later display through the use of the get functions. 

class PersonalInformation:
    def __init__(self, name="",address="",age="",phone=""):
        self.__name = name
        self.__address = address
        self.__age = age
        self.__phone = phone

# //: Sets :\\ # 

    def set_name(self, name):
        self.__name = name

    def set_address(self, address):
        self.__address = address

    def set_age(self, age):
        self.__age = age

    def set_phone(self, phone):
        self.__phone = phone


    # //: Gets :\\ # 

    def get_name(self):
        return self.__name

    def get_address(self):
        return self.__address

    def get_age(self):
        return self.__age

    def get_phone(self):
        return self.__phone

def main():
    people = []

    for i in range(3):
        print("enter information for person", i + 1)
        name = input("Enter name: ")
        address = input("Enter address: ")
        age = input("Enter age: ")
        phone = input("Enter phone: ")
    
        person = PersonalInformation()
        person.set_name(name)
        person.set_address(address)
        person.set_age(age)
        person.set_phone(phone)

        people.append(person)
        print()

    # //: Output :\\ #
    print("\nPersonal Information Entered:\n")

    for i in range(3):
        person = people[i]
        print("Person", i + 1)
        print("name:", person.get_name())
        print("Address:", person.get_address())
        print("Age:", person.get_age())
        print("Phone Number:", person.get_phone())
        print()

main()