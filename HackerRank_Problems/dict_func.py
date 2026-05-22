
names = ['john', 'ala', 'ilia', 'sudan', 'mercy'] #keys
marks = [100, 200, 150, 80, 300] #values
d ={}

    
def create_dict(arr,arr2):
    for i in range(len(arr)):
        d[arr[i]] = arr2[i]
    return d


print(create_dict(names,marks))    

