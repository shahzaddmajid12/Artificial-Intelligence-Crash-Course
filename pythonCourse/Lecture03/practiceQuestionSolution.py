# practiceQuestion:
# if we go mart and buy 10 products then 
# if sum of 10 products is 30000 pkr or above then give 50% discount
# if sum of 10 products is 25000 pkr then give 25% discount
# if sum of 10 products is 10000 pkr then give 10% discount
# if sum of 10 products is less then 10000  pkr then no discount

item1=float(input("Enter Item1 Price: "))
item2=float(input("Enter Item2 Price: "))
item3=float(input("Enter Item3 Price: "))
item4=float(input("Enter Item4 Price: "))
item5=float(input("Enter Item5 Price: "))
item6=float(input("Enter Item6 Price: "))
item7=float(input("Enter Item7 Price: "))
item8=float(input("Enter Item8 Price: "))
item9=float(input("Enter Item9 Price: "))
item10=float(input("Enter Item10 Price: "))

print("_"*30)
total= item1+item2+item3+item4+item5+item6+item7+item8+item9+item10
actualAmount=""
print("Item Total: ", total)
print("_"*30)

if total >= 30000 : 
    actualAmount = total*50/100
    print("After 50%")
    print("Amount to be paid: ", actualAmount)
elif total >= 25000 : 
    actualAmount = total*25/100
    print("After 25%")
    print("Amount to be paid: ", actualAmount)
elif total >= 10000 : 
    actualAmount = total*10/100
    print("After 10%")
    print("Amount to be paid: ", actualAmount)
elif total < 10000 and total >= 0 : 
    print("No discount ", total)
else: 
    print("invalid numbers")