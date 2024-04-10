# Problem 1

''' Sets Adventure
Objective:
 The aim of this assignment is to deepen your understanding and applicaiton of Python sets in various scenarios, 
 ranging from basic operations to advanced manipulations and best practices.
 You will correct given codes, use sets in everyday contexts, and tackle challenges that require creative thinking and problem-solving.

Task 1:
 Imagine you work for an airline and need to compare the flight routes of your airline with a competitor.
 You have two sets of flight destinations, one for each airline. 
 Write a Python program to find out:

 1) Destinations that both airlines fly to.
 2) Destinations unique to your airline.
 3) Whether there are any destinations that neither airline shares.

Example Code:

our_routes = {"LAX", "JFK", "CDG", "DXB"}
competitor_routes = {"JFK", "CDG", "LHR", "BKK"}

'''

our_routes = {"LAX", "JFK", "CDG", "DXB"}
competitor_routes = {"JFK", "CDG", "LHR", "BKK"}

def find_same_flights():
    same_flights = our_routes.intersection(competitor_routes)
    print(f"Both airlines share these flights:")
    for flight in same_flights:
        print(f" - {flight}")

def find_unique_flights():
    unique_flights = our_routes.difference(competitor_routes)
    print(f"Our unique flights are:")
    for flight in unique_flights:
        print(f" - {flight}")

def find_neither():
    unique_to_our_airline = our_routes.difference(competitor_routes)
    print("Destinations unique to our airline:")
    for flight in sorted(unique_to_our_airline): 
        print(f" - {flight}")
    
    unique_to_competitor = competitor_routes.difference(our_routes)
    print("\nDestinations unique to competitor's airline:")
    for flight in sorted(unique_to_competitor):
        print(f" - {flight}")


def display_all_flights():
    print("Flights from Our Company:")
    for flight in sorted(our_routes):  
        print(f" - {flight}")
    
    print("\nFlights from Competitor's Company:")
    for flight in sorted(competitor_routes):
        print(f" - {flight}")    

def run_airline():
    print("\nHello and welcome to the airline comparison program!")
    while True:
        print("\n------------------------------")
        print("Please choose an option:")
        print("1. Find Flights Shared by both Airlines")
        print("2. Look at Flights Unique to Our Airline")
        print("3. Find Flights Unshared by Both")
        print("4. Display All Flights from Both Companies")
        print("5. Exit")
        print("------------------------------")
        
        selection = input("Enter Selection: ")

        if selection == '1':
            print("\nFinding Flights Shared by Both Airlines...")
            find_same_flights()
        elif selection == '2':
            print("\nLooking at Flights Unique to Our Airline...")
            find_unique_flights()
        elif selection == '3':
            print("\nFinding Flights Unshared by Both Airlines...")
            find_neither()
        elif selection == '4':
            print("\nDisplaying All Flights from Both Companies...")
            display_all_flights()
        elif selection == '5':
            print("\nThank you for using the airline comparison program!")
            break
        else:
            print("Improper Selection. Try again.")
        print("\n------------------------------")

run_airline()

# Problem 2
''' Set Operations in Data Analysis
Objective:
 The aim of this assignment is to enhance your skills in using Python sets for data analysis tasks. 
 You will apply various set operations to handle real-world data scenarios, focusing on their practical application and efficiency.

Task 1: Duplicate Entries Cleanup
 You are given a list of customer IDs, some of which are duplicated. Write a Python script to remove duplicates and display the unique customer IDs.

Example Code:

customer_ids = ["C001", "C002", "C003", "C002", "C001", "C004"]

Expected Outcome:
A set of unique customer IDs, ensuring no duplicates. For instance, {'C001', 'C002', 'C003', 'C004'}.

'''

customer_ids = ["C001", "C002", "C003", "C002", "C001", "C004"]

sorted_unique_customer_ids = sorted(set(customer_ids))
print("Unique Customer IDs:", sorted_unique_customer_ids)
