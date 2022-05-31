import math;
def main():
    print("\t * \t Area and Volume Calculators \t *\n")
    print("\t ========================================= \n\n");
    
    print("A. Area Of A Rectangle \nB. Area Of A Trapezoid \nC. Volume Of A Sphere \nD. Volume Of A Hexagonal Pyramid \nE. Volume Of An Octagonal Prism")
    
    user_input = input("Choose one of the following options to calculate:\n")
    
    if (user_input == "A"):
        print("\nOption A. Area Of A Rectangle\n")
        w = float(input("Enter the width of the rectangle:"))
        l = float(input("Enter the length of the rectangle:"))
        
        area_rec = w*l
        format_area_rec = "{:.2f}".format(area_rec)
        print("\nThe area of the rectangle is", format_area_rec)
        
    if (user_input == "B"):
        print("\nOption B. Area Of A Trapezoid\n")
        w = float(input("Enter the short base of the trapezoid:"))
        l = float(input("Enter the long base of the trapezoid:"))
        h = float(input("Enter the height of the trapezoid:"))
        
        area_trap = ((w+l)/2)*h
        format_area_trap = "{:.2f}".format(area_trap)
        print("\nThe area of the trapezoid is", format_area_trap)
        
    if (user_input == "C"):
        print("\nOption C. Volume Of A Sphere\n")
        r = float(input("Enter the radius of the sphere:"))
        
        vol_sphere = (4/3)*3.141592653589793*(r**3)
        format_vol_sphere = "{:.2f}".format(vol_sphere)
        print("\nThe volume of the sphere is", format_vol_sphere)
        
    if (user_input == "D"):
        print("\nOption D. Volume Of A Hexagonal Pyramid\n")
        l = float(input("Enter the base edge of the hexagonal pyramid:"))
        h = float(input("Enter the height of the hexagonal pyramid:")) 
        
        vol_hex = ((3**(1/2))/2)*(l**2)*h
        format_vol_hex = "{:.2f}".format(vol_hex)
        print("\nThe volume of the hexagonal pyramid is", format_vol_hex)
        
    if (user_input == "E"):
        print("\nOption E. Volume Of An Octagonal Prism\n")
        l = float(input("Enter the base edge of the octagonal pyramid:"))
        h = float(input("Enter the height of the octagonal pyramid:"))
        
        vol_oct = 2*(1+2**(1/2))*l**2*h
        format_vol_oct = "{:.2f}".format(vol_oct)
        print("\nThe volume of the octagonal pyramid is", format_vol_oct)
        
    else:
        print("Invalid input! \nPlease enter your choice between A and E.")
        return()
    
        
main();