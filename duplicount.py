def Dupplicount(a):
    res=[]
    
    for i in a:
        if a.count(i)>1:
            if i not in res:
                res.append(i)
    
    return ([res,len(res)])
    
z=Dupplicount([5,3,4,6,7,5,3,2,1])
print(z)