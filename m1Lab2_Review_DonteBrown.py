# Donte Brown
# 1/26/2025
# M1Lab2
# Calculate fastest route for intercampus shuttle
'''
Get distance and speed for each route from user
Calculate time in minutes for each route
Keep track of fastest route and time
Continue getting routes until user is done
Display fastest route and time at end
'''

run_again = "yes"
fastest_route = 0
fastest_time = float('inf')
route_num = 1

# While loop begins here
while run_again == "yes":
    # Get distance from user
    distance = float(input(f"Enter route {route_num} distance (miles): "))
    
    # Prompt user to re enter if invalid
    if distance < 0:
        print("Distance must be positive")
        distance = float(input(f"Enter route {route_num} distance (miles): "))
    
    # Get speed from user    
    speed = float(input(f"Enter route {route_num} speed (miles/hour): "))
    
    # Prompt user to re enter if invalid
    if speed < 0:
        print("Speed must be positive")
        speed = float(input(f"Enter route {route_num} speed (miles/hour): "))
    
    # Calculate time in minutes
    time = (distance / speed) * 60
    
    # Check if this is the fastest route
    if time < fastest_time:
        fastest_time = time
        fastest_route = route_num
    
    # Ask to continue    
    run_again = input("More routes (y/n)? ")
    if run_again.lower() == "y":
        run_again = "yes"
    else:
        run_again = "no"
    route_num += 1

# Display results
if fastest_route > 0:
    print(f"Route {fastest_route} is fastest; {int(fastest_time)} minutes")

print("Program has been terminated.")