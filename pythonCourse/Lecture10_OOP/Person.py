# Defining a class named 'Person'
class Person:
    # Class attribute (shared by all instances of the class)
    country = "PK"  # Default country is Pakistan ("PK")

    # This is a class method — it can change class-level data
    @classmethod
    def userchange(cls, name):
        # 'cls' refers to the class itself (not an instance)
        # This updates the class attribute 'country'
        cls.country = name

    # This is an instance method — it accesses class/instance data
    def userCountry(self):
        # 'self' refers to the specific object (instance)
        print(self.country)

# Create an instance of the Person class
s = Person()

# Access and print the class attribute directly using the class
print(Person.country)  # Output: PK (initial value of the class attribute)

# Call the class method using the instance 's'
s.userchange("TR")  # This changes the class attribute 'country' to "TR"

# Print the updated class attribute again
print(Person.country)  # Output: TR (value was changed by the class method)
