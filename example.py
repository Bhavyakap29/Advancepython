# calculate simple intrest
def simple_intrest(p: float|int, n: int, r: float|int) ->tuple:
    """
    p: principal in INR
    n: number of years
    r: rate of intrest in percent per annum 
    output intrest, amount
    """
    i = (p*n*r)/100
    a = p + i
    return i,a
# Take p,n,r as input from user 
p = float(input("Please enter principal in INR: "))
n = int(input("Please enter number of years: "))
r = float(input("Please enter rate of intrest in %p.a. : "))

# call the simpple intrest function
i,a = simple_intrest(p,n,r)

# print the intrest and amount
print(f"simple intrest : {i:.2f} INR")
print(f"amount : {a:.2f} INR")