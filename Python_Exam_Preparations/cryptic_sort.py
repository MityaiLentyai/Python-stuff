def count_vowels(text: str) -> int:
    return sum(char in "aeiou" for char in text.lower())


def sort_key(text: str) -> tuple:
    return len(text), text.lower(), count_vowels(text)

def cryptic_sorter(strings: list[str]) -> list[str]:
    n = len(strings)

    for i in range(n):
        for j in range(n - i - 1):
            if sort_key(strings[j]) > sort_key(strings[j + 1]):
                strings[j], strings[j + 1] = strings[j + 1], strings[j]

    return strings



# def count_vowels(text: str) -> int:
#     return sum(char in "aeiou" for char in text.lower())
#
#
#
# def cryptic_sorter(strings: list[str]) -> list[str]:
#     if len(strings) == 1 or len(strings) == 0:
#         return strings
#
#     i = 0
#     while i < len(strings):
#         j = 0
#         while j < len(strings) - 1:
#             if len(strings[j]) > len(strings[j + 1]):
#                 strings[j], strings[j + 1] = strings[j + 1], strings[j]
#             j += 1
#         i += 1
#
#     i = 0
#     while i < len(strings) - 1:
#         if (len(strings[i]) == len(strings[i + 1])) and (
#                 strings[i].lower() > strings[i + 1].lower()):
#             strings[i], strings[i + 1] = strings[i + 1], strings[i]
#         i += 1
#
#
#     return strings
#
print(cryptic_sorter(["hello","world","hi","test","1111", "aaaa"]))
