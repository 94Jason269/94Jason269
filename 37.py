n = int(input("輸入n(0 < n < 1000000):"))
while n != 1 :
    if n % 2 == 0 :
        print(int(n),end=" ")
        n = n/2
    else :
        print(int(n),end=" ")
        n = 3 * n + 1
else :
    print("結束(1)")