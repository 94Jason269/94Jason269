p=input("輸入一組四位數字:")
p2=list(p)
for i in range(len(p2)):
    p2[i] = (int(p2[i])+7)%10
print("輸出加密後的數字為:"+str(p2[2])+str(p2[3])+str(p2[0])+str(p2[1]))