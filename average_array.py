##WAP to input an array and count how many elements are greater than the average of array 

arr = [5,10,15,20]
average = sum(arr)/len(arr)
print("The Average of Array is ",average)
for a in arr:
    if a > average:
        print("Element Greater than average of array",a)