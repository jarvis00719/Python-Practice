m_1 = [[1,2,3], 
       [4,5,6], 
       [7,8,9]]


def diagonal_find(arr):      
    arr_1 = []
    diag = []

    n = len(arr)
    for i in range(n):
        arr_1 = arr[i][i]
        diag.append(arr_1)
    return diag 
   

print(diagonal_find(m_1))


