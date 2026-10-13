# twist_sequence([1,2,3], 5)

# [2,3,1]

def twist_sequence(arr: list[int], k: int) -> list[int]:
    try:
        rotation_amount = k%(len(arr))
    except ZeroDivisionError:
        return arr
    if not rotation_amount:
        return arr
    tmp_array = arr[-rotation_amount:]
    for i in range(rotation_amount):
        arr.pop()
    ret = tmp_array + arr
    return ret

print(twist_sequence([], 3))