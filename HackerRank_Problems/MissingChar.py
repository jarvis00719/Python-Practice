

def missingcharacters(st):
    digits = ["0,1,2,3,4,5,6,7,8,9"]
    letters = ["a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,,v,w,x,y,z"]

    present = set(st)

    m_digits = [d for d in digits if d not in present]

    m_letters = [c for c in letters if c not in present]

    result = "".join(m_digits + m_letters)
    
    return result

s = input()

print(missingcharacters(s))