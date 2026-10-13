def whisper_cipher(text: str, shift: int) -> str:
    ret_str = ""
    for char in text:
        if char.islower():
            new_char = (chr(((ord(char) - 97)%26+shift)% 26 +97))
            ret_str +=new_char
        if char.isupper():
            new_char = chr(((ord(char) - 65)%26+shift)% 26 +65)
            ret_str +=new_char
        if not char.isalpha():
            ret_str += char
    return ret_str

print(whisper_cipher("abc", -3))
