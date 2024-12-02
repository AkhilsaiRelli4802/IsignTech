a=[7,145,28,10]
res=[]

for i in a:
    count=0
    for j in range(2,i):
        if i%j==0:
            count+=1
    if count==0:
        res.append("Prime")
    else:
        i=str(i)
        # print(i)
        factlis=[]
        for k in i:
            k=int(k)
            fact=1
            for z in range(1,k+1):
                fact*=z
            factlis.append(fact)
        if sum(factlis) == int(i):
            res.append("Strong")
        else:
            i=int(i)
            perfect=0
            for p in range(1,i):
                if i%p==0:
                    perfect+=p
            if perfect == i:
                res.append("Perfect")
else:
    res.append(i)  
print(res)