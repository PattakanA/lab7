txt = ""
list = []
while True:
    txt = input("Input: Enter a word: ")
    if txt == "exit":
        break 
    if txt[-1:] == "y":
        txt = txt[:-1]+"ily"
    list.append(txt)   
print("Output:", list)