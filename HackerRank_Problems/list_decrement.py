x = [5, 8, 12, 9, 7]
y = [45, 58, 47, 26, 78]
res = []

def dec_list(arr):
    
    for i in arr:
       i -= 1
       res.append(i)             
    return res

    

print(dec_list(x))



