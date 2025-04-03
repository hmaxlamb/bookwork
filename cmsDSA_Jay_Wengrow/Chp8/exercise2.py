def main():
    arr = [1,2,3,3,4,5,2]
    item = find_first_dupe(arr)
    print(item)

def find_first_dupe(list):
    index = {}
    
    for item in list:
        if (index.get(item, False)):
            return item
        else:
            index[item] = True
    
    return None


main()