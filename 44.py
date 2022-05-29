T = int(input("輸入任教班級數量:"))
s = []
for i in range(T) :
    s.append(int(input("輸入班級學生數量:")))
print("需購買電腦數量為:",max(s))