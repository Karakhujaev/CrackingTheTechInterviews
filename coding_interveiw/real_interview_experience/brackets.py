def is_properly(text):
    table = {
        "}": "{",
        ")": "(",
        "]": "[",
    }
    stack = []
    for brckt in text:
        if brckt not in table:
            stack.append(brckt)

        elif brckt in table:
            if not stack or stack.pop() != table[brckt]:
                return False
    return len(stack) == 0