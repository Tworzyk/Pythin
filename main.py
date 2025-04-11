import cmath

def solve_quadratic(a, b, c):
    # Calculate the discriminant
    d = cmath.sqrt(b**2 - 4*a*c)
    
    # Calculate the two solutions
    x1 = (-b + d) / (2*a)
    x2 = (-b - d) / (2*a)
    
    # Remove the imaginary part if it's zero
    if x1.imag == 0:
        x1 = x1.real
    if x2.imag == 0:
        x2 = x2.real
    
    return tuple(sorted([x1, x2], key=lambda x: (x.real, x.imag)))

try:
    a = float(input("Enter coefficient a: "))
    if a == 0:
        print("This is not a quadratic equation.")
    else:
        b = float(input("Enter coefficient b: "))
        c = float(input("Enter coefficient c: "))
        print(f"The solutions are: {solve_quadratic(a, b, c)}")
except ValueError:
    print("Invalid input. Please enter numeric values.")
