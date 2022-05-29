x = int(input("搭了幾次電梯:"))
f = 1
m = 0
for i in range(x) :
    f2 = int(input("請輸入搭到幾樓:"))
    if f2 > f :
        m += (f2 - f) * 20
    elif f2 < f :
        m += (f - f2) * 10
    f = f2
print(m,"元")