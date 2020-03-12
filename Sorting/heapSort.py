
def createHeap(collection, index, heapSize):
    largest = index
    left = 2 * index + 1
    right = 2 * index + 2

    if left < heapSize and collection[left] > collection[largest]:
        largest = left

    if right < heapSize and collection[right] > collection[largest]:
        largest = right

    if largest != index:
        collection[largest], collection[index] = collection[index], collection[largest]
        createHeap(collection, largest, heapSize)

def sort(collection):

    length = len(collection)

    for i in range(length // 2 - 1, -1, -1):
        createHeap(collection, i, length)

    for i in range(length - 1, 0, -1):
        collection[0], collection[i] = collection[i], collection[0]
        createHeap(collection, 0, i)

    return collection

print "Enter a list of numbers seperated by a comma: "
inputCol = raw_input(">>> ")

unsortedCol = [int(item) for item in inputCol.split(",")]

print sort(unsortedCol)