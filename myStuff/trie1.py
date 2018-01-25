class TrieNode(object):
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.isWord = False
        self.sons = {}
        self.labelCount = {}
        

class Trie(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()
        

    def insert(self, wordList):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: void
        """
        
        for word in wordList:
            currentNode = self.root
            for letter in word:
                if letter not in currentNode.sons:
                    currentNode.sons[letter]= TrieNode()
                    currentNode.labelCount[letter]= 1
                else:
                    #since letter is there then update its count
                    currentNode.labelCount[letter]= currentNode.labelCount[letter] + 1
                #now point to the next node we just created. which is the son or children
                #print "---"+letter+"--->"+str(currentNode.labelCount[letter])
                currentNode = currentNode.sons[letter]
                
                
        
            currentNode.isWord = True
        

    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        currentNode = self.root
        for letter in word:
            if letter in currentNode.sons:
                currentNode = currentNode.sons[letter]
            else:
                return False
        
        return currentNode.isWord

    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        currentNode = self.root
        for letter in prefix:
            if letter not in currentNode.sons:
                return False
            else:
                currentNode = currentNode.sons[letter]
        return True

    def generatePrefix(self):
        currentNode = self.root
        prefixList = []
        index = 0
        prefix = ''
        for letter in currentNode.sons:
            print letter
            #if currentNode.labelCount[letter] ==1:
               # prefixList[index] = letter
                #index = index +1
            #else:
               # prefixList[index] = letter
            currentNode = currentNode.sons[letter]
    

inputList = ['zebra', 'dog', 'duck', 'dove']
#Output: {z, dog, du, dov}
trieObj = Trie()
trieObj.insert(inputList)
#print(trieObj.search('dove'))
trieObj.generatePrefix()