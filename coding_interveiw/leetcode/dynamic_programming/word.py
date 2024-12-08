def find(chars, word):
    def dfs(x, y, newCurr, word):
        for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            newX, newY = x + dx, dy + y
            if 0 < newX < len(chars) and 0 < newY < len(chars[0]) and 0 < newCurr < len(word) and chars[newX][newY] == word[newCurr]:
                if newCurr == len(word) - 1:
                    return True
                
                dfs(newX, newY, newCurr + 1)
            

    for x in range(len(chars)):
        for y in range(len(chars[0])):
            if chars[x][y] == word[0]:
                got = dfs(x, y, 1, word)
                if got == True:
                    return True

    return False




print(find([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "ABCCED"))