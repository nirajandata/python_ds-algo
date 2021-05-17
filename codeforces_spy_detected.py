
n=int(input())
li=[]
nu=[]
for i in range(n):
 num=int(input())
 nu.append(num)
 a=[int(i) for i in input().split()]
 li.append(a)



def sol(l,nums):
 ind=-1
 l_test=l[:3]
 l_test.sort()
 if (l_test[1]==l_test[2]):
  sim=l_test[1]
 elif (l_test[0]==l_test[1]):
  sim=l_test[1]
 else:
  ind=1
 for i in range(nums):
  if (l[i]!=sim):
    ind=i+1 
    break 
 return ind
for i in range(n):
 print(sol(li[i],nu[i]))
