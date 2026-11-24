# Lesson 1.2: Strings and operators
# Run with: uv run lessons/01_02_strings/exercises.py

# --- Exercise 1: clean a station name ---
raw_station = "  amsterdam CENTRAAL  "
clean_station = raw_station.strip().title()  # → "Amsterdam Centraal"
assert clean_station == "Amsterdam Centraal", clean_station
print("✅ 1 clean station name")

# --- Exercise 2: make a 3-letter code from a city (slicing + method) ---
city = "utrecht"
code = city[0:3].upper()  # → "UTR"
assert code == "UTR", code
print("✅ 2 station code")

# --- Exercise 3: parse a Dutch-formatted price into a float ---
price_text = "€1.234,50"
price = float(price_text[1:].replace(".", "").replace(",", "."))  # → 1234.5  (hint: remove €, remove the thousands dot, swap , for .)
assert price == 1234.5, price
print("✅ 3 Dutch price")

# --- Exercise 4: trip duration in hours and minutes ---
duration_min = 147
hours = duration_min//60    # → 2   (hint: //)
minutes = duration_min%60   # → 27  (hint: %)
label = f"{hours}h{minutes}"  # → "2h27" (f-string)
assert (hours, minutes, label) == (2, 27, "2h27"), (hours, minutes, label)
print("✅ 4 duration")

# --- Exercise 5: weather summary with an f-string ---
dest = "Maastricht"
temp_c = 16.456
rain_mm = 0.2
summary = f"{dest}: {temp_c:.1f}°C, {rain_mm} mm rain"  # → "Maastricht: 16.5°C, 0.2 mm rain"
assert summary == "Maastricht: 16.5°C, 0.2 mm rain", summary
print("✅ 5 weather summary")

# --- Exercise 6: is this a good weekend trip? (comparison + and) ---
# Good trip = at most 150 minutes AND at least 15°C AND less than 1 mm rain
is_good_trip = duration_min <= 150 and 15 <= temp_c and rain_mm < 1
assert is_good_trip is True, is_good_trip
print("✅ 6 good trip check")

# --- Exercise 7: split a CSV line into fields ---
line = "ASD,Amsterdam Centraal,52.3789,4.9004"
station_code = line.split(",")[0]  # → "ASD"
station_name = line.split(",")[1]  # → "Amsterdam Centraal"
lat =  float(line.split(",")[2])   # → 52.3789 as a float, not a string!
assert (station_code, station_name, lat) == ("ASD", "Amsterdam Centraal", 52.3789)
print("✅ 7 CSV line")

# --- Exercise 8 (bonus): build a station label ---
# If the name contains "Centraal", label it "<name> ⭐ main station",
# otherwise just the name. Use only what you know: `in` + an f-string.
# (Proper if/else comes in Lesson 1.5. Try it anyway if you know it!)
name = "Utrecht Centraal"
if "Centraal" in name:
    station_label = f"{name} ⭐ main station"  # → "Utrecht Centraal ⭐ main station"
else:
    station_label = name
assert station_label == "Utrecht Centraal ⭐ main station", station_label
print("✅ 8 bonus")

print("\n🎉 All exercises passed!")