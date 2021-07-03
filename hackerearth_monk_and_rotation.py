t=int(input())
for i in range(t):
    a,b=map(int,input().split())
    arr=[int(x) for x in input().split()]
    b=b%a
    s=a-b
    val=arr[s:]+arr[:s]
    print(" ".join(str(j) for j in val))
