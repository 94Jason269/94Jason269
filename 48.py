dict = {}
for i in range(int(input("輸入筆數n:"))):
    e, c = input("請輸入單字英文及中文:").split()
    dict[e] = c
sc = input("輸入欲查詢單字:")
if sc in dict:
    print(sc,"中文意思為",dict[sc])
else:
    print("字典未有此單字")