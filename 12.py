
X = input("輸入一整數序列為:").split()
h=len(X)
for n in X:
    if X.count(n) > h//2:
        oh=n
    else:
        oh="NO"
print("過半元素為:",oh)