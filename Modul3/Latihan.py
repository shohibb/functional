data = [
    "3 minggu 3 hari 7 jam 21 menit",
    "5 minggu 5 hari 8 jam 11 menit",
    "7 minggu 1 hari 5 jam 33 menit",
]


def currying_weeks_to_minutes(weeks):
    def currying_days_to_minutes(days):
        def currying_hours_to_minutes(hours):
            def currying_minutes(minutes):
                return weeks * 7 * 24 * 60 + days * 24 * 60 + hours * 60 + minutes

            return currying_minutes

        return currying_hours_to_minutes

    return currying_days_to_minutes


output_data = []

for entry in data:
    parts = entry.split()
    weeks = int(parts[0])
    days = int(parts[2])
    hours = int(parts[4])
    minutes = int(parts[6])

    total_minutes = currying_weeks_to_minutes(weeks)(days)(hours)(minutes)
    output_data.append(total_minutes)
print("Hasil latihan 1 ")
print(output_data)

integer_values = [list(filter(str.isdigit, entry)) for entry in data]

print("\nHasil latihan 2 ")
for entry in integer_values:
    print(entry)
