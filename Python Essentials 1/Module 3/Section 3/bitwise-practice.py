
# TURNING THE SWITCHES ON #

switches = 0b0000 # all off
switches = switches | 0b0001  #turns on switch 1 (output = 1 in decimal)
switches = switches | 0b0010  # turns on switch 2 without effecting the 1st one (output 3 in decimal)
switches = switches | 0b0100  # turns on switch 3 without effecting the 1st & 2nd one (output 7 in decimal)
print(switches)

# TURNING THE SWITCHES OFF #

# currently 1, 2, and 3 are on

switches = switches & ~4  # turning off switch 3 which has a decimal value 4
switches = switches & ~2  # turning off switch 2 which has a decimal value 2
switches = switches & ~1  # turning off switch 1 which has a decimal value 1

# 0 1 1 1 original state
# 1 0 1 1 switch to be turned off which is 3rd in this case
# 0 0 1 1 the conjunction of the two states turns the 3rd switch off

# USING XOR TO TOGGLE SWITCH BACK & FORTH #

# currently all the swithes are off, so:
switches = switches | 0b0100  # turns the 3rd switch on
switch_3 = 4  # the decimal value
print(f"Initial switch state: {switches} (Switch 3 in ON)")
# first toggle
switches = switches ^ switch_3
print(f"After 1st toggle: {switches} (Switch 3 in now OFF)")
# second toggle
switches = switches ^ switch_3
print(f"After 2nd toggle: {switches} (Switch 3 in now ON)")

print("Are the switches on?")
print("Nr. 4", (switches & 0b1000) != 0)
print("Nr. 3", (switches & 0b0100) != 0)
print("Nr. 2", (switches & 0b0010) != 0)
print("Nr. 1", (switches & 0b0001) != 0)

