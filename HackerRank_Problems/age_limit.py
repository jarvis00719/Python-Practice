
name = 'john'
age = int(input('Enter your age: '))

age_limit = (age >= 18)

if age_limit:
    print(f"Hello {name}, you're eligible!" )
else:
    print(f"Sorry {name}, you're below age limit!")



"""Age Limit Function:-
def age_limit(age):
    if(age >= 18): 
        return "Eligible"
    else:
        return "Not Elgible"
    
age = int(input("Enter Age: "))

print(age_limit(age)) """