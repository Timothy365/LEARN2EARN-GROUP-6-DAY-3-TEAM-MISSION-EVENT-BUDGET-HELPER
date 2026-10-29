
#this fuction calculate the total cost for the event.
def event_total(attendees, food_per_person, transport_per_person, venue_cost):
    total_cost = participant_cost(attendees, food_per_person, transport_per_person) + venue_cost
    return total_cost
