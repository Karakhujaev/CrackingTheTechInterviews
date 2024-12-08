def deletionDistance(str1, str2):
    # Get lengths of both strings
    len1, len2 = len(str1), len(str2)

    # Create a DP table with dimensions (len1+1) x (len2+1)
    dp = [[0] * (len2 + 1) for _ in range(len1 + 1)]
    print(dp)
    # Fill the DP table
    for i in range(1, len1 + 1):
        for j in range(1, len2 + 1):
            if str1[i - 1] == str2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
                print(dp)
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    # Length of the longest common subsequence
    lcs_length = dp[len1][len2]

    # Calculate deletion distance
    return (len1 - lcs_length) + (len2 - lcs_length)

assert deletionDistance("some", "same") == 2

def deletion_distance(str1: str, str2: str) -> int:

    globalmin = float('inf')

    def recur(str1,str2,edits):
        nonlocal globalmin

        if not str1 and not str2:
            globalmin = min(globalmin,edits)
            return edits

        if not str1:
            edits += len(str2)
            globalmin = min(globalmin,edits)
            return edits

        if not str2:
            edits += len(str1)
            globalmin = min(globalmin,edits)
            return edits

        if str1[0] == str2[0]:
            recur(str1[1:],str2[1:],edits)
        else:
            edits += 1
            recur(str1[1:],str2,edits)
            recur(str1,str2[1:],edits)

    recur(str1,str2,0)
    
    return globalmin

assert deletion_distance("","") == 0
assert deletion_distance("heat","hit") == 3
assert deletion_distance("some","some") == 0
assert deletion_distance("dog","frog") == 3
assert deletion_distance("some","thing") == 9