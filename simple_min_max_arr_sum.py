//hackerrank solution of https://www.hackerrank.com/challenges/mini-max-sum/problem
def miniMaxSum(arr):
    arr_min=sorted(arr)
    arr_max=arr_min[::-1]
    min_sum=sum(arr_min[1:])
    max_sum=sum(arr_max[1:])
    print(max_sum,min_sum)
    # Write your code here

if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
