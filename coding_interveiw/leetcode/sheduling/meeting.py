def find_next_available_slot(participants):
    # Merge all schedules into one list
    merged_schedule = []
    for participant_schedule in participants.values():
        merged_schedule.extend(participant_schedule)
    # Sort the merged schedule by start time
    merged_schedule.sort(key=lambda x: x[0])
    print(merged_schedule)

    # Iterate through the sorted schedule to find the next available 30-minute slot
    current_time = merged_schedule[0][0]
    for slot in merged_schedule:
        start_time, end_time = slot
        if start_time > current_time:
            if start_time - current_time >= 30:
                return current_time, current_time + 30
        current_time = max(current_time, end_time)

    # If no available slot is found, return None
    return None

# Test cases
participants1 = {
    "P1": [(1000, 1030), (1030, 1100), (1130, 1230)],
    "P2": [(930, 1015), (1030, 1045), (1130, 1300)],
    "P3": [(930, 1015), (1015, 1110), (1130, 1300)],
}
print("Next available slot for participants 1:", find_next_available_slot(participants1))

# participants2 = {
#     "P1": [(700, 1000), (1230, 1300), (1440, 1600)],
#     "P2": [(930, 1015), (1050, 1320), (1400, 1700)],
#     "P3": [(830, 1010), (1100, 1445)],
# }
# print("Next available slot for participants 2:", find_next_available_slot(participants2))