import random

class CardGame:
    """
    Complexity = 0(n/2) ->  0(n)
    """
    def __init__(self, arr):
        mid = len(arr) // 2
        self.first_pile = arr[mid:]
        self.second_pile = arr[:mid]
        self.winner = 0

    def play(self):
        first_sum, second_sum = 0, 0
        curr = 0
        while curr < len(self.first_pile):
            first_sum += self.first_pile[curr]
            second_sum += self.second_pile[curr]
            curr += 1
        if first_sum > second_sum:
            print("Congratualions First Player 🥳")
        print("Congratualions Second Player 🥳")
    
deck = [i for i in range(1, 53)]
random.shuffle(deck)
game = CardGame(deck)
game.play