# Startedat 3.05. End at 3.35.

#row = [0,0,1,0,0,1,0,1,0,0] -> 2
#max = [1,0,1,0,0,1,0,1,0,1]

def fillSeats(inputRowList):
    
    rowLength = len(inputRowList)
    oldCount = 0
    newCount = 0
    for people in inputRowList:
        if people ==1:
            oldCount +=1
    #print(oldCount)
    
    if inputRowList[0] ==0 or inputRowList[rowLength-1] == 0:
        if inputRowList[1]==0:
            inputRowList[0] = 1
        if inputRowList[rowLength-2] == 0:
            inputRowList[rowLength-1] = 1
            
    #print(inputRowList)
    
    
    for rowIndex in range(0, rowLength):
        #print "row Index : "+str(rowIndex)
        if rowIndex == 0 or (rowLength-1)==0:
            #print "test 1 "+str(rowIndex)
            continue
        else:
            #print "test 2 "+str(rowIndex)
            #print inputRowList[rowIndex]
            if inputRowList[rowIndex] == 1:
                #print "test 3"
                continue
            else:
                #print "test 4"
                if inputRowList[rowIndex-1] ==0 and inputRowList[rowIndex+1] == 0:
                    #print "test 5"
                    inputRowList[rowIndex] = 1
                else:
                    #print "test 6"
                    continue
            
    print(inputRowList) 
    for people in inputRowList:
        if people ==1:
            newCount +=1
    
    return newCount-oldCount
    
    
inputRow = [0,0,1,0,0,1,0,1,0,0]
inputRow1 =[1,0,0,0,0,0,0,0,0,1]
inputRow2 = [0,0,0,0,0,0,0,0,0,0]
inputRow3 = [0,0,0,0,0,0,0,0,0,0]

    
print(fillSeats(inputRow2))