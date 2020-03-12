
def sort(collection):

    length = len(collection)

    for i in range(length - 1):
        least = i
    
        for k in range(i + 1, length):    
            if collection[k] < collection[least]:
                least = k
    
        if least != i:
            collection[least], collection[i] = (collection[i], collection[least])
    
    return collection

print "Enter a list of numbers seperated by a comma: "
inputCol = raw_input(">>> ")

unsortedCol = [int(item) for item in inputCol.split(",")]

print sort(unsortedCol)