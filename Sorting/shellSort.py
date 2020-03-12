
def sort(collection):
    gaps = [701, 301, 132, 57, 23, 10, 4, 1]

    for gap in gaps:
        i = gap
        while i < len(collection):
            temp = collection[i]
            j = i
            while j >= gap and collection[j - gap] > temp:
                collection[j] = collection[j - gap]
                j -= gap
            collection[j] = temp
            i += 1

    return collection

print "Enter a list of numbers seperated by a comma: "
inputCol = raw_input(">>> ")

unsortedCol = [int(item) for item in inputCol.split(",")]

print sort(unsortedCol)