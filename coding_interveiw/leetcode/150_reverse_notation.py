def evaluate_operators(got, result, operator):
    got = int(got)
    result = int(result)
    if operator == "+":
        return got + result

    elif operator == "-":
        return got - result

    elif operator == "*":
        return got * result

    elif operator == "/":
        return int(got / result) if got / result != -1 else 0

class Solution(object):
    def evalRPN(self, tokens):
        operators = {"*", "/", "+", "-"}
        stack = []
        curr = 0
        while curr < len(tokens):
            if tokens[curr] in operators:
                result = stack.pop()
                got = stack.pop()
                stack.append(evaluate_operators(got, result, tokens[curr]))
                
            else:
                stack.append(int(tokens[curr]))

            curr += 1
        return stack[0]
