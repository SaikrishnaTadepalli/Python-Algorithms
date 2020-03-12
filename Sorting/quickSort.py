
def sort(collection):

    length = len(collection)
    
    if length <= 1:
        return collection
    else:
        pivot = collection.pop()
        greater, lesser = [], []

        for element in collection:
            if element > pivot:
                greater.append(element)
            else:
                lesser.append(element)

        return sort(lesser) + [pivot] + sort(greater)

print "Enter a list of numbers seperated by a comma: "
inputCol = raw_input(">>> ")

unsortedCol = [int(item) for item in inputCol.split(",")]

print sort(unsortedCol)