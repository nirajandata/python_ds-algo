#list1=[int(x) for x in input().split()]
list1=[3,4,5,7,8,9,50]
t=5
n=len(list1)

def binar():
 l=0 ;r=n-1
 while (l<=r):
  mid=(r-l)//2 +l
 
  if (t==int(list1[mid])):
   return mid
  elif (t>int(list1[mid])):
   l=mid+1
  else:
   r=mid-1
 return -1
print(binar())
