D=["Mon","Tues","Wednes","Thurs","Fri","Satur","Sun"]
from datetime import date
for _ in range(int(input())):
    args=input().split("-")
    if len(args)==4:
        args[1]="-"+args[1]
    args=args[-3:]
    args=list(map(int,args))
    d=date(*args)
    i=d.toordinal()
    if i<=639785: i+=5
    i+=6
    i%=7
    i+=7
    i%=7
    print(D[i]+"day")