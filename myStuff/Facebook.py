
'''
We have a list of various types of tasks to perform. Task types are identified with an integral identifier: task of type 1, task of type 2, task of type 3, etc. Each task takes 1 time slot to execute, and once we have executed a task we need cooldown (parameter) time slots to recover before we can execute another task of the same type.  However, we can execute tasks of other types in the meantime.  The recovery interval is the same for all task types. We do not reorder the tasks: always execute in order in which we received them on input. 

Given a list of input tasks to run, and the cooldown interval, output the minimum number of time slots required to run them.

algo :
check the task number in list
-if the task is new
---create a new operation map of task number and cool down period.
---increment the time slot by 1
----if there is any other task in pro
-if the task to be operated is in process list
---increament the time slot by cooldown period
---process the task. increment time slot by 1

'''
#Tasks: 1, 1, 2, 1
#Recovery interval (cooldown): 2
#Output: 7  (order is 1 _ _ 1 2 _ 1)

#Tasks: 1, 2, 3, 1, 2, 3
#Recovery interval (cooldown): 3
#Output: 7  (order is 1 2 3 _ 1 2 3)

def checkTaskStatus(taskCoolCounter):
    if taskCoolCounter == 0:
        return True
    else:
        return False
    

def calculateTimeSLot(taskList, coolDownInterval):
    globalTimeSlotCount = 0
    taskMap = {}
    outputList = set()
    for task in taskList:
        #all tasks are cooled
        taskMap[task] = 0
    
    for task in taskList:
        print "Task Map :"+str(taskMap)
        varInterval = 0
                
        if checkTaskStatus(taskMap[task]) is True:
            print 'a'
            #outputList.add(task)
            taskMap[task] = coolDownInterval 
            varInterval = 1
            globalTimeSlotCount = globalTimeSlotCount + varInterval
        else:
            print "b"
            #outputList.add(task)
            
            varInterval = taskMap[task] + 1
            taskMap[task] = coolDownInterval
            globalTimeSlotCount = globalTimeSlotCount + varInterval
        
        for taskInMap in taskMap:
            if task == taskInMap:
                taskMap[taskInMap] = coolDownInterval
            else:
                if (taskMap[taskInMap]- varInterval) < 0:
                    taskMap[taskInMap] = 0
                else:
                    taskMap[taskInMap] = taskMap[taskInMap]- varInterval
            
        
        print "globalTimeSlotCount  :"+str(globalTimeSlotCount)
    return globalTimeSlotCount



taskList = [1, 1, 2, 1]
coolDownInterval = 2
print calculateTimeSLot(taskList, coolDownInterval)


 /**
     * 
     * Given an array of n + 1 integers, where each element is between 1 and n
     * and all but one element is distinct. Find the duplicate number.
     * 
     * [ 4, -6, -1, -3, -2, -5, -5 ]
     * 
     * 1. Brute force
     *      - Maintain counters using hashtable, array, or a set
     * 2. Use sum of natural numbers
     *      - n * (n + 1) / 2 (numbers between 1 and n)
     *      - n * (n - 1) / 2 (numbers between 0 and n)
     * 3. Using fast and slow pointers using values as indices
     *      - slow = arr[slow]
     *      - fast = arr[arr[fast]]
     * 4. Negate values using indices, or change them to 0
     * 
     * 
     * Reverse all the words in a string
     *  - Different from reversing the entire string
     * 
     * Find the kth largest element in an unsorted array
     *  - Using quick select
     * 
     * 
     * */
    
    
    
