#Implement an algorithm to determine if a string has all unique characters. What if you can not use additional data structures

#Create a map of all charaters and set it to True
#If we are allowed to destroy the input string, we could sort the string in O(n log n) time and 
#then linearly check the string for neighboring characters that are identical. 
#Care- ful, though - many sorting algorithms take up extra space.
import ctc_string_1_2 as test

def ifStringIsUnique(stringInput):
	print "Characters in string uniquie ? :"
	charList = []
  	for char in stringInput:
  		if char in charList:
  			return False
  		else:
  			charList.append(char)
  	return True


def reverseString(inputString):
	print "Print the reversed string of : "+inputString
	l = len(inputString)
	reversedString = ''
	for i in range(l-1,-1,-1):
		reversedString += inputString[i]

	return reversedString

def isPalindrome(inputString):
	if inputString == reverseString(inputString):
		return True
	else:
		return False


inputText= "abcba"
print(isPalindrome(inputText))


