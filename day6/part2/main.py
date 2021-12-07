fishes = list(map(lambda x: int(x), open("input.txt", "r").read().split(",")))


days = [0] * 9
# Update the current numbers
for fish in fishes:
    days[fish] += 1

for i in range(256):
    # To make it cyclic: 0, 1, 2, 3, 4, 5, 6, 7, 8
    today = i % len(days)  # Add new babies
    days[(today + 7) % len(days)] += days[today]

print(f"Total lanternfish after 256 days: {sum(days)}")
