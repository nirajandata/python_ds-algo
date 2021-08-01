#https://www.hackerrank.com/challenges/divisible-sum-pairs/problem?utm_campaign=challenge-recommendation&utm_medium=email&utm_source=24-hour-campaign
def divisibleSumPairs(n, k, ar):
    count=0
    for i in range(n):
        for j in range(i):
            #print(ar[i],ar[j])
            if((ar[i]+ar[j])%k==0):
                #print(ar[i],ar[j])
                count+=1
    return count

n,k=map(int,input().split())
arr=[int(i) for i in input().split()]
arr=sorted(arr)
print(divisibleSumPairs(n,k,arr))
