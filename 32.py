m = int(input("小明身上有幾元:"))
n = int(input("販賣機有幾種飲料:"))
ans = 0
for i in range(n) :
    price = int(input("販賣機飲料價格:"))
    if m >= price :
        ans += 1
print("可以購賣的飲料數量為:",ans)