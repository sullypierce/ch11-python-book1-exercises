

class Student:

    @property # The getter for first 
    def first_name(self):
        try:
            return self.__first_name # Note there are 2 underscores here
        except AttributeError:
            return ""

    @first_name.setter # The setter for first name
    def first_name(self, new_first_name):
        if type(new_first_name) is str:
            self.__first_name = new_first_name
        else:
            raise TypeError('a string, the name must be.  -Coda')

    @property # The getter
    def last_name(self):
        try:
            return self.__last_name # Note there are 2 underscores here
        except AttributeError:
            return ""

    @last_name.setter # The setter
    def last_name(self, new_last_name):
        if type(new_last_name) is str:
            self.__last_name = new_last_name
        else:
            raise TypeError('a string, the name must be.  -Coda')

    @property # The getter
    def age(self):
        try:
            return self.__age # Note there are 2 underscores here
        except AttributeError:
            return ""

    @age.setter # The setter
    def age(self, new_age):
        if type(new_age) is int:
            self.__age = new_age
        else:
            raise TypeError('an integer, the age must be.  -Coda')

    @property # The getter
    def cohort(self):
        try:
            return self.__cohort # Note there are 2 underscores here
        except AttributeError:
            return ""

    @cohort.setter # The setter
    def cohort(self, new_cohort):
        if type(new_cohort) is int:
            self.__cohort = new_cohort
        else:
            raise TypeError('an integer, the cohort number must be.  -Coda')

    @property # The getter
    def full_name(self):
        try:
            return self.__first_name + " " + self.__last_name # Note there are 2 underscores here
        except AttributeError:
            return ""

    def __str__(self): 
        return f"{self.full_name} is {self.age} and is in Cohort {self.cohort}"

    def __repr__(self):
        return f"name: {self.full_name}, age: {self.age}, Cohort: {self.cohort}"


rob = Student()
rob.first_name = "Rob"
rob.last_name = "Bob"
rob.age = 111 
rob.cohort = 17

print(rob)
print(repr(rob))