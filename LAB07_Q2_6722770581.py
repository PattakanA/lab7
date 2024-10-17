txt = ""
list = []
new = ""
txt = input("Input: Enter a word: ")
while txt !="exit" and txt != "Exit":
    list.append(txt.capitalize())
    txt = input("Input: Enter a word:")

        
print("Output:", list)