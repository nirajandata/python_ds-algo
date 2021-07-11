s,n=input().split()
arr=[]
n=int(n)
for i in range(len(s)):
    arr.append(s[i:])
    

val=sorted(arr)
val=val[n-1]
print("".join(val))
