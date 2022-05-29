x = input("輸入一連串數字為甲方:")
y = input("輸入一連串數字為乙方:")
for i in range(len(x)) :
    if x[i] == "1" and y[i] == "5" :
        print("贏",end="")
    elif x[i] == "5" and y[i] == "1" :
        print("輸",end="")
    elif x[i] == "2" and y[i] == "1" :
        print("贏",end="")
    elif x[i] == "1" and y[i] == "2" :
        print("輸",end="")
    elif x[i] == "3" and y[i] == "2" :
        print("贏",end="")
    elif x[i] == "2" and y[i] == "3" :
        print("輸",end="")
    elif x[i] == "4" and y[i] == "3" :
        print("贏",end="")
    elif x[i] == "3" and y[i] == "4" :
        print("輸",end="")
    elif x[i] == "5" and y[i] == "4" :
        print("贏",end="")
    elif x[i] == "4" and y[i] == "5" :
        print("輸",end="")
    else :
        print("和",end="")