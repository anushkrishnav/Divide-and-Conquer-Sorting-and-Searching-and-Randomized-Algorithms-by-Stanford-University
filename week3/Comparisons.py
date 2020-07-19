def median-of-three(x):
    pass
def countComparisonsWithLast(x):
    """ Counts number of comparisons while using Quick Sort with last element of unsorted array as pivot """
    global count_pivot_last
    if len(x) == 1 or len(x) == 0:
        return x
    else:
        count_pivot_last += len(x)-1
        x[0],x[-1] = x[-1],x[0]
        i = 0
        for j in range(len(x)-1):
            if x[j+1] < x[0]:
                x[j+1],x[i+1] = x[i+1], x[j+1]
                i += 1
        x[0],x[i] = x[i],x[0]
        first_part = countComparisonsWithLast(x[:i])
        second_part = countComparisonsWithLast(x[i+1:])
        first_part.append(x[i])
        return first_part + second_part
def countComparisonsWithfirst(x):
    """ Counts number of comparisons while using Quick Sort with last element of unsorted array as pivot """
    global count_pivot_last
    if len(x) == 1 or len(x) == 0:
        return x
    else:
        count_pivot_last += len(x)-1
        i = 0
        for j in range(len(x)-1):
            if x[j+1] < x[0]:
                x[j+1],x[i+1] = x[i+1], x[j+1]
                i += 1
        x[0],x[i] = x[i],x[0]
        first_part = countComparisonsWithLast(x[:i])
        second_part = countComparisonsWithLast(x[i+1:])
        first_part.append(x[i])
        return first_part + second_part

if __name__ == "__main__":
    #f = open("QuickSort.txt", "r")
    #a=[int(text) for text in f]
    a=[10, 7, 8, 9, 1, 5]
    count_pivot_last=0
    b=countComparisonsWithfirst(a)
    print(b)
    
     