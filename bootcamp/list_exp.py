#here we will do list example

line1=[" ", " ", " "]
line2=[" ", " ", " "]
line3=[" ", " ", " "]
map=[line1, line2, line3]

ask=input("please enter location")
letter=ask[0].lower()
print (f"lettter = {letter}")
abc=["a", "b", "c"]
letter_index=abc.index(letter)
actul_index=int(ask[1])

map[letter_index][actul_index]="X"

print(f"{letter_index}")
print(f"{actul_index}")

print(f"{line1}\n{line2}\n{line3}")
