from msilib.schema import RadioButton


o = ""
p = input("輸入傳送密碼(6位數):")
if len(p) == 6 :
    p2 = list(p)
    for i in range(0,len(p)):
        for x in range(0,10):
            if x*4%7 == int(p2[i]):
                o += str(x)
                break
print("解密後密碼為:",o)