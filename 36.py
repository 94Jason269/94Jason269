t = int(input("請輸入測試資料(1~20):"))
x = []
for i in range(t) :
    if i == t:
        break
    for z in range(4) :
        e=input("請輸入第"+str(z+1)+"項資料:")
        x.append(e)
    if int(x[1]) - int(x[0]) == (int(x[3]) - int(x[2])) :
        ans = int(x[3]) + (int(x[3]) - int(x[2]))
        x.append(str(ans))
        print(str(x)+"此為等差數列")
    if  int(x[1]) / int(x[0]) == int(x[2]) / int(x[1]) :  
        ans2 = int(x[3]) * 2
        x.append(str(ans2))
        print(str(x)+"此為等比數列")
    
    x = []
    

