ad,a=input().split()
b=list(input())
d=list(b)
 
for j in range(int(a)):
 for i in range(int(ad)-1):
  if (b[i]=="B" and b[i+1]=="G"):
   d[i],d[i+1] =d[i+1],d[i]
 b=list(d)
 
b="".join(b)   
print(b)
