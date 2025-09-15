print("*"*8)

print("Sign Up")

userName= input("Enter Your Name: ")

userEmail= input("Enter Your Email: ")

userPass= input("Enter Your  Password: ")

userContact= input("Enter Your Contact: ")

print("Account Successfully created")

userEmailLogin= input("Enter Your Email: ")
userPassLogin= input("Enter Your  Password: ")


if userEmail==userEmailLogin and userPass== userPassLogin:
    print("Welcome In MITI ",userName )
    print("*"*25)
    print("Program 01 Marksheet ")
    eng=float(input("Enter Your English Marks: "))
    urdu=float(input("Enter Your Urdu Marks: "))
    math=float(input("Enter Your Math Marks: "))

    obtained=eng+urdu+math
    meriPercentage=obtained/300*100
    print("Obatined Marks = ", obtained)
    print("Percentage = ", meriPercentage, "%")
    if meriPercentage<=100 and meriPercentage>=80:
        print("Grade A1 MashaAllah ")
    elif meriPercentage<=79 and meriPercentage>=70:
        print("Grade A ")
    elif meriPercentage<=69 and meriPercentage>=60:
        print("Grade B ")
    elif meriPercentage<=59 and meriPercentage>=50:
        print("Grade C ")
    elif meriPercentage<=49 and meriPercentage>=40:
        print("Grade D  ")
    elif meriPercentage<=39 and meriPercentage>=30:
        print("Grade F ")
    else:
        print("Try Again")

    print("*"*25)
    print("Program No 02 EVEN / ODD")
    num=int(input("Enter Your Number: "))
    if num%2==0:
        print(num, "is Even ")
    else:
        print(num, "is Odd")
    
    print("*"*25)
    print("Program No 03 LEAP YEAR ")
    year=int(input("Enter Any Year "))
    if year%4==0:
        print("Leap Year: ", year)
    else:
        print(year, "is not a Leap Year")


    print("*"*25)
    print("Program No 04 POS/ NEG")
    num1=int(input("Enter any number: "))
    if num1 <0:
        print(num1, " is negative")
    else:
        print(num1, " is positive")

    print("*"*25)
    print("Positive") if num1>0 else print("Negative")


else:
    print("Incorrect Email or Password ")
    

# practiceQuestion:
# if we go mart and buy 10 products then 
# if sum of 10 products is 30000 pkr or above then give 50% discount
# if sum of 10 products is 25000 pkr then give 25% discount
# if sum of 10 products is 10000 pkr then give 10% discount
# if sum of 10 products is less then 10000  pkr then no discount