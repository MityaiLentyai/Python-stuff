# Write a function that checks if a string is a palindrome,
# ignoring spaces and case, only consider alphabetic characters
# for the comparison.

def echo_validator(text: str) -> bool:
    new_str = text.replace(" ","")
    if new_str == "":
        return False
    new_str = new_str.lower()
    if new_str == new_str[::-1]:
        return True
    else:
        return False

print(echo_validator("hello"))