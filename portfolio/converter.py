def main():
    print("\t ************************************************* \n");
    print("\t * \t\t CNIT155 Assignment 02 \t\t *\n");
    print("\t * \t\t Conversion Calculator \t\t *\n");
    print("\t ************************************************* \n\n"); 
    # enter user's name
    username = input("Enter your full name:")
    print("My name is", username, "\n");
    
    #lb to kg conversion
    print("** 1st. Pounds to Kilograms conversion **");
    weight_lb = input("What is the weight in pounds to convert it to kilograms?:")
    #convert user input to float & limit to 2 decimal places
    format_lb = "{:.2f}".format(float(weight_lb))
    weight_kg = (float(weight_lb)/2.2046)
    format_kg = "{:.2f}".format(weight_kg)
    print("The weight entered in pounds is", format_lb, "lb and it is", format_kg, "kg\n");
    
    #c to f conversion
    print("** 2nd. Celsius to Farenheit conversion **");
    temp_c = input("Enter the Celsius temperature to convert it to Farenheit:")
    format_c = "{:.2f}".format(float(temp_c))
    temp_f = (float(temp_c)*9/5)+32
    format_f = "{:.2f}".format(temp_f)
    print("The entered temperature in Celsius is", format_c, "C and it is", format_f, "F\n");
    
    #mi to km conversion
    print("** 3rd. Miles to Kilometers conversion **");
    dist_mi = input ("Enter miles to convert it to kilometers:")
    format_mi = "{:.2f}".format(float(dist_mi))
    dist_km = (float(dist_mi)*1.609344)
    format_km = "{:.2f}".format(dist_km)
    print("The entered distance in miles is", format_mi, "mi and it is", format_km, "km\n");
    
    #ft & in to cm conversion
    print("** 4th. Feet and Inches to Centimeters conversion **");
    height_ft = input("What is your height in feet and inches?\nFeet?:")
    height_in = input("Inches?:")
    format_ft = "{:.2f}".format(float(height_ft))
    format_in = "{:.2f}".format(float(height_in))
    height_cm = (float(height_ft)*30.48)+(float(height_in)*2.54)
    format_cm = "{:.2f}".format(height_cm)
    print("The entered height is", format_ft, "ft and", format_in, "in and it is", format_cm, "cm");
main();
