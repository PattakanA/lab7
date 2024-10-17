num = 0
while num!=3:
    txt = []
    print("===== MAIN MENU =====")
    print("1. Addition")
    print("2. Subtraction")
    print('3. Exit \n')
    num = int(input("Select an operation (1-3): "))
    if num == 3:
        break
    txt = input("Enter two numbers: ").split(" ")
    if num== 1:
        print("%s + %s = %d " %(txt[0],txt[1],(int(txt[0])+int(txt[1]))))
    elif num == 2:
        print("%s - %s = %d " %(txt[0],txt[1],(int(txt[0])-int(txt[1]))))
    else:
        break
    print("\n")
print("Bye!!! \n")
    

