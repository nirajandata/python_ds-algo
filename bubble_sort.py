def bubble_sort(arr):
  num=len(arr)
  for i in range(num-1):
    for j in range(num-1):
      if arr[j]>arr[j+1]:
        arr[j],arr[j+1]=arr[j+1],arr[j]
arr=[1,3,2,3,43,45,0]
bubble_sort(arr)
for b in range(len(arr)):
  print(arr[b])
