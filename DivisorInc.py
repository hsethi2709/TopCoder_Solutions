n=int(input())
m=int(input())
arr=[99999]*100001
arr[n]=0
i=n
for i in range(n,m+1):
    j=2
    while(j*j<=i):
        if(i%j==0):
            k=i+j
            if(k<=m):
                print(k)
                arr[k]=min(arr[k],arr[i]+1)

            k=int(i+(i/j))
            if(k<=m):
                arr[k]=min(arr[k],arr[i]+1)
        j+=1
if(arr[m]==99999):
    print ('-1')
else:
    print(arr[m])

