weight = 4.8   #input("What's the weight of the package?: ")

# Ground shipping
if weight <= 2:
  print (f"Ground Shipping {weight * 1.50 + 20}$")
elif weight <= 6:
  print (f"Ground shipping {weight * 3.00 + 20}$")  
elif weight <= 10:
  print (f"Ground shipping {weight * 4.00 + 20}$")  
elif weight > 10:      
  print (f"Ground shipping {weight * 4.75 + 20}$")  

# Premium Ground Shipping

premium_ground_shipping = "Ground Shipping Premium $125.00"
print (premium_ground_shipping)

# Drone shipping

if weight <= 2:
  print (f"Drone Shipping {weight * 4.50}$")
elif weight <= 6:
  print (f"Drone Shipping {weight * 9.00}$")  
elif weight <= 10:
  print (f"Drone Shipping {weight * 12.00}$")  
elif weight > 10:      
  print (f"Drone Shipping {weight * 14.25}$")  
