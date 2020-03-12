
def sort(collection):

    length = len(collection)

    for i in range(length):
            
        for j in range (0,length -1 -i):
            
            if collection[j] > collection[j+1]:
                collection[j],collection[j+1] = collection[j+1], collection[j]
            

    return collection

print "Enter a list of numbers seperated by a comma: "
inputCol = raw_input(">>> ")

unsortedCol = [int(item) for item in inputCol.split(",")]

print sort(sort(unsortedCol))