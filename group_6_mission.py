def participant_cost(attendees, food_per_person, transport_per_person):
    cost_per_person = attendees * (food_per_person + transport_per_person)

    return cost_per_person


def event_total(attendees, food_per_person, transport_per_person, venue_cost):
    total_cost = participant_cost(attendees, food_per_person, transport_per_person) + venue_cost

    return total_cost


def budget_status(budget, total):
    if total <= budget:
        return "Within budget."
    else:
        return "Over budget."


def event_summary(event_name, total, status):
    summary = f"{event_name}: total {total} naira. {status}"

    return summary
