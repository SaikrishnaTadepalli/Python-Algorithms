
def sort(collection):
    
    writes = 0
 
    for i, item in enumerate(collection):
 
        pos = i
        for item2 in collection[i + 1:]:
            if item2 < item:
                pos += 1
 
        if pos == i:
            continue
 
        while item == collection[pos]:
            pos += 1

        collection[pos], item = item, collection[pos]
        writes += 1
 
        while pos != i:

            pos = i
            for item2 in collection[i + 1:]:
                if item2 < item:
                    pos += 1

            while item == collection[pos]:
                pos += 1
                
            collection[pos], item = item, collection[pos]
            writes += 1
 
    return collection

print "Enter a list of numbers seperated by a comma: "
inputCol = raw_input(">>> ")

unsortedCol = [int(item) for item in inputCol.split(",")]

print sort(unsortedCol)