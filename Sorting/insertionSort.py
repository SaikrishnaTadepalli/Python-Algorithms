
def sort(collection):

    for loop_index in range(1, len(collection)):
        insertion_index = loop_index
        while (
            insertion_index > 0
            and collection[insertion_index - 1] > collection[insertion_index]
        ):
            collection[insertion_index], collection[insertion_index - 1] = collection[insertion_index - 1],collection[insertion_index]
            insertion_index -= 1

    return collection

print "Enter a list of numbers seperated by a comma: "
inputCol = raw_input(">>> ")

unsortedCol = [int(item) for item in inputCol.split(",")]

print sort(unsortedCol)