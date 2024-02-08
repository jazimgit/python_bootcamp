print ("will check no and print the type of no")
num=int(input("please enter number : "))

num_type=type(num)

print (num_type)

# if num_type == '<class 'int'>':
#     print ("you typed number we can procced ..... ")
# else:
#     print ("you have entered wrong input Please check input")
#     exit()

check_num=num%2

if check_num == 0:
    print (f"you typed {num} that is even number....thanks")
else:
    print (f"you typed {num} that is odd number......thanks")



