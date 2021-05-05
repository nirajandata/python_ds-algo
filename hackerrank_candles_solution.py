arr=[3,4,4]
def sol(arr):
	max=sorted(arr,reverse=True)[0]
	msum=0 
	for i in arr:
		if (i==max):
			msum+=1
	return msum
print(sol(arr))
	
