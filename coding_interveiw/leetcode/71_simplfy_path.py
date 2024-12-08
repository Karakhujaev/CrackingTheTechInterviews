class Solution:
    def simplifyPath(self, path: str) -> str:
        paths = path.split("/")
        stack = []

        for path in paths:
            if path == "." or path == "":
                continue
            elif path == "..":
                if stack:
                    stack.pop()
            else:
                stack.append(path)
        return "/" + "/".join(stack)
        