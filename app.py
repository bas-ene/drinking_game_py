import random
from deck_lib import Deck, Card
from trivia_lib import Trivia
from neverhaveiever_lib import NeverHaveIEver as Nhie

def handleCard(card: Card):

    if card.value == 'JOKER':
        print('You lostt!')
        return 

    match card.suit:
        case 'CLUBS' :
            question = trivia.serve_question()
            print(f'Question: {question["question"]["text"]}')
            print('Options:')
            possible_answers = question['incorrectAnswers'] + [question['correctAnswer']]
            random.shuffle(possible_answers)
            for i, answer in enumerate(possible_answers):
                print(f'{i + 1}. {answer}')
            user_answer_idx = input('Your answer: ')
            while not user_answer_idx.isdigit() or int(user_answer_idx) < 1 or int(user_answer_idx) > 4:
                user_answer_idx = input('Your answer: ')
                print('Invalid answer')

            user_answer = possible_answers[int(user_answer_idx) - 1]
            success = user_answer == question['correctAnswer']

            if success:
                print('Correct!')
            else:
                print('Incorrect!')
                print(f'Correct answer: {question["correctAnswer"]}')
            
        case 'DIAMONDS':
            print(nhie.serve_nhie())

            print('Have you ever done this? (y/n): ')
            user_answer = input()
            while user_answer not in ['y', 'n']:
                user_answer = input('Invalid answer. Please enter y or n: ')
            if user_answer == 'y':
                print('You\'ve lcst!')
            else:
                print('You\'ve won!')

        case 'HEARTS':
            print('You won a heart!')

        case 'SPADES':
            print('You won a spade!')

        case _: 
            raise Exception('Invalid suit')

if __name__ == '__main__':
    deck = Deck()
    trivia = Trivia()
    nhie = Nhie(r_rated=True)
    while input('Draw a card? (y/n): ') == 'y':
        drawn = deck.draw(1)[0]
        print(f'You drew: {drawn}')
        
        # handleCard(drawn)
        handleCard(Card('DIAMONDS', '2'))
