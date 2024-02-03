#1.	შექმენი კლასი რომელსაც ექნება public, protected და private პარამეტრები.
#  გამოიყენე @property დეკორატორი და ასევე შექმენი setter და  getter
#  დეკორატორებიანი ფუნქციები პარამეტრებზე წვდომისა და რედაქტირებისთვის
class Person:
    def __init__(self, name, age):
        self._protected_age = age  # 
        self.__private_name = name  
    @property
    def private_name(self):
        return self.__private_name
    @property
    def protected_age(self):
        return self._protected_age

    # Setter 
    @protected_age.setter
    def protected_age(self, new_age):
        assert new_age > 0,  " age must be positive"
        self._protected_age = new_age

    # Deleter for private_name
    @private_name.deleter
    def private_name(self):
        print(f"Deleting private_name for {self.__private_name}")
        del self.__private_name

person = Person("John", 30)
print("Public attribute (name):", person.private_name)
print("Protected attribute (age):", person.protected_age)

# Using  setter
person.protected_age = 25
print("Updated protected attribute (age):", person.protected_age)

del person.private_name

#2 ნაწილი
class ChildPerson(Person):
    def __init__(self, name, age, school):
        super().__init__(name, age)
        self.school = school

    def display_info(self):
        print(f"Name: {self.private_name}, Age: {self.protected_age}, School: {self.school}")

child = ChildPerson(name="Alice", age=10, school="ABC School")


print("Public attribute (name):", child.private_name)
print("Protected attribute (age):", child.protected_age)
print("New attribute (school):", child.school)
child.display_info()

