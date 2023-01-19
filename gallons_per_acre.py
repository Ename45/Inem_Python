import math

#prompt user to enter inch of rainfall
#Calculate rainfall volume
#Convert gallons to inches and multiply the rainfall volume

rain_inch = input("Enter amount of rainfall in inches: ")
rain_inch = int(rain_inch)

volume_of_rainfall = float (rain_inch * 0.623)

gallons_of_water_per_acre = volume_of_rainfall * 231
print("The total gallons of water is: ",gallons_of_water_per_acre)