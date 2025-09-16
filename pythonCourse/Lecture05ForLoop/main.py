
# range(stop)
for  a in range(100):
    print("AAAAAAAAAAa",a)

print("-"*10)

# range(start, stop)
for  a in range(90,100):
    print("BBBBBBBBBBBB",a)

print("-"*10)


# range( start, stop, step)
for  a in range(90,100,2):
    print("CCCCCCCCCCCCC",a)

print("-"*10)


for a in range(100):
    if a % 2==0:
        print("Evennnnnn ",a)
    else:
        print("Odd ",a)

print("-"*10)

num =int(input("Enter Your Number: "))
merafactorial=1
for b in range(1,num+1):
    merafactorial*=b
print("Factorial is = ",merafactorial)


