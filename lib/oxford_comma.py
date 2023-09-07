def oxford_comma(elements):
    if len(elements) == 0:
        return ""
    elif len(elements) == 1:
        return elements[0]
    elif len(elements) == 2:
        return f"{elements[0]} and {elements[1]}"
    else:
        # Join all elements except the last one with commas, then add "and" before the last element
        return ", ".join(elements[:-1]) + f", and {elements[-1]}"

# test
result = oxford_comma(["fiddleheads", "okra", "kohlrabi"])
print(result)  # Output: "fiddleheads, okra, and kohlrabi"

