one = input("輸入第一行正整數為:")
two = input("第二行中數列中的數字為:").split()
c = 1
for i in two :
    if two.count(i) > c :
        c = two.count(i)
        f = i
    
if c == 1 :
    print("每個數字剛好只出現 1 次")
else :
    print("最大出現次數的數字為:", f ,"出現次數為:", c )