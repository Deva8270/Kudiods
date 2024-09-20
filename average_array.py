##WAP to input an array and count how many elements are greater than the average of array 

arr = []
a = int(input("Enter No. of elements"))
for i in range(0,a):
    ele = int(input())
    arr.append(ele)
average = sum(arr)/len(arr)
print("The Average of Array is ",average)
for a in arr:
    if a > average:
        print("Element Greater than average of array",a)