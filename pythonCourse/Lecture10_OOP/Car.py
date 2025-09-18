# Defining the 'Car' class
class Car:
    # Class attributes (shared by all instances of the class)
    name = "Suzuki"  # The name of the car
    model = "Alto"   # The model of the car

    # Defining a method 'runstop' within the class
    def runstop(self):
        # 'self' refers to the current instance of the class
        print("bhai yeh function kee andaar hai ", self)
        print("car is starting ")

# Creating an object (instance) of the Car class
obj1 = Car()

# Printing the object itself, which will show the memory location unless __str__() is defined
print(obj1)  # Output: <__main__.Car object at some_memory_location>

# Accessing the class attributes via the object
print(obj1.name)  # Output: Suzuki
print(obj1.model)  # Output: Alto

# Calling the 'runstop' method on the object
obj1.runstop()  # Output: bhai yeh function kee andaar hai <__main__.Car object at memory_location>
                #         car is starting 
