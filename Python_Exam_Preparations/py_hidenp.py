# hidenp("abc", "a1b2c3")
# True

# hidenp("ace", "abcde")
# True

# hidenp("aec", "abcde")
# False

def hidenp(small: str, big: str) -> bool:
    array = list(small)
    for letter in big:
        if not array:
            return True
        if letter == array[0]:
            array.remove(letter)
    if not array:
        return True
    return False


print(hidenp("sing","subsequence testing"))
