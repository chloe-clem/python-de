# Lesson 1.4: Dictionaries and sets
# Run with: uv run lessons/01_04_dicts_sets/exercises.py

# --- Exercise 1: look up by key ---
stations = {
    "ASD": "Amsterdam Centraal",
    "UT": "Utrecht Centraal",
    "RTD": "Roterdam Centraal",   # (typo on purpose, you'll fix it in exercise 2)
}
utrecht = stations['UT']     # → "Utrecht Centraal"
count = len(stations)      # → 3
assert (utrecht, count) == ("Utrecht Centraal", 3), (utrecht, count)
print("✅ 1 lookup")

# --- Exercise 2: add and update ---
# Write 2 lines: fix the Rotterdam typo, then add "EHV": "Eindhoven Centraal"
stations['RTD'] = 'Rotterdam Centraal'
stations['EHV'] = 'Eindhoven Centraal'
assert stations == {
    "ASD": "Amsterdam Centraal",
    "UT": "Utrecht Centraal",
    "RTD": "Rotterdam Centraal",
    "EHV": "Eindhoven Centraal",
}, stations
print("✅ 2 add and update")

# --- Exercise 3: safe lookups ---
maastricht = stations.get('MT', 'Unknown station')      # → "Unknown station"   ("MT" is NOT in the dict, so don't crash!)
has_ut = 'UT' in stations          # → True    is "UT" a key?
has_name = 'Utrecht Centraal' in stations        # → False   is "Utrecht Centraal" a key?
assert maastricht == "Unknown station", maastricht
assert (has_ut, has_name) == (True, False), (has_ut, has_name)
print("✅ 3 safe lookups")

# --- Exercise 4: keys, values and helpers ---
durations = {"Haarlem": 15, "Leiden": 35, "Utrecht": 27, "Maastricht": 147}
leiden_time = durations['Leiden']      # → 35
total_time = sum(durations.values())       # → 224   (sum of all values)
names_a_to_z = sorted(durations.keys())     # → ["Haarlem", "Leiden", "Maastricht", "Utrecht"]
assert leiden_time == 35, leiden_time
assert total_time == 224, total_time
assert names_a_to_z == ["Haarlem", "Leiden", "Maastricht", "Utrecht"], names_a_to_z
print("✅ 4 keys and values")

# --- Exercise 5: nested weather data ---
weather = {
    "Maastricht": {"temp_c": 16.5, "rain_mm": 0.2},
    "Groningen": {"temp_c": 9.0, "rain_mm": 4.1},
}
maastricht_temp = weather['Maastricht']['temp_c']    # → 16.5
groningen_rain = weather['Groningen']['rain_mm']     # → 4.1
assert (maastricht_temp, groningen_rain) == (16.5, 4.1), (maastricht_temp, groningen_rain)
print("✅ 5 nested weather")

# --- Exercise 6: NS-API-style trip (dict → list → dict) ---
trip = {
    "origin": {"code": "ASD", "name": "Amsterdam Centraal"},
    "destination": {"code": "MT", "name": "Maastricht"},
    "duration_min": 147,
    "transfers": 1,
    "legs": [
        {"train": "IC 3018", "from": "ASD", "to": "UT", "platform": "5b"},
        {"train": "IC 818", "from": "UT", "to": "MT", "platform": "18"},
    ],
}
dest_name = trip['destination']['name']        # → "Maastricht"
first_train = trip['legs'][0]['train']     # → "IC 3018"
second_platform = trip['legs'][1]['platform'] # → "18"
leg_count = len(trip['legs'])       # → 2
assert (dest_name, first_train, second_platform, leg_count) == ("Maastricht", "IC 3018", "18", 2), \
    (dest_name, first_train, second_platform, leg_count)
print("✅ 6 nested trip")

# --- Exercise 7: remove duplicates (SELECT DISTINCT) ---
visited = ["Haarlem", "Leiden", "Haarlem", "Utrecht", "Leiden", "Delft"]
unique_visited =  set(visited)  # → {"Haarlem", "Leiden", "Utrecht", "Delft"}
unique_count = len(set(visited))     # → 4
assert unique_visited == {"Haarlem", "Leiden", "Utrecht", "Delft"}, unique_visited
assert unique_count == 4, unique_count
print("✅ 7 distinct")

# --- Exercise 8: set maths (EXCEPT / INTERSECT) ---
want_to_visit = {"Maastricht", "Groningen", "Leiden", "Delft"}
not_yet = want_to_visit - set(visited)         # → {"Maastricht", "Groningen"}   want, but not visited yet
done_already = want_to_visit & set(visited)     # → {"Leiden", "Delft"}           on both
assert not_yet == {"Maastricht", "Groningen"}, not_yet
assert done_already == {"Leiden", "Delft"}, done_already
print("✅ 8 set maths")

# --- Exercise 9: fix the crash ---
# This line crashes with a KeyError. Fix it so zwolle_time is 0 when Zwolle is missing.
zwolle_time = durations.get("Zwolle", 0)
assert zwolle_time == 0, zwolle_time
print("✅ 9 KeyError fixed")

# --- Bonus: tuple keys ---
journey_times = {("ASD", "UT"): 27, ("ASD", "MT"): 147, ("UT", "MT"): 118}
utrecht_to_maastricht = journey_times['UT', 'MT']   # → 118
assert utrecht_to_maastricht == 118, utrecht_to_maastricht
print("✅ bonus")
# Experiment: uncomment, run, read the error, comment again
bad = {["ASD", "UT"]: 27}

print("\n🎉 All exercises passed!")