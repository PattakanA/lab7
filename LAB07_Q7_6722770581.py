print("===================")
print("Cashier Program")
print("===================\n")
y = 0
i = 0
while True:
    x = float(input("Enter item price or -1 when finished: "))
    if x == -1:
        break
    else:
        y+=x
        i+=1

print("\nTotal purchase amount is %.2f"%y)
pay = float(input("Your payment: "))
print("\n You bought %d items today." %i)
print("Your change is %.2f baht." %(pay-y))