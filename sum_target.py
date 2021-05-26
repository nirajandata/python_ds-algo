# finding the minimum and maximum sum of the two digit target value
# input : 15 => 69 96 (6+5=> is the min. sum  of 15)
n,m=map(int,input().split())

def soln(n,m):
 min_sum=0
 for i in range(1,10):
  for j in range(10):
   sums=i+j # as first sum in ascending order is always min_sum 
   print(sums,i,j)
   if(sums==m):
    min_sum=int(str(i)+str(j))
    if(j==0):
        maxs=min_sum
    else:
     maxs=int(str(min_sum)[::-1])
    return min_sum,maxs

 return -1 , -1

n,m=soln(n,m)
print(n,m)
