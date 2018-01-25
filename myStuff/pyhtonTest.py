def binAdd(s1, s2):
    if not s1 or not s2:
        return ''

    maxlen = max(len(s1), len(s2))

    s1 = s1.zfill(maxlen)
    s2 = s2.zfill(maxlen)

    result  = ''
    carry   = 0

    i = maxlen - 1
    while(i >= 0):
        s = int(s1[i]) + int(s2[i])
        if s == 2: #1+1
            if carry == 0:
                carry = 1
                result = "%s%s" % (result, '0')
            else:
                result = "%s%s" % (result, '1')
        elif s == 1: # 1+0
            if carry == 1:
                result = "%s%s" % (result, '0')
            else:
                result = "%s%s" % (result, '1')
        else: # 0+0
            if carry == 1:
                result = "%s%s" % (result, '1')
                carry = 0   
            else:
                result = "%s%s" % (result, '0') 

        i = i - 1;

    if carry>0:
        result = "%s%s" % (result, '1')
    return result[::-1]
    
    
def binAddwithXor(s1,s2):
    if not s1 or not s2:
        return ''

    maxlen = max(len(s1), len(s2))

    s1 = s1.zfill(maxlen)
    s2 = s2.zfill(maxlen)

    result  = 0
    carry   = 0
    for i in range(maxlen-1,-1,-1):
        sum = int(s1[i])^int(s2[i])^int(carry)
        result = result + sum
        carry = (int(s1[i]) & int(s2[i])) | (int(s2[i]) & int(carry)) | (int(carry) & int(s1[i]))
        
    if carry:
        print(result)
    
    print(result)

s1 = '1101'
s2 = '111'

#res = binAdd(s1,s2)
#print(res)
binAddwithXor(s1,s2)