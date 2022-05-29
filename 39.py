x = int(input("輸入一整數:"))
y = x // 2 + 1
for i in range(y) :
    print((y-i) * " " + (2 * i + 1) * "*")
for q in range(y) :
    print(" " * (q + 2) + "*"*((x - 2) - (2 *q)))