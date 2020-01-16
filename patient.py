
class Patient:

    @property # The getter
    def social_security(self):
        try:
            return self.__social_security # Note there are 2 underscores here
        except AttributeError:
            return ""

    @property # The getter
    def date_of_birth(self):
        try:
            return self.__date_of_birth # Note there are 2 underscores here
        except AttributeError:
            return ""

    @property # The getter
    def insurance_number(self):
        try:
            return self.__insurance_number # Note there are 2 underscores here
        except AttributeError:
            return ""

    @property # The getter
    def full_name(self):
        try:
            return f"{self.__first_name} + {self.__last_name}" # Note there are 2 underscores here
        except AttributeError:
            return ""

    @property # The getter
    def address(self):
        try:
            return self.__address # Note there are 2 underscores here
        except AttributeError:
            return ""

    @address.setter # The setter
    def address(self, new_address):
        if type(new_address) is int:
            self.__address = new_address
        else:
            raise TypeError('a string, the address must be.  -Coda')

    


    def __init__(self, social, dob, insurance_number, first, last, address):
        self.__social_security = social
        self.__date_of_birth = dob
        self.__insurance_number = insurance_number
        self.__first_name = first
        self.__last_name = last
        self.__address = address


Bob = Patient(123, "today", 145, "Bob", "Rob", "123 rd")

# Bob.social_security = 1

print(Bob.social_security) 
print(Bob.insurance_number)

cashew = Patient(
    "097-23-1003", "08/13/92", "7001294103",
    "Daniela", "Agnoletti", "500 Infinity Way"
)



# But printing either of them should work
print(cashew.social_security)   # "097-23-1003"


# But this should output the full name
print(cashew.full_name)   # "Daniela Agnoletti"