
def staircase(n):
	count=n
	for i in range(0,n+1):
		print(" "*count,"#"*i)
		count=count-1
n=4
staircase(n)
		
