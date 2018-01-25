#Given an integer representing a given amount of change, write a 
#function to compute the total number of coins required to make 
#that amount of change. You can assume that there is always a 1 cent coin.
MAX_SIZE = 10000
def minMakeChangeRecur(c):
    print "For C :",c
    if c == 0:
        return 0
    
    minCoins = MAX_SIZE

    for coin in coinsList:
        #print "minCoins  c :",minCoins,c
        #print "coin :",coin
        if (c-coin) >= 0:
            currentMinCoins = minMakeChangeRecur(c-coin)
        
            if currentMinCoins < minCoins:
                minCoins = currentMinCoins
            
    print "minCoins for c :",(minCoins+1),c
    return minCoins + 1
    
    
#Bottom up dynamic programming solution.Iteratively compute number of coins for larger and larger amounts of change

def makeChange(c):

    cache = [0 for k in range(c+1)]
    #cache[0] =1
    #print cache
    for i in range(1,c+1):
        
        minCoins = MAX_SIZE
        
        #Try removing each coin from the total and see which requires the fewest extra coins
        for coin in coinsList:
            if (i-coin)>=0:
                currCoins = cache[i-coin] +1
                print "currCoins minCoins ",currCoins,minCoins
                if currCoins < minCoins:
                    minCoins = currCoins
                print "minCoins :",minCoins
        
        cache[i] = minCoins
        
        print cache
    return cache[c]


coinsList = [2,1]

print makeChange(4)

# Dynamic Programming Python implementation of Coin 
# Change problem
def count(S, m, n):
 
    # table[i] will be storing the number of solutions for
    # value i. We need n+1 rows as the table is constructed
    # in bottom up manner using the base case (n = 0)
    # Initialize all table values as 0
    table = [0 for k in range(n+1)]
    print table
    # Base case (If given value is 0)
    table[0] = 1
 
    # Pick all coins one by one and update the table[] values
    # after the index greater than or equal to the value of the
    # picked coin
    for i in range(0,m):
        for j in range(S[i],n+1):
            table[j] += table[j-S[i]]
 
    return table[n]
 
# Driver program to test above function
#arr = [2,1]

#x = makeChange(4)
#print (x)
def makeChangeUtils(c,cache):
    print "For C :",c
    print "cache :",cache
    if cache[c]>=0:
        return cache[c]
    
    minCoins =c
    
    for coin in coinsList:
        #print "minCoins  c :",minCoins,c
        #print "coin :",coin
        if (c-coin) >= 0:
            currentMinCoins = makeChangeUtils(c-coin, cache)
        
            if currentMinCoins < minCoins:
                minCoins = currentMinCoins
            
    print "minCoins for c :",(minCoins+1),c
    cache[c] = minCoins +1
    return cache[c]
    
def makeChangeDynamic(c):
    cache = [-1 for k in range(c+1)]
    print makeChangeUtils(c,cache)
    print cache
    
    
#print makeChangeDynamic(4)





def dynamicCoinChange( T, L ):

    cache = [0 for i in range(0, L+1)]
    n = len(T)
    for i in range(1, L+1):
        smallest = MAX_SIZE
        #for j in range(0, n):
        for coin in T:
            if (i-coin>=0):
                smallest = min(smallest, cache[i - coin]) 
                
        cache[i] = 1 + smallest 
    return cache[L]

T = [3,2,1]
L=12
#print dynamicCoinChange(T,L)








