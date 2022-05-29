A = list(input("輸入A的好友:").split())
B = list(input("輸入B的好友:").split())
ans = 0
for i in A :
    if i in B :
        ans += 1
print(ans)