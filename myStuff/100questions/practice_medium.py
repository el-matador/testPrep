#Question Two sum: Given an array of integers, find two numbers such that they add up to a specific target number
A = [2,4,5,1,15,4,7]
A1=[1,4,2,7,9]
target = 9
#output [1,2]

def twoSum(A,target):
    j =1
    mapIndexPair = {}
    for index in range(len(A)):
        for j in range (index+1,len(A)):
            if A[j]== (target - A[index]):
                mapIndexPair[index] = j

    return mapIndexPair
    
#print twoSum(A,9)
            
#another solution with O(n)

def twoSums(A,target):
    map = {}
    result = []
    for i in range(len(A)):
        if A[i] in map:
            index = map[A[i]]
            result.append((index,i))
            #break
        else:
            map[target-A[i]]= i
    return result
#print twoSums(A1,11)



#third approach
#First sort the array, then start tracking from left and right.

    
def hasArrayTwoCandidates(A,sum):
    arrayLength = len(A)
    result = []
    #sort the array first
    A.sort()
    print A
    l=0
    r=arrayLength -1
    while (l<arrayLength) and (r>=0):
        if ((A[l] + A[r]) == sum):
            result.append((l,r))
            print result
            return 1
        elif ((A[l] + A[r]) < sum):
            l +=1
        else:
            r -= 1
    return 0
    
#print hasArrayTwoCandidates(A,9)
#question: Find a triplet that sum to a given value

#Question : Add two numbers represented by linked lists


#Question: Stock Buy Sell to Maximize Profit




class Interval:
    def __init__(self):
        self.buy = 0
        self.sell = 0
        
def stockBuySell(priceList):
    #prices must be for atleast two days
    n = len(priceList)
    print "size of list :"+str(n)
    print priceList
    if n == 1:
        return
    count = 0
    
    #solution array
    solution = []
    i = 0
    j=0
    while i< n-1:
        
        #find the local minima first
        while ((i<(n-1)) and (priceList[i+1]<= priceList[i])):
            i +=1
        print "end of finiding local minima :"+str(i)
       
        #if we reached the end then no further 
        if i == (n-1):
            break
        e = Interval()
        e.buy = i
        i +=1
        

        #find local maxima
        while (i<n) and ((priceList[i]>=priceList[i-1])):
            i +=1
        
        print "end of finiding local maxima :"+str(i)
        e.sell =i-1
        solution.append(e)
        
        count +=1
        
    if count == 0:
        print "No solution "
        
    else:
        for interval in solution:
            print "Buy :"+str(interval.buy)+" Sell :"+str(interval.sell)
            
priceList = [100, 180, 260, 310, 40, 535, 695]
#stockBuySell(priceList)
    



#Question : Combinational sum

def combinationSum(candidates, target):
        #First sort the candidates
        candidates.sort()
        #Remove all the duplicates from candidates
        solution=[]
        
        combinationSumRec(candidates, target, 0, 0, [], solution)
        return solution
        
def combinationSumRec(candidates, target, index, sum, listT, solution):
        #If at any time sub-problem sum == 0 
        #then add that array to the result
        #if index == len(candidates):
            #return
        #print "count :",count
        #print "Solution :",solution," Sum :",sum," Index :",index
        if sum == target:
            solution.append(list(listT))
            print "Appending Solution :",solution
        for i in range(index,len(candidates)):
            if sum + candidates[i] > target:
                break;
            listT.append(candidates[i])
            print "list :",listT
            
            combinationSumRec(candidates, target, i, sum+candidates[i], listT, solution, count)
            listT.pop()
        

candidates = [10,1,2,7,6,1,5]
target = 8

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

class Solution:
    # @param candidates, a list of integers
    # @param target, integer
    # @return a list of lists of integers
    def DFS(self, candidates, target, start, valuelist):
        length = len(candidates)
        if target == 0:
            return Solution.ret.append(valuelist)
        for i in range(start, length):
            if target < candidates[i]:
                return
            self.DFS(candidates, target - candidates[i], i, valuelist + [candidates[i]])
        
    def combinationSum(self, candidates, target):
        candidates.sort()
        Solution.ret = []
        self.DFS(candidates, target, 0, [])
        return Solution.ret


#Question Sum with no duplicates

def combinationSum2(candidates, target):
        candidates.sort()
        solution =[]
        combinationSum2Rec(candidates, target, 0, 0, [], solution)
        return solution
    
def combinationSum2Rec(candidates, target, index, sum, tempList, solution):
        if sum == target:
            solution.append(list(tempList))
            return
        for i in range(index, len(candidates)):
            if (i==index or candidates[i-1]!=candidates[i]) and sum+candidates[i]<=target:
                tempList.append(candidates[i])
                combinationSum2Rec(candidates, target, i+1, sum+candidates[i], tempList, solution) 
                tempList.pop()


#print combinationSum2(candidates, target)

#Question Given two integers n and k, return all possible combinations of k numbers out of 1 ... n.


#keep values in decreasing order
def knapsack(valueList, weightList, maxWeight):
    if maxWeight == 0:
        return 0
    for index in range(len(valueList)):
        if maxWeight == 0:
            break
        elif (maxWeight -weightList[index])>=0:
            knapsack.value += valueList[index]
            maxWeight -= weightList[index]
            knapsack(valueList, weightList, maxWeight)
            
    return knapsack.value

#Question brute force solution to dynamic programming
def _maxKnapsack(items,w,index):
    #if we have gone through all items then return
    print w,index
    if index == len(items):
        return 0
    
    #if weight is too big then skip it
    if (w - items[index].weight) <0:
        return _maxKnapsack(items,w,index+1)
    
    return max(_maxKnapsack(items,w-items[index].weight,index+1)+ items[index].value, _maxKnapsack(items,w,index+1))


def maxKnapsack(itemList, maxWeight):
    return _maxKnapsack(itemList, maxWeight,0)
    
class Item:
    def __init__(self,wt=0,v=0):
        self.weight = wt
        self.value = v

valueList = [6,10,12]
weightList = [2,2,3]
itemList=[]
for index in range(len(weightList)):
    itemList.append(Item(weightList[index],valueList[index]))
    

maxWeight = 5
knapsack.value = 0

print maxKnapsack(itemList, maxWeight)


















