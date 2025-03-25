import statistics
def calculate_median(stream):
    list = []
    for i in stream:
        median = (i+1)/2
        list.append(median)
    return list

print(calculate_median([1, 2, 3, 4, 5]))

        
        