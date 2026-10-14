"""HarborFlow Assignment 1 starter file.

Replace the TODO sections with your team's implementation. Keep the program
entry point so the file can be run with: python harborflow_app.py
"""

def validate_booking(): # DO WE NEED ANOTHER FUNCTION TO PASS AN ARG THROUGH??

    booking_ref = (input("\nBooking reference: ").strip()).upper()
    
    while len(booking_ref) != 12 or (booking_ref[3] and booking_ref[7]) != "-" or not(booking_ref[4:7].isalpha()) or not(booking_ref[8:12].isdigit()) or booking_ref[:3] != "HFL":
        print("Invalid booking reference.")
        booking_ref = (input("\nBooking reference: ").strip()).upper()
    

    print("Valid booking reference:", booking_ref)
    return booking_ref


def calculate_quote(distance, weight, service_code):
    # Sets the service multiplier
    if service_code == "S":
        service_multiplier = 1.0
    elif service_code == "X":
        service_multiplier = 1.25
    elif service_code == "P":
        service_multiplier = 1.60

    # Calculates the quote
    subtotal = 45.0 + distance * 6.50 + weight * 4.00
    quote = subtotal * service_multiplier
    return quote

# Asks for inputs used to calculate quotes
def input_calculate_quote(): 
    distance = float(input("Distance (km): "))
    while distance <= 0: # Distance must be greater than 0
        print("Error - Value must be greater than zero.")
        distance = float(input("Distance (km): "))

    weight = float(input("Weight (kg): "))
    while weight <= 0: # Weight must be greater than 0
        print("Error - Value must be greater than zero.")
        weight = int(input("Weight (kg): "))

    service_code = (input("Service code: ")).upper()
    while service_code not in ["S","X","P"]: # Service code must be S, X or P
        print("Error - Service code must be S, X or P.")
        service_code = (input("Service code: ")).upper()

    quote = calculate_quote(distance, weight, service_code) # Defines quote by calling this function

    print(f"Delivery quote: {quote:.2f} SEK")

       
def parcel_labels():
    scanned_labels = input("Scanned labels: ").upper()
    scanned_labels = scanned_labels.split(",") # Seperate scanned labels into a list
    load_list = [] # Creates an empty list

    # Checks for unique labels and adds them to the list
    for label in scanned_labels: 
        if label.strip() not in load_list:
            load_list += [label.strip()]

    count = 0

    # Counts the number of labels and prints them in order
    for item in load_list: 
        count += 1
        print(f"{count}. {item}")
    print(f"Total unique parcels: {count}")

    
def van_capcity():
    van_capacity = float(input("Van capacity (kg): "))
    while van_capacity <= 0: # Check if value is invalid
        print("Error - Value must be greater than zero.")
        van_capacity = float(input("Van capacity (kg): "))

    parcel_weights = input("Parcel weights (kg): ")
    parcel_weights = (parcel_weights.split(",")) # Seperate parecel weights into a list    

    # Check parcel weights (make sure all are greater than 0)
    valid = False
    while not valid:
        valid = True
        for parcel in parcel_weights: # Run through each individual parcel weight
            if float(parcel.strip()) <= 0: # If weight is invalid...
                valid = False
                print("Error - All values must be greater than zero.")
                parcel_weights = input("Parcel weights (kg): ")
                parcel_weights = parcel_weights.split(",") # Seperate parecel weights into a list     
            
    count_parcel = 0
    parcels_accepted = 0
    loaded_weight = 0

    for parcel in parcel_weights: # Run through each individual parcel weight
        parcel = float(parcel.strip())
        count_parcel += 1

        if (van_capacity - parcel) >= 0: # If the parcel is compatible with the remaining capacity
            print(f"Parcel {count_parcel}: ACCEPTED")
            parcels_accepted += 1
            van_capacity -= parcel
            loaded_weight += parcel
        else: # If the parcel is too heavy
            print(f"Parcel {count_parcel}: REJECTED")

    print(f"Accepted parcels: {parcels_accepted}")
    print(f"Loaded weight: {loaded_weight:.2f} kg")
    print(f"Remaining capacity: {van_capacity:.2f} kg")

# Input delivery time and damaged parcels and check for validity
def classify_performance():
    # Each variable has to be 0 or above
    promised_minutes = int(input("Promised minutes: "))
    while promised_minutes < 0:
        print("Invalid input.")
        promised_minutes = int(input("Promised minutes: "))

    actual_minutes = int(input("Actual minutes: "))
    while actual_minutes < 0:
        print("Invalid input.")
        actual_minutes = int(input("Actual minutes: "))

    damaged_parcels = int(input("Damaged parcels: "))
    while damaged_parcels < 0:
        print("Invalid input.")
        damaged_parcels = int(input("Damaged parcels: "))

    # Categorize service status
    delay = actual_minutes - promised_minutes
    if damaged_parcels > 0:
        status = "SERVICE FAILURE"
    elif delay <= 0:
        status = "ON TIME"
    elif delay <= 15:
        status = "MINOR DELAY"
    else:
        status = "MAJOR DELAY"

    print(f"Delay: {delay} minutes")
    print(f"Service status: {status}")

