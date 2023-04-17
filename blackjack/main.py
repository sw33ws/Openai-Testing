import random

# Define constants
SUITS = ["♠", "♣", "♦", "♥"]
RANKS = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
VALUES = {"2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "10": 10, "J": 10, "Q": 10, "K": 10, "A": 11}

# Define classes
class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return f"{self.rank}{self.suit}"

class Deck:
    def __init__(self):
        self.cards = [Card(suit, rank) for suit in SUITS for rank in RANKS]
        random.shuffle(self.cards)

    def deal_card(self):
        return self.cards.pop()

class Hand:
    def __init__(self):
        self.cards = []
        self.value = 0

    def add_card(self, card):
        self.cards.append(card)
        self.value += VALUES[card.rank]

    def adjust_for_ace(self):
        for card in self.cards:
            if card.rank == "A" and self.value > 21:
                self.value -= 10

class BlackjackGame:
    def __init__(self):
        self.deck = Deck()
        self.player_hand = Hand()
        self.dealer_hand = Hand()

    def deal_initial_cards(self):
        for _ in range(2):
            self.player_hand.add_card(self.deck.deal_card())
            self.dealer_hand.add_card(self.deck.deal_card())

    def player_turn(self):
        while True:
            print(f"Your cards: {', '.join(str(card) for card in self.player_hand.cards)}, current score: {self.player_hand.value}")
            if self.player_hand.value == 21:
                return "Blackjack!"
            elif self.player_hand.value > 21:
                return "Bust."
            else:
                choice = input("Type 'hit' to draw another card, or 'stand' to pass: ").lower()
                if choice == "hit":
                    self.player_hand.add_card(self.deck.deal_card())
                    self.player_hand.adjust_for_ace()
                else:
                    return "stand"

    def dealer_turn(self):
        while self.dealer_hand.value < 17:
            self.dealer_hand.add_card(self.deck.deal_card())
            self.dealer_hand.adjust_for_ace()

    def determine_winner(self):
        if self.player_hand.value > 21:
            return "Dealer"
        elif self.dealer_hand.value > 21:
            return "Player"
        elif self.player_hand.value == self.dealer_hand.value:
            return "Draw"
        elif self.player_hand.value == 21:
            return "Player"
        elif self.dealer_hand.value == 21:
            return "Dealer"
        elif self.player_hand.value > self.dealer_hand.value:
            return "Player"
        else:
            return "Dealer"

    def play(self):
        print("Welcome to Blackjack!")
        self.deal_initial_cards()
        game_over = False
        while not game_over:
            player_choice = self.player_turn()
            if player_choice == "stand":
                self.dealer_turn()
                winner = self.determine_winner()
                print(f"Your final cards: {', '.join(str(card) for card in self.player_hand.cards)}, current score: {self.player_hand.value}")
                print(f"Dealer's final cards: {', '.join(str(card) for card in self.dealer_hand.cards)}, current score: {self.dealer_hand.value}")
                if winner == "Player":
                    print("You win!")
                elif winner == "Dealer":
                    print("Dealer wins.")
                else:
                    print("It's a draw.")
                game_over = True

# Start the game
game = BlackjackGame()
game.play()