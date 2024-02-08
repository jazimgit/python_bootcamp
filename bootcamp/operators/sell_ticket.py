print ("selling tickets with condition")

hight=int(input ("Enter your hight"))

if hight >= 120:
    print ("you can ride")
    ege = int(input ("Please enter your ege : "))
    if ege < 12:
        bill=5
        print ("child tickets are $5")
    elif ege <= 18:
        bill=7
        print ("youth ticket are $7")
    else:
        bill=12
        print ("audult ticket is $12")
    photo=input ("do you want to take photo? : Y OR N ")
    if photo == "Y":
        bill = bill + 5
        print(f"you need give {bill}")
    else:
        print(f"you need give {bill}")
else:
    print ("you cannot ride")
