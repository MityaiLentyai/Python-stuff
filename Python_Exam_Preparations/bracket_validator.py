def bracket_validator(s: str) -> bool:
    brackets = [0]
    for c in s:
        if c in '{[(':
            brackets.append(c)
            continue
        match c:
            case ']':
                if brackets[-1] == '[':
                    brackets.pop()
                    continue
                else:
                    return False
            case '}':
                if brackets[-1] == '{':
                    brackets.pop()
                    continue
                else:
                    return False
            case ')':
                if brackets[-1] == '(':
                    brackets.pop()
                    continue
                else:
                    return False
    if len(brackets) == 1:
        return True
    else: return False
print(bracket_validator('1{124[11421]n42()}1'))