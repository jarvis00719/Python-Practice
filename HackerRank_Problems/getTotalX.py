
# X (integer)- must be a multiple of a[i], for all I's 
#            - must be a factor of all b[i], for all I's   
# We need to find all such X's !!
import math

def getTotalx(a,b): 
    
    a_lcm = math.lcm(*a)
    b_hcf = math.gcd(*b)
    x = []

    for i in range(a_lcm, b_hcf, a_lcm):
        if b_hcf%i==0:
            x.append(i)
        return x



#Input Statements !!
multiple_input = list(map(int, input().split()))

n = multiple_input[0]
m = multiple_input[1]

a_arr = list(map(int, input().split()))
b_arr = list(map(int, input().split()))

print(getTotalx(a_arr,b_arr))