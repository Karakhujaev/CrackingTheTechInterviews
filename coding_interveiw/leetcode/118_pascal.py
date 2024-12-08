class Solution(object):
    def generate(self, numRows):
        if numRows > 1:
            res = [[1], [1, 1]]
        else:
            return [[1]]
        
        for i in range(2, numRows):
            add = [1]
            for j in range(len(res[-1]) -1):
                add.append(res[-1][j] + res[-1][j+1])
            add.append(1)
            res.append(add)
        return res
            