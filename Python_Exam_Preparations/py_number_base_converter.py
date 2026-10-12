def number_base_converter(number: str, from_base: int, to_base: int) -> str:
    if  (from_base < 2 or from_base > 36) or (to_base < 2 or to_base > 36):
        return "ERROR"
    base = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    power = 0
    decimal = 0
    ret = ""
    for char in reversed(number):

        digit = base.index(char)
        if digit > from_base:
            return "ERROR"
        current = digit * from_base ** power
        power +=1
        decimal += current

    while decimal:
        modulo = decimal%to_base
        ret += base[modulo]
        decimal //= to_base

    return ret[::-1]
print(number_base_converter("123", 1, 10))
