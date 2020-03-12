
def merge(left, right):
    result = []

    while left and right:
        result.append((left if left[0] <= right[0] else right).pop(0))
    
    return result + left + right

def sort(collection):    

    if len(collection) <= 1:
        return collection

    mid = len(collection) // 2
    
    return merge(sort(collection[:mid]),sort(collection[mid:]))


print "Enter a list of numbers seperated by a comma: "
inputCol = raw_input(">>> ")

unsortedCol = [int(item) for item in inputCol.split(",")]

print sort(unsortedCol)