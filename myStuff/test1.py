#Find shortest unique prefix to represent each word in the list.
#Input: [zebra, dog, duck, dove]
#Output: {z, dog, du, dov}


def prefix(A):
        tree = [0, {}]
        #print tree
        for s in A:
            node = tree
            node[0] += 1
            print s
            for c in s:
                node = node[1].setdefault(c, [0, {}])
                node[0] += 1
                print node
                
            print "----"
            #print node
            print "*****"
        l = []
        for s in A:
            prefix = ''
            node = tree
            for c in s:
                if node[0] <= 1:
                    l.append(prefix)
                    break
                prefix += c
                node = node[1][c]
            else:
                l.append(s)
            print l
        return l
        
A = ['zebra', 'dog', 'duck', 'dove']

print(prefix(A))