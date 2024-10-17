e = 0
o = 0
while True:
    num = int(input("Enter an integer (0 to exit): "))
    if num == 0:
        break
    if num%2==0:
        e+=1
    else:
        o+=1
print("----------------------------------")
print("The number of even integers is",e)
print("The number of odd integers is",o)