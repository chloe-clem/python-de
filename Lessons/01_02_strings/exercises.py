# Lesson 1.2: Strings and operators
# Run with: uv run lessons/01_02_strings/exercises.py

# --- Exercise 1: clean a station name ---
raw_station = "  amsterdam CENTRAAL  "
clean_station = None  # → "Amsterdam Centraal"
assert clean_station == "Amsterdam Centraal", clean_station
print("✅ 1 clean station name")

# --- Exercise 2: make a 3-letter code from a city (slicing + method) ---
city = "utrecht"
code = None  # → "UTR"
assert code == "UTR", code
print("✅ 2 station code")

# --- Exercise 3: parse a Dutch-formatted price into a float ---
price_text = "€1.234,50"
price = None  # → 1234.5  (hint: remove €, remove the thousands dot, swap , for .)
assert price == 1234.5, price
print("✅ 3 Dutch price")

# --- Exercise 4: trip duration in hours and minutes ---
duration_min = 147
hours = None    # → 2   (hint: //)
minutes = None  # → 27  (hint: %)
label = None    # → "2h27" (f-string)
assert (hours, minutes, label) == (2, 27, "2h27"), (hours, minutes, label)
print("✅ 4 duration")

# --- Exercise 5: weather summary with an f-string ---
dest = "Maastricht"
temp_c = 16.456
rain_mm = 0.2
summary = None  # → "Maastricht: 16.5°C, 0.2 mm rain"
assert summary == "Maastricht: 16.5°C, 0.2 mm rain", summary
print("✅ 5 weather summary")

# --- Exercise 6: is this a good weekend trip? (comparison + and) ---
# Good trip = at most 150 minutes AND at least 15°C AND less than 1 mm rain
is_good_trip = None
assert is_good_trip is True, is_good_trip
print("✅ 6 good trip check")

# --- Exercise 7: split a CSV line into fields ---
line = "ASD,Amsterdam Centraal,52.3789,4.9004"
station_code = None  # → "ASD"
station_name = None  # → "Amsterdam Centraal"
lat = None           # → 52.3789 as a float, not a string!
assert (station_code, station_name, lat) == ("ASD", "Amsterdam Centraal", 52.3789)
print("✅ 7 CSV line")

# --- Exercise 8 (bonus): build a station label ---
# If the name contains "Centraal", label it "<name> ⭐ main station",
# otherwise just the name. Use only what you know: `in` + an f-string.
# (Proper if/else comes in Lesson 1.5. Try it anyway if you know it!)
name = "Utrecht Centraal"
station_label = None  # → "Utrecht Centraal ⭐ main station"
assert station_label == "Utrecht Centraal ⭐ main station", station_label
print("✅ 8 bonus")

print("\n🎉 All exercises passed!")