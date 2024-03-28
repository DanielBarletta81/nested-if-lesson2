# Task 2: Venue Selection

attendees = int(input("Enter number of attendees: "))
venue = "large hall" if attendees > 100 else "conference room"
print(venue)

if attendees > 125:
    if attendees > 175:
        print("The venue will require a projector and an audio system.")
    else:
        print("Depending on your audience, an audio system may be needed.")
elif venue == "large hall" and attendees < 125:
    print("You will need a projector, but an audio system is not required.")

elif venue == "conference room" and attendees > 50:
    print("Better speak up!")

else:
    print("You should be seen and heard easily in this " + venue)


