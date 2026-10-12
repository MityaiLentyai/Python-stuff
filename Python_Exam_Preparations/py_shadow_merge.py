def shadow_merge(list1: list[int], list2: list[int]) -> list[int]:
    return sorted(list1 + list2)

print(shadow_merge([1,1,2], [1,3,3]))