def calculate_produce_report(completed_deliveries, daily_target):
    #Creates lists and defines variables
 deliveries_list = []
 mapped_deliveries = []
 days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
 total = 0
 count_deliveries = 0
    
    #Adds deliveries to a list and adds days mapped to deliveries to another list
    #Count_deliveries is a postion for the items in days
 for deliveries in completed_deliveries:
    deliveries = deliveries.strip()
    deliveries_list.append(int(deliveries))
    mapped_deliveries += [[days[count_deliveries], int(deliveries)]]
    deliveries = int(deliveries)
    #Counts how many deliveries in total and calculates average
    count_deliveries += 1
    total += deliveries
 average_deliveries = total/7
    
 #Find highest and lowest day
 highest_day = ""
 highest_count = -1
 lowest_day = ""
 lowest_count = 100   
 for days, deliveries in mapped_deliveries:     
    if deliveries > highest_count:
        highest_count = deliveries
        highest_day = days

    if deliveries < lowest_count:
                lowest_count = deliveries
                lowest_day = days
 count_target = 0
                    
 for deliveries in deliveries_list:
    if deliveries >= daily_target:
        count_target +=1
 return total, average_deliveries, highest_day, highest_count, lowest_day, lowest_count, count_target


def produce_report():
 completed_deliveries = input("Completed deliveries: ").split(",")

    # Keep asking until we get exactly 7 positive integers 
 while len(completed_deliveries) != 7 or not all(deliveries.strip().isdigit() for deliveries in completed_deliveries):
    print("Error - Weekly report requires 7 delivery counts.")
    completed_deliveries = input("Completed deliveries: ").split(",")

    #Number of days matching or above target
 daily_target = int(input("Daily target: "))
 while daily_target < 0:
    print("Error - Daily target must be non-negative.")
    daily_target = int(input("Daily target: "))

 total, average_deliveries, highest_day, highest_count, lowest_day, lowest_count, count_target = calculate_produce_report(completed_deliveries, daily_target)
 print("\nWeekly dispatch report")
 print(f"Total deliveries: {total}")
 print(f"Average per day: {average_deliveries:.2f}")
 print(f"Highest day: {highest_day} ({highest_count})")
 print(f"Lowest day: {lowest_day} ({lowest_count})")
 print(f"Days meeting target: {count_target}")

def compare_service():
    distance = float(input("Distance (km): "))
    while distance <= 0:
        print("Value must be greater than zero")
        distance = float(input("Distance (km): "))

    weight = float(input("Weight (kg): "))
    while distance <= 0:
        print("Value must be greater than zero")
        weight = float(input("Weight (kg): "))

    print("Service comparison")

    price_s = calculate_quote(distance, weight, "S")
    price_x = calculate_quote(distance, weight, "X")
    price_p = calculate_quote(distance, weight, "P")

    print(f"Standard: {price_s:.2f} SEK")
    print(f"Express: {price_x:.2f} SEK")
    print(f"Priority: {price_p:.2f} SEK")

    #Determine cheapest service
    if price_s <= price_x and price_s <= price_p:
        cheapest = "Standard"
    elif price_x <= price_s and price_x <= price_p:
        cheapest = "Express"
    else:
        cheapest = "Priority"

    # Determine most expensive service
    if price_s >= price_x and price_s >= price_p:
        most_expensive = "Standard"
    elif price_x >= price_s and price_x >= price_p:
        most_expensive = "Express"
    else:
        most_expensive = "Priority"

    print(f"Cheapest service: {cheapest}")
    print(f"Most expensive service: {most_expensive}")

def main():
    """Run the HarborFlow Dispatch Console."""

    choice = "0"

    # Repeatedly print menu until choice is 1
    while choice != "1":

        # Print menu
        print("\nHARBORFLOW DISPATCH CONSOLE")
        print("1. Close console")
        print("2. Validate booking reference")
        print("3. Calculate delivery quote")
        print("4. Consolidate parcel labels")
        print("5. Check van capacity")
        print("6. Classify service performance")
        print("7. Produce weekly dispatch report")
        print("8. Compare service scenarios")
        choice = input("Select service: ")

        # Check for invalid choice
        while choice not in ["1","2","3","4","5","6","7", "8"]:
            print("Error - Select a service from 1 to 8.")
            choice = input("Select service: ")

        # Call functions for each choice
        if choice=="2":         
            booking_reference = validate_booking()

        elif choice=="3":
            input_calculate_quote() 

        elif choice=="4":
            parcel_labels()

        elif choice=="5":
            van_capcity()

        elif choice=="6":
            classify_performance()

        elif choice=="7":
            produce_report()

        elif choice=="8":
            compare_service()

    print("Console closed. Dispatch data remains safe.")

        
            

if __name__ == "__main__":
    main()
