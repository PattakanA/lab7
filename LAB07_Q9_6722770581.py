x = 0
while True:
    num = int(input("Enter an integer (-1 to exit): "))
    if num == -1:
        break
    else:
        x+=num
print("The sum of 5 number(s) is",x)