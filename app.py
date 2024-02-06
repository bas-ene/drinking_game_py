import random
from deck_lib import Deck, Card
from trivia_lib import Trivia
from neverhaveiever_lib import NeverHaveIEver as Nhie
from wouldyourather_lib import WouldYouRather as Wyr
from truthrdare_lib import TruthOrDare as ToD
def handleCard(card: Card):

    if card.value == 'JOKER':
        print('You lost!')
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

            print('Have you ever done this? (y/n/r): ')
            user_answer = input()
            while user_answer not in ['y', 'n', 'r']:
                user_answer = input('Invalid answer. Please enter y or n: ')
            if user_answer == 'y':
                print('You\'ve lcst!')
            elif user_answer == 'n':
                print('You\'ve won!')
            else:
                print('You\'ve refused to answer, so you lose!')

        case 'HEARTS':
            print(wyr.serve_wyr())
            
            print('Everyone has to answer, the minority loses!')

        case 'SPADES':
            print('Truth or dare? (t[ruth]/d[are]): ')
            user_answer = input()
            while user_answer.lower() not in ['t', 'd', 'truth', 'dare']:
                user_answer = input('Invalid answer. Please enter t, d, truth or dare: ')

            user_answer = user_answer.lower()
            if user_answer in ['t' , 'truth']:
                print(tod.serve_truth())
            else: 
                print(tod.serve_dare())

            print('You can refuse, but if you do so you lose!')

        case _: 
            raise Exception('Invalid suit')

if __name__ == '__main__':
    deck = Deck()
    trivia = Trivia()
    nhie = Nhie(r_rated=True)
    wyr = Wyr(r_rated=True)
    tod = ToD(r_rated=True)

    while input('Draw a card? (y/n): ') == 'y':
        drawn = deck.draw(1)[0]
        print(f'You drew: {drawn}')
        
        handleCard(drawn)
