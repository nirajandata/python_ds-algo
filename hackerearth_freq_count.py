n=int(input())
lis=[i for i in input().split()]
print(max(lis,key=lis.count))
