#Sum of array singles
def repeats(arr):
    num = 0
    for x in arr:
        if arr.count(x) >1:
            pass
        else:
            num += x
    return num