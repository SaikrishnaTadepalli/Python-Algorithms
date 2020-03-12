
def sort(collection):

    for i, num in enumerate(collection):
        try:
            if collection[i + 1] < num:
                collection[i] = collection[i + 1]
                collection[i + 1] = num
                sort(collection)
        except IndexError:
            pass
    return collection

print "Enter a list of numbers seperated by a comma: "
inputCol = raw_input(">>> ")

unsortedCol = [int(item) for item in inputCol.split(",")]

print sort(unsortedCol)