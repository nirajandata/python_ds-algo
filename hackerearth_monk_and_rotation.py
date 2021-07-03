#https://www.hackerearth.com/problem/algorithm/monk-and-rotation-3-bcf1aefe/
t=int(input())
for i in range(t):
    a,b=map(int,input().split())
    arr=[int(x) for x in input().split()]
    b=b%a
    s=a-b
    val=arr[s:]+arr[:s]
    print(" ".join(str(j) for j in val))
