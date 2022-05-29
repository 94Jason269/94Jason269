x = {"123":[456,9000],"456":[789,5000],"789":[888,6000],"336":[558,10000],"775":[666,12000],"566":[221,7000]}
f = int(input("輸入查詢組數N為:"))
q="123"
w="456"
e="789"
a="888"
s="558"
d="775"
z="666"
c="566"
v="221"
for i in range(f) :
    y = input("請輸入帳號:")
    y2 = input("請輸入密碼:")
    if y == q and y2 == w :
        print(x[y][1])
    elif y == w and y2 == e :
        print(x[y][1])
    elif y == e and y2 == a :
        print(x[y][1])
    elif y == a and y2 == s :
        print(x[y][1])
    elif y == d and y2 == z :
        print(x[y][1])
    elif y == c and y2 == v :
        print(x[y][1])
    else :
        print("error")