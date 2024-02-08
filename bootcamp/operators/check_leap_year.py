print ("In this program will check leap year by adding year value")

year=int(input("Please enter ther year : "))

print (f"e.g. The year {year}")

if year % 4 == 0:
    print("this is leap year")
    if year % 100 == 0:
        if year % 400 == 0:
            print ("this is leap year")
        else:
            print ("this is not leap year")
    else:
        print("this is leap year")
else:
    print ("this is not leap year")
            
