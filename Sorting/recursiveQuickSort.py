def sort(collection):

    if len(collection) <= 1:
        return collection
    else:
        return (
            sort([e for e in collection[1:] if e <= collection[0]])
            + [collection[0]]
            + sort([e for e in collection[1:] if e > collection[0]])
        )

print "Enter a list of numbers seperated by a comma: "
inputCol = raw_input(">>> ")

unsortedCol = [int(item) for item in inputCol.split(",")]

print sort(unsortedCol)