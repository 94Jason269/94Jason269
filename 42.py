
a = int(input("a:"))
b = int(input("b:"))
c = int(input("c:"))
ans = 0
if b**2-(4*a*c)>0 :
    print(((-b+(b**2-(4*a*c))**0.5))/2*a,((-b-(b**2-(4*a*c))**0.5))//2*a)
elif b**2-(4*a*c)==0 :
    print(-b/(2*a))
else :
    print("0")
    