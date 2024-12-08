from typing import List
from collections import deque
from collections import Collect


def shortestWordEditPath(source: str, target: str, words: List[str]) -> int:
    """
    source = "bit", target = "dot"
    words = ["but", "put", "big", "pot", "pog", "dot", "lot"]
    output: 4
    explanation: bit -> but -> put -> pot -> dot has 4 transitions

                bit
               /   \
              but  big
            /        \
           put     
          /
        pot     
    
    graph = {
        "bit": ["but", "big"],
        "but": ["put"],
        "big": [],
        "put": ["pot"],
    }
    
    1) Step is to make a graph
    2) BS using que

    bit <-> but
    letter_1 = {
        "u" : 1
    }
    letter_2 = {
        "i" : 1,
    }
    """

    def find_diff(word1, word2):
        prev_word_letters = Collect(word1)
        curr_word_letters = Collect(word2)

        all_chars = set()
        for key_prev in prev_word_letters.keys():
            all_chars.add(key_prev)
        
        for key_curr in curr_word_letters.keys():
            all_chars.add(key_curr)
        
        diff = 0
        for char in all_chars:
            count_prev = prev_word_letters(char, 0)
            count_curr = curr_word_letters(char, 0)

            diff += abs(count_prev-count_curr)

        return True if diff != 1 else False

    graph = {}
    is_it = False
    words.append(source)
    for word1  in words: # making graph
        for word2 in words:
            if word1 == word2:
                continue

            if word1 == target: # clearifying is word in words
                is_it = True
            
            if find_diff(word1, word2):
                if word1 in graph:
                    graph[word1].append(word2) # word as a neigh

                else:
                    graph[word1] = [word2]
            
    
    if not is_it:
        return -1
    
    paths = 0
    qeue = deque([graph[source]])
    while qeue:
        pass
        # Traversing through graph
        
