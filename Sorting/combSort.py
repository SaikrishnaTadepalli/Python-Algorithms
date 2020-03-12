
def sort(collection): 
    
    length = len(collection)   
    gap = length
    swapped = True

    while gap !=1 or swapped == 1: 
        gap = getNextGap(gap) 
        swapped = False
        
        for i in range(0, length-gap): 
            if collection[i] > collection[i + gap]: 
                collection[i], collection[i + gap]=collection[i + gap], collection[i] 
                swapped = True

    return collection

def getNextGap(gap): 
    gap = (gap * 10)/13

    if gap < 1: 
        return 1
    return gap

print "Enter a list of numbers seperated by a comma: "
inputCol = raw_input(">>> ")

unsortedCol = [int(item) for item in inputCol.split(",")]

print sort(sort(unsortedCol))