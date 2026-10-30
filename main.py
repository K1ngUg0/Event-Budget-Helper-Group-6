# 1. Calculate people cost
def participant_cost(attendees, food_per_person, transport_per_person):
    return attendees * (food_per_person + transport_per_person)

# 2. Add venue to get total cost
def event_total(attendees, food_per_person, transport_per_person, venue_cost):
    people_cost = participant_cost(attendees, food_per_person, transport_per_person)
    return people_cost + venue_cost
    
# 3. Check if we have enough money
def budget_status(budget, total):
    if total <= budget:
        return "Within budget"
    else:
        return "Over budget"

# 4. Build the final sentence
def event_summary(event_name, total, status):
    return f"{event_name}: total {total} naira. {status}."


# Step 1: Set up our numbers from the brief & Pass data step by step
people = participant_cost(10, 800, 200)
total = event_total(10, 800, 200, 5000)
status = budget_status(16000, total)
summary = event_summary("Study Day", total, status)

# Step 2: Print out each step to confirm
print("People cost :", people)   # Expected: 10000
print("Total cost  :", total)    # Expected: 15000
print("Status      :", status)   # Expected: Within budget
print("Summary     :", summary)  # Expected: Study Day: total 15000 naira. Within budget.

# Component C: Budget Status 
def budget_status(budget, total):
    if total <= budget:
        return "Within budget"
    else:
        return "Over budget"


status = budget_status(1000, 15000)
status1 = budget_status(16000, 15000)

print(status)  # Expected: Over budget
print(status1)  # Expected: Within budget