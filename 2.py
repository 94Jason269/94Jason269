ele=int(input("請輸入一個度數:"))
if ele <= 120 :
    print("summer months:",(ele * 2.10))
    print("non-summer months:",(ele * 2.10))
elif ele <= 330:
    print("summer months:",((ele-120) * 3.02 + 120 * 2.10))
    print("non-summer months:",((ele-120) * 2.68 + 120 * 2.10))
elif ele <= 500:
    print("summer months:",((ele-330) * 4.39 + (330-120) * 3.02 + 120 * 2.10))
    print("non-summer months:",((ele-330) * 3.61 + (330-120) * 2.68 + 120 * 2.10))
elif ele <= 700 :
    print("summer months:",((ele-500) * 4.97 + (500-330) * 4.39 + (330-120) * 3.02 + 120 * 2.10))
    print("non-summer months:",((ele-500) * 4.01 + (500-330) * 3.61 + (330-120) * 2.68 + 120 * 2.10))
elif ele > 700 :
    print("summer months:",((ele-700) * 5.63 + (700-500) * 4.97 + (500-330) * 4.39 + (330-120) * 3.02 + 120 * 2.10))
    print("non-summer months:",((ele-700) * 5.63 + (700-500) * 4.01 +(500-330) * 3.61 + (330-120) * 2.68 + 120 * 2.10)) 
    