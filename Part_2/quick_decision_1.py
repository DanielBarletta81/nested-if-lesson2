# Task 1 Code Correction


# Buggy

""" attendees = input("Enter number of attendees: ") # attendees should be an integer
venue = "large hall" if attendees > 100 else "conference room"
print(venue) """

# Corrected

attendees = int(input("Enter number of attendees: "))
venue = "large hall" if attendees > 100 else "conference room"
print(venue)