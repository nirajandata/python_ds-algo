n=int(input())
#testing n=4
arr=[]
#testing answer=['a','c','d','b']
count=0
for i in range(n):
 arr.append(input())
 if(i==0):
     print(i)
 else:
     for j in range(i):
         fin=arr[i]
         if(fin>arr[j]):
             count+=1
         if(j==i-1):
             print(count)

     count=0

