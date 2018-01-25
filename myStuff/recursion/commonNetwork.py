
def combineUtil(item1, sets, result):
return
    
def combinationSet(resultSetList):
    print resultSetList
    
set1 = ['a','b']
set2 = ['c','d']
resultSetList = []
resultSetList.append(set1)
resultSetList.append(set2)
combinationSet(resultSetList) 

def find(A,t,res,index =0,tempResult=[]):
  print A,t,res,index,tempResult
  
  if t==0:
    res.append(list(tempResult))
    return 

  for i in range(index,len(A)):
    if (t-A[i]>=0):
      tempResult.append(A[i])
      find(A,(t-A[i]),res,i,tempResult)
      tempResult.pop()
    else:
      break


def findSolution(A, t):
    result = []
    A.sort()
    find(A,t,result)
    
    print result
    
  

def find1(N,n, tempResult, result,index=1):
    if len(tempResult)==n:
      result.append(list(tempResult))
      return
    
    for i in range(index,N+1):
      tempResult.append(i)
      find1(N,n,tempResult,result,i+1)
      tempResult.pop()
    
      
def findCombination(N,n):
  result = []
  find1(N,n,[],result)
  print result
  

def find2(N,tempResult, result,index=1):
    print N,index,tempResult
    if len(tempResult)<=N:
      result.append(list(tempResult))
    else:  
      return
    
    for i in range(index,N+1):
      tempResult.append(i)
      print tempResult
      find1(N,tempResult,result,i+1)
      tempResult.pop()
    
      
def findCombination(N):
  result = []
  find2(N,[],result)
  print result
  


findCombination(4)
A= [2,3,6,4,7]
target =7
findCombination(7,3)



def largestRectangleArea(self, A):
        l = len(A)
        maxArea = 0
        for i in range(l):
          currentArea = 1 * A[i]
          if currentArea> maxArea:
            maxArea = currentArea
          minHeight = A[i]
          for j in range(i+1,l):
            if A[j]<minHeight:
              minHeight = A[j]
            currentArea = minHeight*(j-i+1)
            if currentArea>maxArea:
              maxArea= currentArea
              
        return maxArea
        
        
def swap(A,n1,n2):
  temp = A[n1]
  A[n1]=A[n2]
  A[n2]= temp
  

def find2(A, result,index=0):
    
    if index==(len(A)):
      result.append(list(A))
      return
    
    for i in range(index,len(A)):
      swap(A,index,i)
      find2(A,result,index+1)
      swap(A,index,i)

def findCombination(A):
  result = []
  find2(A,result)
  print result
        