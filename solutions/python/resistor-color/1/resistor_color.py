# The colors are ordered from 0 to 9
COLORS = [
    "black", "brown", "red", "orange", "yellow",
    "green", "blue", "violet", "grey", "white"
]

def color_code(color):
    """Return the numerical value associated with a specific color."""
    return COLORS.index(color)

def colors():
    """Return the list of all resistor colors in order."""
    return COLORS
