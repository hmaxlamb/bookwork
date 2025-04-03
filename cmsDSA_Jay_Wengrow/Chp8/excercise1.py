def main():
    arr1 = [1,2,3,4,5]
    arr2 = [3,4,6,0,8]
    arr = intersect(arr1, arr2)

    print(arr)

def intersect(arr1, arr2):
    index1 = {}
    inter = []

    for item in arr1:
        index1[item] = True
    
    for item in arr2:
        if index1.get(item, False):
            inter.append(item)
    
    return inter

main()