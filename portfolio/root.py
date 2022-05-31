import math;
def main():
    #promt user to input coefficients
    a = float(input("Enter the coefficient a:"))
    b = float(input("Enter the coefficient b:"))
    c = float(input("Enter the coefficient c:"))
    
    #execute quadratic equation with coefficients provided by user
    print("\n Quadratic Equation is:", a, "*X^2 +", b,"*X +", c, "= 0\n");
    
    #discriminant formula
    d = ((b)**2)-(4*((a)*(c)))
    #format discriminant to 2 decimal places 
    format_d = "{:.2f}".format(d)
    print("The Discriminant is:", format_d, "\n")
    
    #quadratic equation separated into positive and negative
    x1 = (-b+((b**2)-4*a*c)**(1/2))/(2*a)
    x2 = (-b-((b**2)-4*a*c)**(1/2))/(2*a)
    root = ((-b)/(2*a))
    
    #if statement separating different number of solutions for each scenario
    if d>0:
        format_x1 = "{:.2f}".format(x1)
        format_x2 = "{:.2f}".format(x2)
        print("The equation has two real roots:", format_x1, "and", format_x2, "\n")
    elif d==0:
        format_root = "{:.2f}".format(root)
        print("The equation has only one root:", format_root, "\n")
    else:
        print("The equation has no real roots. \n")
        
    #if statement to determine smallest coefficient
    if (a<b) and (a<c):
        smallest = a
    if (b<a) and (b<c) :
        smallest = b
    if (c<a) and (c<b) :
        smallest = c
    
    format_smallest = "{:.2f}".format(smallest)
    
    print("The smallest coefficient is:", format_smallest)
    
main();