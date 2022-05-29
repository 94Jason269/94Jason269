n = int(input("輸入一整數:"))
for i in range(1 ,n ,2) :
    print(" "*(n//2) + str(i))
for i in range(1 ,n+1 ,2) :
    print(i ,end="")
for i in range(n-2 ,0 ,-2) :
    print(i ,end="")
print()
for i in range(n-2 ,0 ,-2) :
    print(" "*(n//2)+str(i))