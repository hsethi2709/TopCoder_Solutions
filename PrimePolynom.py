import math
def isPrime(n):
    if(n==2):
        return True
    if(n!=2 and n%2==0):
        return False

    for i in range(3,int(math.sqrt(n))+1):
        if(n%i==0):
            return False

    return True


a=int(input())
b=int(input())
c=int(input())
i=0
ans=True
while(ans):
    i += 1
    num=(a * math.pow(i, 2) + b * i + c)
    if(num<0):
        i=0
        break
    else:
        ans=isPrime(a * math.pow(i, 2) + b * i + c)


print(i)
