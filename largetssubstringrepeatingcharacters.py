str="abcabcbb"
charset=set()
start=0
maxlen=0
for i in range(len(str)):
    while str[i] in charset:
        charset.remove(str[start])
        start+=1
    charset.add(str[i])
    maxlen=max(maxlen,i-start+1)
print(maxlen)
