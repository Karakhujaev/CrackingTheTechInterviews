class Solution(object):
    def longestCommonPrefix(self, strs):
        shortest, pose = len(strs[0]), 0
        for idx_short, word in enumerate(strs):
            if len(word) < shortest:
                shortest = len(word)
                pose = idx_short

        search = strs[pose]
        is_prefix = True
        for i in range(len(search), 0, -1):
            search = search[0:i]
            for comp in strs:
                if search != comp[0:i]:
                    is_prefix = False
                    break

            if is_prefix == True:
                return search
        
            is_prefix = True
            
        return ""
    

solution = Solution()
print(solution.longestCommonPrefix(["flower","flow","flight"]))
