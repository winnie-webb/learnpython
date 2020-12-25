speeds = [99,14,12,15]
def median(array) :
    arrayLength = len(array)
    
    if arrayLength % 2 == 0 :
        sub_median_1 = (arrayLength // 2)
        sub_median_2 = (arrayLength // 2) -1
        median = (array[sub_median_1] + array[sub_median_2]) // 2
        print(median)
    else :
        arrayMedian = array[arrayLength // 2]
        print(arrayMedian)
median(speeds)




