m=int(input("請輸入階乘值 M:"))
N = 1
ans = 1
while ans < m :
    N = N + 1
    ans = ans * N

print("超過M為",m,"的最小階乘N值為",N)
