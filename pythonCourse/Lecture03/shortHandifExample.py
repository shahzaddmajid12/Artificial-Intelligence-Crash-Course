num1=int(input("Enter your number: "))
# print("Positive") if num1 > 0 else print("Negative")
# OR remove repititon by good practice
status="Positive" if num1 > 0 else "Negative"
print(status)


ride = (input("Enter your ride status: "))
status="On the way" if ride == 'started' else "Accepted" if ride == 'acc' else "Cancel" if ride == 'can' else "Requested"
print(status)