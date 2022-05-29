su = ['國文','英文','微積分','體育','程式設計']
s = []
t = 0
for i in range(5) :
    score = int(input(su[i]+":"))
    s.append(score)
    t += s[i]
    q = float(t/5)
print("平均分數:%.2f"%q)
print("最高分科目:",max(s))
print("最低分科目:",min(s))