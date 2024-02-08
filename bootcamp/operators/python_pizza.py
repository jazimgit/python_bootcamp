print ("we are selling python pizza")
size=input ("Please enter the size of pizza (S OR M Or L) : ")
if size == "S":
    print ("you chose small pizza ")
    bill=15
    pep=input("do you want to add pepperoni (Y or N):") 
    if pep == "Y":
        bill= bill + 2
    chees=input ("do you want to add chees (Y or N):")
    if chees == "Y":
        bill= bill + 1
elif size == "M":
    print ("you chose midium pizza ")
    bill=20
    pep=input("do you want to add pepperoni (Y or N):") 
    if pep == "Y":
        bill= bill + 3
    chees=input ("do you want to add chees (Y or N):")
    if chees == "Y":
        bill= bill + 1
else:
    print ("you chose large pizza ")
    bill=25
    pep=input("do you want to add pepperoni (Y or N):") 
    if pep == "Y":
        bill= bill + 3
    chees=input ("do you want to add chees (Y or N):")
    if chees == "Y":
        bill= bill + 1

print ("thanks ......")
print (f"your bill is {bill}")

