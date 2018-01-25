def findPivot(arrayList):
    #we know the array is in ascending order
    #the pivot will be around the first element which is decreseas
    pivotIndex = 0
    for i in range(0,(len(arrayList)-1)):
        if arrayList[i+1]<arrayList[i]:
            pivotIndex = i+1
            break
    return pivotIndex

def SearchPivotedArray(arrayList,item):
    pivotIndex = findPivot(arrayList)
    print "pivotIndex :"+str(pivotIndex)
    print arrayList[pivotIndex]
    low = 0
    high = len(arrayList)-1
    if pivotIndex > 0:
        if item == arrayList[pivotIndex]:
            return pivotIndex
        elif arrayList[0] > item:
            itemIndex = binary_search(arrayList[pivotIndex+1:],item)
            if itemIndex == -1:
                return -1
            else:
                itemIndex + pivotIndex+1
        else:
            return binary_search(arrayList[:pivotIndex],item)
            
    else:
        return binary_search(arrayList,item)

def binary_search(arrayList,item):
    low =0
    high = len(arrayList)-1
    print arrayList
    while low<=high:
        mid = (high+low)/2
        if arrayList[mid]==item:
            return mid
        elif arrayList[mid] < item:
            low = mid +1
        else:
            high = mid -1
    return -1
    
arrayList = [3,6,9,10,12,14,17,18]
arrayList1 = [5,6,7,8,9,1,2,3,4]
arrayList2 = [ 4,9,7,3,2,3 ]
arrayList3= [ 19, 20, 21, 22, 28, 29, 32, 36, 39, 40, 41, 42, 43, 45, 48, 49, 51, 54, 55, 56, 58, 60, 61, 62, 65, 67, 69, 71, 72, 74, 75, 78, 81, 84, 85, 87, 89, 92, 94, 95, 96, 97, 98, 99, 100, 105, 107, 108, 109, 110, 112, 113, 115, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 128, 130, 131, 133, 134, 135, 136, 137, 138, 139, 141, 142, 144, 146, 147, 148, 149, 150, 153, 155, 157, 159, 161, 163, 164, 169, 170, 175, 176, 179, 180, 185, 187, 188, 189, 192, 196, 199, 201, 203, 205, 3, 7, 9, 10, 12, 13, 17 ]
#print binary_search(arrayList,0,len(arrayList)-1, 10)
print SearchPivotedArray(arrayList2, 5)