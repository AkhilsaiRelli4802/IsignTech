def fun(n):
    a=0
    b=1
    string=""
    res=[]
    for i in range(2,n):
        c=a+b
        string+=str(c)
        a=b
        b=c
    resste="0"+"1"+string
    for i in resste:
        res.append(int(i))
    return res
z=fun(5)
print(z)