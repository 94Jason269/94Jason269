x=input("輸入第一個矩陣:").split()
x2=input("輸入第一個矩陣第一列的值:").split()
x3=input("輸入第一個矩陣第二列的值:").split()
x4=input("輸入第二個矩陣:").split()
x5=input("第二個矩陣第一列的值:").split()
x6=input("第二個矩陣第二列的值:").split()
if len(x2) == len(x5) and len(x3) == len(x6) :
    ans = int(x2[0]) + int(x5[0])
    ans2= int(x2[1]) + int(x5[1])
    ans3= int(x3[0]) + int(x6[0])
    ans4= int(x3[1]) + int(x6[1])
    print(str(ans)+" "+str(ans2))
    print(str(ans3)+" "+str(ans4))
else :
    print("兩個矩陣無法相加")