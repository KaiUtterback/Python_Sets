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

# Problem 3

''' Playlist Duplication Check
Create a Python script that takes multiple playlist sets and checks if any playlist is a duplicate of another (i.e., contains the same set of songs).

Example Code:

playlist1 = {"Song A", "Song B", "Song C"}
playlist2 = {"Song D", "Song E", "Song F"}
playlist3 = {"Song A", "Song B", "Song C"}

playlists = [playlist1, playlist2, playlist3]

Expected Outcome:
A confirmation of whether there are duplicate playlists, such as Duplicate playlists found: True.

'''
print()

def find_common_songs(playlist1, playlist2, playlist3):
    try:
        common_songs = playlist1.intersection(playlist2, playlist3)
        if common_songs: 
            print("Common Songs Across All Playlists:", common_songs)
        else:
            print("No common songs across all playlists.")
    except Exception as e:
        print(f"An error occurred while finding common songs: {e}")

def find_unique_songs(playlist1, playlist2, playlist3):
    try:
        unique_to_playlist1 = playlist1 - (playlist2.union(playlist3))
        unique_to_playlist2 = playlist2 - (playlist1.union(playlist3))
        unique_to_playlist3 = playlist3 - (playlist1.union(playlist2))

        if unique_to_playlist1:
            print("Unique Songs in Playlist 1:", unique_to_playlist1)
        else:
            print("No unique songs in Playlist 1.")

        if unique_to_playlist2:
            print("Unique Songs in Playlist 2:", unique_to_playlist2)
        else:
            print("No unique songs in Playlist 2.")

        if unique_to_playlist3:
            print("Unique Songs in Playlist 3:", unique_to_playlist3)
        else:
            print("No unique songs in Playlist 3.")
    except Exception as e:
        print(f"An error occurred while finding unique songs: {e}")

def check_for_duplicate_playlists(playlist1, playlist2, playlist3):
    playlists = {'Playlist 1': playlist1, 'Playlist 2': playlist2, 'Playlist 3': playlist3}
    duplicates = []

    playlist_names = list(playlists.keys())
    for i in range(len(playlist_names)):
        for j in range(i + 1, len(playlist_names)):
            if playlists[playlist_names[i]] == playlists[playlist_names[j]]:
                duplicates.append((playlist_names[i], playlist_names[j]))

    if duplicates:
        for dup in duplicates:
            print(f"{dup[0]} and {dup[1]} are duplicates.")
    else:
        print("No duplicate playlists found.")

playlist1 = {"Song A", "Song B", "Song C"}
playlist2 = {"Song D", "Song E", "Song F"}
playlist3 = {"Song A", "Song B", "Song C"}  


find_common_songs(playlist1, playlist2, playlist3)
find_unique_songs(playlist1, playlist2, playlist3)
check_for_duplicate_playlists(playlist1, playlist2, playlist3)