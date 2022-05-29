x=str(input("請輸入檢測的字串(end結束):"))

if x == "end" :
    print("檢測結束")
else :
    y=str(input("請輸入檢測的單一字元:"))
    print("字元",y,"出現次數為:",x.count(y))