current_hours = 14
current_minutes = 34
current_seconds = 42

seconds_per_day = 60 * 60 * 24

seconds_passed = ((current_hours * 60 * 60) + (current_minutes * 60) + current_seconds)

remained_seconds = seconds_per_day - seconds_passed

print(remained_seconds)
