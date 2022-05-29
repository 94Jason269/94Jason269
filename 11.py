cc=["Capricornus","Sagittarius","Aquarius", "Pisces", "Aries", "Taurus", "Gemini", "Cancer", "Leo", "Virgo", "Libra", "Scorpio" ]
month=int(input("請輸入出生月份:"))
day=int(input("請輸入出生日期:"))
if month == 1:
    if day < 20:
        print("星座為:",cc[0])
    else:
        print("星座為:",cc[2])
elif month == 2: 
    if day < 19:
        print("星座為:",cc[2])
    else:
        print("星座為:",cc[3])
elif month == 3:
    if day < 20:
        print("星座為:",cc[3])
    else:
        print("星座為:",cc[4])
elif month == 4:
    if day < 20:
        print("星座為:",cc[4])
    else:
        print("星座為:",cc[5])
elif month == 5:
    if day < 21:
        print("星座為:",cc[5])
    else:
        print("星座為:",cc[6])
elif month == 6:
    if day < 21:
        print("星座為:",cc[6])
    else:
        print("星座為:",cc[7])
elif month == 7:
    if day < 22:
        print("星座為:",cc[7])
    else:
        print("星座為:",cc[8])
elif month == 8:
    if day < 23:
        print("星座為:",cc[8])
    else:
        print("星座為:",cc[9])
elif month == 9:
    if day < 23:
        print("星座為:",cc[9])
    else:
        print("星座為:",cc[10])
elif month == 10:
    if day <23 :
        print("星座為:",cc[10])
    else:
        print("星座為:",cc[11])
elif month == 11:
    if day < 22:
        print("星座為:",cc[11])
    else:
        print("星座為:",cc[1])
elif month == 12:
    if day < 22:
        print("星座為:",cc[1])
    else:
        print("星座為:",cc[0])