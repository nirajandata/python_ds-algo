class Solution(object):
    def reverse(self, x):
       l=1
       if x<0:
        l=-1
        x=-1*x
       x=str(x)
       x=x[::-1]
       x=l*int(x)
       return x if -(2**31)-1 < x < (2**31) else 0
