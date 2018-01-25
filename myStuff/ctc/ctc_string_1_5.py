# Check if the two strings have identical counts for each unique char.
#aaabcd abcd 

def check_permutation(str1, str2):
    if len(str1) != len(str2):
        return False
    counter = dict()
    for c in str1:
        counter[c] +=1
    for c in str2:
        if counter[c] == 0:
            return False
        counter[c] -= 1
    return True




str1 = "krishna"
str2 = "riskhan"

print check_permutation(str1, str2)

