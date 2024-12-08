from typing import List

class Solution:
    def hIndex(self, citations: List[int]) -> int:
        # Sort citations in descending order
        citations.sort(reverse=True)
        
        # Traverse the sorted list and find the h-index
        for i, citation in enumerate(citations):
            if i + 1 > citation:
                return i
        
        # If all citations are greater than their positions, h-index is the length of the list
        return len(citations)
