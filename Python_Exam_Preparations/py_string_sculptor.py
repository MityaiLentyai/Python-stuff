def string_sculptor(text: str) -> str:
    ret = ""
    flag = -1

    for letter in text:
        if flag == -1 and letter.isalpha():
            ret += letter.lower()
            flag = 1
            continue
        if flag == 1 and letter.isalpha():
            ret += letter.upper()
            flag = -1
            continue
        if letter == " ":
            ret += letter
            flag = -1
            continue
        if not letter.isalpha():
            ret += letter
            continue
    return ret


print(string_sculptor("Hell World!@and ME!"))
