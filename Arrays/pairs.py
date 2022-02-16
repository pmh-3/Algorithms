# find number of pairs that result in given difference

def pairs(k, arr):
    # determine values that result in a pair for each value in array
    # check if array contains those values
    arr = set(arr)
    pairs = 0
    for val in arr:
        diff = val-k
        
        if diff in arr:
            pairs += 1

    return pairs