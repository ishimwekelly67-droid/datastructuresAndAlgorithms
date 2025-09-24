# ------------------------------
# Project 39: Hotel Booking Summary
# ------------------------------

import array

# ========== Integers ==========
# Example integer values: number of bookings per day
bookings = [25, 30, 18, 40, 35]

total_bookings = sum(bookings)
average_bookings = total_bookings / len(bookings)
min_bookings = min(bookings)
max_bookings = max(bookings)

print("=== Integers Section ===")
print(f"Total bookings: {total_bookings}")
print(f"Average bookings: {average_bookings:.2f}")
print(f"Min bookings: {min_bookings}")
print(f"Max bookings: {max_bookings}\n")

# ========== Strings ==========
print("=== Strings Section ===")
report = (
    f"Hotel Booking Summary Report\n"
    f"Total bookings recorded: {total_bookings}\n"
    f"Average bookings per day: {average_bookings:.2f}\n"
)
print(report)

# ========== Booleans ==========
print("=== Booleans Section ===")
threshold = 28
# Compound condition: check if average is above threshold and max is also high
if average_bookings > threshold and max_bookings > 30:
    print("Status: Above Standard\n")
else:
    print("Status: Below Standard\n")

# ========== Lists ==========
print("=== Lists Section ===")
booking_days = ["Mon", "Tue", "Wed", "Thu", "Fri"]

print("Before modifications:", booking_days)

# Add new element
booking_days.append("Sat")

# Remove element based on condition (remove "Wed")
if "Wed" in booking_days:
    booking_days.remove("Wed")

# Sort list
booking_days.sort()

print("After modifications:", booking_days, "\n")

# ========== Arrays ==========
print("=== Arrays Section ===")
# Use array module (subset of bookings data)
booking_array = array.array("i", [25, 30, 18])

array_sum = sum(booking_array)
list_sum = sum(bookings)

print(f"Array sum: {array_sum}")
print(f"List sum: {list_sum}")

if array_sum < list_sum:
    print("Array sum is smaller than List sum\n")

# ========== Dictionaries ==========
print("=== Dictionaries Section ===")
hotel_records = [
    {"id": 1, "name": "Deluxe Room", "value": 120},
    {"id": 2, "name": "Suite Room", "value": 200},
    {"id": 3, "name": "Standard Room", "value": 80},
]

# Update one record (change Suite Room value)
hotel_records[1]["value"] = 220

# Delete one record (remove Standard Room)
hotel_records = [record for record in hotel_records if record["id"] != 3]

# Compute total value
total_value = sum(record["value"] for record in hotel_records)

print("Final Records:", hotel_records)
print("Total value across records:", total_value)
