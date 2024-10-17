num = int(input("Enter an integer number: "))
x = 0
y = num-2
t = num-2
print("o "*num)
while x!=(y):
    print("o "+"  "*(y-t)+ "x "*t + "o")
    x+=1
    t-=1

print("o "*num)