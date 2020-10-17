l = [ 2,3,4,5,6,8]

n = len(l)

for i in range(n-1):  
        for j in range(n-i-1): 
            if l[j] > l[j+1] : 
                l[j], l[j+1] = l[j+1], l[j] 

print ("Sorted Array:") 
print (l)