k = 4
l = [ 2,3,4,5,6,8]

flag = 0
n = len(l)

for i in range(n):
	if l[i] == k:
		flag = 1
		pos = i
		break 

if flag == 0:
	print("Element not present")
else:
	print("Element is present at index", str(pos))
