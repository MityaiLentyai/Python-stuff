def inter(s1: str, s2: str) -> str:
    temp = list()

    for letter in s1:
        if letter in s2 and letter not in temp:
            temp.append(letter)
    ret = ''.join(temp)

    return ret

s1 = ""
s2 = "abc"

print(inter(s1,s2))