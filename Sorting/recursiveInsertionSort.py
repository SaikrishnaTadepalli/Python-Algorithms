
#from typing import List


def sort(collection, n):

    if len(collection) <= 1 or n <= 1:
        return

    nextInsert(collection, n - 1)
    sort(collection, n - 1)

    return collection

def nextInsert(collection, index):

    if index >= len(collection) or collection[index - 1] <= collection[index]:
        return

    collection[index - 1], collection[index] = collection[index],collection[index - 1]    
    
    nextInsert(collection, index + 1)

print "Enter a list of numbers seperated by a comma: "
inputCol = raw_input(">>> ")

unsortedCol = [int(item) for item in inputCol.split(",")]

print sort(unsortedCol,len(unsortedCol))