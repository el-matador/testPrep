import math

def generatePrimeNum(evenNum):
    listOfPrimes = []
    for num in range(2,evenNum + 1):
        
        for i in range(2,num):
            if (num % i) == 0:
                    break
        else:
            #print(num)
            listOfPrimes.append(num)
    
    return listOfPrimes
           
def simpleSieve(sieveSize):
    #creating Sieve.
    sieve = [True] * (sieveSize+1)
    # 0 and 1 are not considered prime.
    sieve[0] = False
    sieve[1] = False
    for i in xrange(2,int(math.sqrt(sieveSize))+1):
        if sieve[i] == False:
            continue
        for pointer in xrange(i**2, sieveSize+1, i):
            sieve[pointer] = False
    # Sieve is left with prime numbers == True
    primes = []
    for i in xrange(sieveSize+1):
        if sieve[i] == True:
            primes.append(i)
    return primes



def calculatePrimeSum(listOfPrimes, evenNum):
    lenList = len(listOfPrimes)
    primePairDict = {}
    for i in range(0,lenList):
        if (evenNum - listOfPrimes[i]) in listOfPrimes:
            primePairDict[listOfPrimes[i]] = evenNum - listOfPrimes[i]
            
    return primePairDict

int Solution::isPrime(int n) {
    if (n < 2) return 0;
    int upperLimit = (int)(sqrt(n));
    for (int i = 2; i <= upperLimit; i++) {
        if (i < n && n % i == 0) return 0;
    }
    return 1;
}

def isPrime(self, A):

	    if A<2:
	        return 0
	    upperLimit = int(A**0.5)
	    for i in xrange(2, upperLimit + 1):
		    if i < A and A % i == 0:
			    return 0
	    return 1

#n1 = 18
#n2 = 1048574
#resList = generatePrimeNum(n1)
#resList = simpleSieve(n2)
#print(resList)
#resDict = calculatePrimeSum(resList,n2)
#print(resDict)
#print(min(resDict))
#print(resDict[min(resDict)])