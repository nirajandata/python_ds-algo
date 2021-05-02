def diagonalDifference(arr):

    dl,dr=0,0
    
    for i in range(n):
        dl+=arr[i][i] 
    counter=0
    
    for j in range(n-1,-1,-1): 
        dr+=arr[j][counter]
        counter+=1 
    
    diag=abs(dl-dr)
    return diag

if __name__ == '__main__':
    n = int(input().strip())
    arr = []
    
    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))
    
    result = diagonalDifference(arr)
