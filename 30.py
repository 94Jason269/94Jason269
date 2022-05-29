from re import L


x = list(input("正確答案為:"))
A = 0
B = 0
while True :
    z = list(input("猜測答案:"))
    for i in range(len(x)) :
        if x[i] == z[i] :
            A += 1
        elif z[i] in x :
            B += 1
        else :
            continue
        
    print(A,"A",B,"B")
    A = 0
    B = 0
    if x == z :
        break