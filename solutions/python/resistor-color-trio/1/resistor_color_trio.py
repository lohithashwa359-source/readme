# Resistor Color Trio - Python Solution

COLOR_VALUES = {
    "black": 0,
    "brown": 1,
    "red": 2,
    "orange": 3,
    "yellow": 4,
    "green": 5,
    "blue": 6,
    "violet": 7,
    "grey": 8,
    "white": 9
}

def label(colors):
    # First two colors form the significant digits
    value = COLOR_VALUES[colors[0]] * 10 + COLOR_VALUES[colors[1]]

    # Third color is the multiplier
    value *= 10 ** COLOR_VALUES[colors[2]]

    units = ["ohms", "kiloohms", "megaohms", "gigaohms"]

    unit_index = 0

    # Convert to higher units if divisible by 1000
    while value >= 1000 and value % 1000 == 0:
        value //= 1000
        unit_index += 1

    return f"{value} {units[unit_index]}"
