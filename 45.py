m = int(input("輸入出生月份:"))
d = int(input("輸入出生日期:"))
s = (m*2 + d) % 3
if s == 2 :
    print("大吉")
elif s == 1 :
    print("吉")
elif s == 0  :
    print("普通")