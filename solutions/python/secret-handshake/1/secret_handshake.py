def commands(binary_str):
    actions = [
        "wink",
        "double blink",
        "close your eyes",
        "jump"
    ]

    result = []

    if binary_str[-1] == "1":
        result.append(actions[0])

    if binary_str[-2] == "1":
        result.append(actions[1])

    if binary_str[-3] == "1":
        result.append(actions[2])

    if binary_str[-4] == "1":
        result.append(actions[3])

    if len(binary_str) >= 5 and binary_str[-5] == "1":
        result.reverse()

    return result