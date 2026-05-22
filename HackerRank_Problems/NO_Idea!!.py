###__Variables_used __###
# n(no. of elemnts_in array), m(no of elements in A,B sets)
# arr = n number of integers  
#A - m number of elements
#B - m number of elements

##-----------------------------------##

## Input Statements !!
arr, sets = list(map(int, input().split()))
int_values_arr = list(map(int, input().split()))

A_set = set(map(int, input().split())) 
B_set = set(map(int, input().split()))
happy = 0

for i in int_values_arr:

    if i in A_set:
        happy+=1
    elif i in B_set:
        happy-= 1

print(happy)