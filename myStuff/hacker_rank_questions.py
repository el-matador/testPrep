#Compress the string to aabbaa -> a2b2a2 not a4b2

def string_compression(strArray):
    #using extra space
    n= len(strArray)
    if n<2:
        return strArray
    count,prev = 1,0
    result = ''
    for i in range(1,n):
        if strArray[prev]==strArray[i]:
            count = count + 1
        else:
            result += strArray[prev]+ str(count)
            count = 1
        prev = i
    result += strArray[-1]+str(count)
    print result

#str1 = 'aaabbdcccccf'
#string_compression(str1)

def spiralOrder( n):
        A = [[0 for x in range(n)] for x in range(n)]
        result = []
        rows = n
        clmn = n
        #print (rows,clmn)
        top = 0
        left = 0
        bottom = rows
        right = clmn
        dir = 0
        res = []
        
        counter = 1
        while(top <bottom and left <right):
        #print(top,bottom,left,right)
            if (dir==0):
                #print('going right')
                for i in range(left,right):
                    #res.append(A[top][i])
                    A[top][i] = counter
                    counter +=1
      
                top = top + 1 
                dir = 1 
                #print "going left",A
            elif (dir ==1):
                #print('going down')
                for i in range(top, bottom):
                    #print (i)
                    #res.append(A[i][right-1])
                    A[i][right-1] = counter
                    counter +=1
      
                right = right - 1 
                dir = 2
            elif (dir ==2):
                #got to the left
                #print('going left')
                for i in range(right-1,left-1, -1):
                    #for i in range(1,-1, -1):
                    #print(i)
                    #res.append(A[bottom-1][i])
                    A[bottom-1][i] = counter
                    counter +=1
      
                bottom = bottom - 1 
                dir = 3
            elif (dir==3):
                #print('going to top')
                for i in range(bottom-1,top-1, -1):
                    #res.append(A[i][left])
                    A[i][left] = counter
                    counter +=1
                left = left + 1 
                dir = 0
        ## Actual code to populate result
        return A


def generateMatrix( A):
        ans = [[0]*A for j in xrange(A)]
        l = 0
        r = A-1
        t = 0
        b = A-1
        di = 0
        j = 1
        while (l <= r and t <= b):
            if di == 0:
                for i in xrange(l,r+1):
                    ans[t][i] = j
                    j = j + 1
                di = 1
                t = t + 1
            elif di == 1:
                for i in xrange(t,b+1):
                    ans[i][r] = j
                    j = j +1
                di = 2
                r = r - 1
            elif di == 2:
                for i in xrange(r,l-1,-1):
                    ans[b][i] = j
                    j = j + 1
                di = 3
                b = b -1
            else:
                for i in xrange(b,t-1,-1):
                    ans[i][l] = j
                    j = j +1
                di = 0
                l = l + 1
        return ans
#n=3
#print spiralOrder(n)


def permutationForDistinct(inputStringList):
    
    #if the list is empty
    #print "Input String :",inputStringList
    if len(inputStringList) ==0:
        return []
    
    #if only one element is left in the list then one permutation possible
    if len(inputStringList) ==1:
        return [inputStringList]
    
    # Find the permutations for lst if there are
    # more than 1 characters
 
    l = [] # empty list that will store current permutation
    
    # Iterate the input(lst) and calculate the permutation
    for i in range(len(inputStringList)):
        m = inputStringList[i]
        remLst = inputStringList[:i]+inputStringList[i+1:]
        #print "First---",inputStringList[:i]
        #print "Second--",inputStringList[i+1:]
        #print "remaining List :",remLst
        
        # Generating all permutations where m is first
        for p in permutationForDistinct(remLst):
            #print "appending---> :",m,p
            l.append(str(m) + str(p))
    
    return l

 
 
# Driver program to test above function
#data = 'rta'
#print permutationForDistinct(data)


def permute(input):

    #create a map for the count of all characters in the string
    count_map = {}
    for ch in input:
        if ch in count_map.keys():
            count_map[ch] = count_map[ch] + 1
        else:
            count_map[ch] = 1
            
    print "count_map :",count_map
    
    keys = sorted(count_map)
    print "keys in sorted order :",keys
    str = []
    count = []
    for key in keys:
        str.append(key)
        count.append(count_map[key])
    
    print "str list :",str
    print "count list :",count
    result = [0 for x in range(len(input))]
    permute_util(str, count, result, 0)

def permute_util(str, count, result, level):
    if level == len(result):
        print(result)
        return

    for i in range(len(str)):
        if count[i] == 0:
            continue;
        result[level] = str[i]
        count[i] -= 1
        #print result
        permute_util(str, count, result, level + 1)
        count[i] += 1

if __name__ == '__main__':
    #input = ['B', 'C', 'A', 'A']
    input = 'rrta'
    permute(input)
    data1 = 'rta'
    data2 = 'rrta'
    #print permutationForDistinct(data2)