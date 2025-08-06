arr=[[1,2],[3,4],[0,6],[5,7],[7.5,9.5]]
n = len(arr)
for i in range(n):
    for j in range(0, n-i-1):
        if arr[j][1] > arr[j+1][1]:
            arr[j], arr[j+1] = arr[j+1], arr[j]
i=0
j=1
count=1
while i<len(arr) and j<(len(arr)):
    if arr[i][1]<=arr[j][0]:
        count+=1
        i=j
        j+=1
    else:
        j+=1
print(count)