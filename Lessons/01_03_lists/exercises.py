# Lesson 1.3: Lists and tuples
# Run with: uv run lessons/01_03_lists/exercises.py

# --- Exercise 1: indexing and length ---
destinations = ["Haarlem", "Leiden", "Utrecht", "Den Haag", "Groningen", "Maastricht"]
first = destinations[0]   # → "Haarlem"
last = destinations[-1]   # → "Maastricht"  (works for ANY length list)
count = len(destinations)   # → 6
assert (first, last, count) == ("Haarlem", "Maastricht", 6), (first, last, count)
print("✅ 1 indexing")

# --- Exercise 2: three shortest trips (ORDER BY ... LIMIT 3) ---
durations = [15, 35, 27, 50, 140, 147]
shortest_three = sorted(durations)[:3] # → [15, 27, 35]
assert shortest_three == [15, 27, 35], shortest_three
print("✅ 2 shortest three")

# --- Exercise 3: change a list in place ---
weekend = ["Haarlem", "Den Haag", "Leiden"]
# Write 2 lines below: add "Zandvoort" to the end, then remove "Den Haag"
weekend.insert(len(weekend)+1,'Zandvoort')
weekend.remove('Den Haag')

assert weekend == ["Haarlem", "Leiden", "Zandvoort"], weekend
print("✅ 3 append and remove")

# --- Exercise 4: fix the .sort() trap ---
# This line has a bug. Fix it so sorted_durations is sorted
# AND the original durations list stays in its original order.
sorted_durations = sorted(durations)
assert sorted_durations == [15, 27, 35, 50, 140, 147], sorted_durations
assert durations == [15, 35, 27, 50, 140, 147], durations
print("✅ 4 sort trap fixed")

# --- Exercise 5: trip statistics ---
shortest = min(durations)   # → 15
longest = max(durations)    # → 147
average = sum(durations)/len(durations)    # → 69.0  (rounded to 1 decimal: round(x, 1))
assert (shortest, longest, average) == (15, 147, 69.0), (shortest, longest, average)
print("✅ 5 stats")

# --- Exercise 6: unpack a station tuple ---
station = ("UT", "Utrecht Centraal", 52.0894, 5.1101)
# One line: unpack into code, name, lat, lon
code, name, lat, lon = station  # ← replace this whole line
assert (code, name, lat, lon) == ("UT", "Utrecht Centraal", 52.0894, 5.1101)
print("✅ 6 unpacking")
# Experiment: uncomment the next line, run, read the error, then comment it again
# station[0] = "X"

# --- Exercise 7: rank trips (list of tuples) ---
trips = [(35, "Leiden"), (147, "Maastricht"), (15, "Haarlem"), (27, "Utrecht")]
ranked = sorted(trips)          # → sorted by duration, shortest first
closest = ranked[0][1]         # → "Haarlem"     (just the name!)
furthest = ranked[-1][1]        # → "Maastricht"  (just the name!)
assert ranked == [(15, "Haarlem"), (27, "Utrecht"), (35, "Leiden"), (147, "Maastricht")], ranked
assert (closest, furthest) == ("Haarlem", "Maastricht"), (closest, furthest)
print("✅ 7 ranking")

# --- Exercise 8: strings <-> lists ---
names = ["Haarlem", "Utrecht", "Leiden"]
names_text = (', ').join(names)     # → "Haarlem, Utrecht, Leiden"
codes_line = "ASD;UT;RTD"
codes = codes_line.split(';')          # → ["ASD", "UT", "RTD"]
assert names_text == "Haarlem, Utrecht, Leiden", names_text
assert codes == ["ASD", "UT", "RTD"], codes
print("✅ 8 split and join")

# --- Exercise 9: the copy bug ---
favourites = ["Haarlem", "Leiden"]
backup = favourites.copy()            # ← this line has a bug. Fix it.
favourites.append("Delft")
assert backup == ["Haarlem", "Leiden"], backup
print("✅ 9 real copy")

# --- Bonus: two longest trips, longest first (ORDER BY ... DESC LIMIT 2) ---
longest_two = sorted(durations, reverse=True)[:2]     # → [147, 140]   one line, use durations
assert longest_two == [147, 140], longest_two
print("✅ bonus")

print("\n🎉 All exercises passed!")