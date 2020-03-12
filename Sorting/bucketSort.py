
defaultBucketSize = 5

def sort(collection, bucketSize=defaultBucketSize):
    if len(collection) == 0:
        raise Exception("Please add some elements in the array.")

    minVal, maxVal = (min(collection), max(collection))
    bucket_count = (maxVal - minVal) // bucketSize + 1
    buckets = [[] for _ in range(int(bucket_count))]

    for i in range(len(collection)):
        buckets[int((collection[i] - minVal) // bucketSize)].append(collection[i])

    return sorted(
        [buckets[i][j] for i in range(len(buckets)) for j in range(len(buckets[i]))]
    )


print "Enter a list of numbers seperated by a comma: "
inputCol = raw_input(">>> ")

unsortedCol = [int(item) for item in inputCol.split(",")]

print sort(unsortedCol)