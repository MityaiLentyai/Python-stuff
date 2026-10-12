def anagram(s1: str, s2: str) -> bool:
    s2= s2.lower().replace(" ", "")
    s1=s1.lower().replace(" ","")
    array = list(s1)
    if len(s1) != len(s2):
        return False

    for letter in s2:
        if letter in array:
            array.remove(letter)
    if len(array) == 0:
        return True
    else:
        return False

print(anagram("abc", "abcc"))
