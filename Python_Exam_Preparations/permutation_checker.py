def string_permutation_checker(s1: str, s2: str) -> bool:
    if len(s1) != len(s2):
        return False
    array = list(s1)
    for char in s2:
        if char in array:
            array.remove(char)
    if not array:
        return True
    return False
print(string_permutation_checker("a gentleman","elegant man"))