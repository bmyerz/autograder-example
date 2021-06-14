# this is the sample solution to addone

def addone(ls):
    result = ls.copy()
    for i in range(len(result)):
        result[i] += 1
    return result
