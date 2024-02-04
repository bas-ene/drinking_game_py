from deck_lib import Deck, Card

def handleCard(card: Card) -> bool:
    if card.value == 'JOKER':
        return False
    return True

if __name__ == '__main__':
    deck = Deck()

    while input('Draw a card? (y/n): ') == 'y':
        drawn = deck.draw(1)[0]
        print(f'You drew: {drawn}')

        has_won = handleCard(drawn)
        if has_won:
            print('You won!')
        else: 
            print('You lost!')

