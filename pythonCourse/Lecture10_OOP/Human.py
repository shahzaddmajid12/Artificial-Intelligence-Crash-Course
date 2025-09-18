# Define the base class 'Human'
class Human:
    # Class attributes shared by all humans (instances of Human class)
    brain = True  # Humans have a brain (default value)
    eyes = True   # Humans have eyes (default value)

    # Method to represent the human's ability to speak
    def speak(self):
        print("Speak")

# Define the 'Male' class, which inherits from the 'Human' class
class Male(Human):
    # Additional attribute for Male class
    beard = True  # Males typically have a beard (default value)

# Creating an object (instance) of the Male class
ali = Male()

# Accessing the 'eyes' attribute from the inherited Human class
print(ali.eyes)  # Output: True (because 'Male' inherits from 'Human' and has 'eyes' as True)
