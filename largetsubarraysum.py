arr=[15,-2,2,-8,1,7,10,23]
k=0
prefixsum={}
maxlen=0
sum=0
for i in range(len(arr)):
    sum+=arr[i]
    if sum == k:
        maxlen=max(maxlen,i+1)
    rem=sum-k
    if rem in prefixsum:
        length=i-prefixsum[rem]
        maxlen=max(maxlen,length)
    if rem not in prefixsum:
        prefixsum[sum]=i
print(maxlen)