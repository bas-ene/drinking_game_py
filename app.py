from deck_lib import Deck, Card
from trivia_lib import Trivia

def handleCard(card: Card) -> bool:

    if card.value == 'JOKER':
        return False
    match card.suit:
        case 'CLUBS' | 'DIAMONDS' | 'HEARTS' | 'SPADES':
            question = trivia.serve_question()
            print(f'Question: {question["question"]["text"]}')

            user_answer = str(input('Your answer: '))
            success = user_answer.lower() == question['correctAnswer'].lower()

            if success:
                print('Correct!')
            else:
                print(f'Correct answer: {question["correctAnswer"]}')

            return success

        case _: 
            raise Exception('Invalid suit')

if __name__ == '__main__':
    deck = Deck()
    trivia = Trivia()
    while input('Draw a card? (y/n): ') == 'y':
        drawn = deck.draw(1)[0]
        print(f'You drew: {drawn}')

        has_won = handleCard(drawn)

        if has_won:
            print('You won!')
        else: 
            print('You lost!')
