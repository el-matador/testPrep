class Solution:
    # @return a string
    def longestCommonPrefix(self, strs):
        print len(strs)
        retList = []
        if len(strs) == 0:
            return

        longest = len(strs[0])  # use the first string as the base
        print longest
        for string in strs[1:]:
            # Compute the new longest common prefix of current string
            # and longest common prefix so far from previous rounds
            index = 0
            #print string
            while index < len(string) and (index < longest) and (strs[0][index] == string[index]):
                index += 1
            longest = min(index, longest)
        retList.append(strs[0][:longest])
        print retList
        
        
inputList = ['zebra', 'dog', 'duck', 'dove']
solObj = Solution()

print solObj.longestCommonPrefix(inputList)
