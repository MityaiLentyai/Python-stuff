def pattern_tracker(text: str) -> int:
    counter = 0
    for char in text[:-1]:
        if char.isdigit() and char[+1].isdigit():
            if int(char) - int(char[+1]) == 1:
                counter += 1
        else:
            continue

    return counter


print(pattern_tracker("1234b41b24"))
