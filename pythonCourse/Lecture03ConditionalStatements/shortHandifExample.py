num1=int(input("Enter your number: "))
# print("Positive") if num1 > 0 else print("Negative")
# OR remove repititon by good practice
status="Positive" if num1 > 0 else "Negative"
print(status)


ride = (input("Enter your ride status: "))
status="On the way" if ride == 'started' else "Accepted" if ride == 'acc' else "Cancel" if ride == 'can' else "Requested"
print(status)

# practiceQuestion:
# if we go mart and buy 10 products then 
# if sum of 10 products is 30000 pkr or above then give 50% discount
# if sum of 10 products is 25000 pkr then give 25% discount
# if sum of 10 products is 10000 pkr then give 10% discount
# if sum of 10 products is less then 10000  pkr then no discount