def pattern_tracker(text: str) -> int:
    counter = 0
    i = 0
    for _ in text:
        try:
            if text[i].isdigit() and text[i+1].isdigit():
                if int(text[i+1]) - int(text[i])  == 1:
                    counter += 1
        except IndexError:
            break
        i +=1
    return counter


print(pattern_tracker("112233"))
