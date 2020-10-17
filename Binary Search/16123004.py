l = [ 2,3,4,5,6,8]

n = len(l)

k = 4

left = 0
right = n - 1
mid = 0

flag = 0

while left <= right: 

    mid = (right + left) // 2

    if l[mid] < k: 
        left = mid + 1

    elif l[mid] > k: 
        right = mid - 1

    else: 
        flag = 1
        pos = mid
        break 

if flag == 0:
	print("Element not present")
else:
	print("Element is present at index", str(pos))

