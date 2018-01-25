from collections import defaultdict
class TrieNode():
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.isWord = False
        self.sons = {}
        self.frequencyMap = {}
        
class Trie():
    def __init__(self):
        self.root = TrieNode()
        self.prefixList = []
        
    def insert(self, wordList):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: void
        """
        print wordList
        for word in wordList:
            currentNode = self.root
            for letter in word:
                
                if letter not in currentNode.sons:
                    currentNode.sons[letter] = TrieNode()
                    currentNode.frequencyMap[letter] = 0
                
                currentNode.frequencyMap[letter] += 1
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
                print currentNode.frequencyMap
                currentNode = currentNode.sons[letter]
            else:
                return False
        
        return currentNode.isWord
        
    def prefixGenerator(self, node, prefix):
        currentNode = node
        if (currentNode is None):
            return
        
        #prefix = ''
        if currentNode.sons:
            print "-----"
            print currentNode.sons
            print prefix
            print "......."
            for letter in currentNode.sons:
                currentPrefix = ''
                currentPrefix += letter
                print letter+str(" -letter")
                print currentNode.frequencyMap
                if currentNode.frequencyMap[letter] == 1:
                    self.prefixList.append(prefix+currentPrefix)
                    continue
               
                currentNode = currentNode.sons[letter]
                print str(currentNode.sons)+"  *****"
                self.prefixGenerator(currentNode, prefix+currentPrefix)

        
        
inputList = ['zeebra', 'dog', 'duck', 'dove',]
inList1 = ['geeksforgeeks', 'geeks', 'geek', 'geezer']
trieObj = Trie()
trieObj.insert(inputList)
print(trieObj.search('geezer'))
#Output: {z, dog, du, dov}
#longest prefix matching
trieObj.prefixGenerator(trieObj.root, '')
print trieObj.prefixList