s = "Den Haag Centraal"
print(repr(s[4:8]))                  # Q1: guess?  Haag (repr shows the quotes, so spaces are visible)

name = "  Utrecht  "
name.strip()
print(repr(name))                    # Q2: guess? "  Utrecht  "
name = name.strip()
print(repr(name))                    # ...and now? Utrecht

print(17 % 5, 17 // 5, 17 / 5)       # Q3: guess all three 2/5, 3, 3 2/5 --> 2 3 3.4

minutes = 5
print(f"2h{minutes}", f"2h{minutes:02d}")   # Q4 2h5 2h05

print("Centraal" in "utrecht centraal")             # Q7 false
print("centraal" in "utrecht centraal".lower())     # the safe version True 

print(int(float("12.5")))            # Q6: this works... 12
print(int("12.5"))                   # ...this one crashes. Read the error message! invalid literal for int() with base 10: '12.5'