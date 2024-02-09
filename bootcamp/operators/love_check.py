print ('''             . --- .
           /        \
          |  O  _  O |
          |  ./   \. |
          /  `-._.-'  \
        .' /         \ `.
    .-~.-~/           \~-.~-.
.-~ ~    |             |    ~ ~-.
`- .     |             |     . -'
     ~ - |             | - ~
         \             /
       ___\           /___
       ~;_  >- . . -<  _i~
          `'         `'
       ''')
print ("we are creating love calculater. Please enter two name will print love between them")
name1=input ().lower()
name2=input().lower()

#combine string
com_name = str(name1) + str(name2)

#check char in string

L=com_name.count("l")
O=com_name.count("o")
V=com_name.count("v")
E=com_name.count("e")

G=com_name.count("g")
I=com_name.count("i")
U=com_name.count("u")
A=com_name.count("a")


cal1 = L + O + V + E
cal2 = G + I + U + A

score = str(cal1) + str(cal2)

print ("your love scoere is " + score + "thanks .......")

