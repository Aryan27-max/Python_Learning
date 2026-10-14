# The Game class - this is where everything comes together.
# Run this file to play:  python game.py

from deck import Deck
from hand import Hand


class Game:
    def play(self):
        game_number = 0
        games_to_play = 0

        # keep asking until we get a real number
        while games_to_play <= 0:
            try:
                games_to_play = int(input("How many games do you want to play? "))
            except ValueError:
                print("You must enter a number.")

        while game_number < games_to_play:
            game_number += 1

            deck = Deck()
            deck.shuffle()

            player_hand = Hand()
            dealer_hand = Hand(dealer=True)

            # everyone gets two cards to start
            for _ in range(2):
                player_hand.add_card(deck.deal(1))
                dealer_hand.add_card(deck.deal(1))

            print()
            print("*" * 30)
            print(f"Game {game_number} of {games_to_play}")
            print("*" * 30)
            player_hand.display()
            dealer_hand.display()

            if self.check_winner(player_hand, dealer_hand):
                continue  # someone already won, move on to the next game

            # Player's turn: hit or stand
            choice = ""
            while player_hand.get_value() < 21 and choice not in ["s", "stand"]:
                choice = input("Please choose 'Hit' or 'Stand': ").lower()
                print()
                while choice not in ["h", "s", "hit", "stand"]:
                    choice = input("Please enter 'Hit' or 'Stand' (or H/S): ").lower()
                    print()
                if choice in ["hit", "h"]:
                    player_hand.add_card(deck.deal(1))
                    player_hand.display()

            if self.check_winner(player_hand, dealer_hand):
                continue

            # Dealer's turn: dealer keeps taking cards until they reach 17
            player_value = player_hand.get_value()
            dealer_value = dealer_hand.get_value()

            while dealer_value < 17:
                dealer_hand.add_card(deck.deal(1))
                dealer_value = dealer_hand.get_value()

            dealer_hand.display(show_all_dealer_cards=True)

            if self.check_winner(player_hand, dealer_hand):
                continue

            print("Final Results")
            print("Your hand:", player_value)
            print("Dealer's hand:", dealer_value)

            self.check_winner(player_hand, dealer_hand, game_over=True)

        print("\nThanks for playing!")

    def check_winner(self, player_hand, dealer_hand, game_over=False):
        # Before the end, we only check for busts and blackjacks
        if not game_over:
            if player_hand.get_value() > 21:
                print("You busted. Dealer wins! 😭")
                return True
            elif dealer_hand.get_value() > 21:
                print("Dealer busted. You win! 😀")
                return True
            elif dealer_hand.is_blackjack() and player_hand.is_blackjack():
                print("Both players have blackjack! Tie! 🤨")
                return True
            elif player_hand.is_blackjack():
                print("You have blackjack. You win! 😀")
                return True
            elif dealer_hand.is_blackjack():
                print("Dealer has blackjack. Dealer wins! 😭")
                return True
        else:
            # At the very end, just compare the scores
            if player_hand.get_value() > dealer_hand.get_value():
                print("You win! 😀")
            elif player_hand.get_value() == dealer_hand.get_value():
                print("Tie! 🤨")
            else:
                print("Dealer wins. 😭")
            return True
        return False


# This line means "only start the game if this file is run directly"
if __name__ == "__main__":
    g = Game()
    g.play()
