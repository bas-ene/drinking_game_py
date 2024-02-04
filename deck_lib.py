import requests, os, time

class Deck: 

    def __init__(self) -> None:
        #if there is no deck id sacved or the one saved is older than 2 weeks, get a new one
        self.deck_id = self.get_deck_id()

        self.shuffle()

    # the deck id is saved in a file, alongside the unix timestamp of when it was last used
    def get_deck_id(self) -> str:
        #check if the file exists
        if not os.path.exists('deck_id.txt'):
            deck_id = self.get_new_deck_id()
            with open('deck_id.txt', 'w') as file:
                file.write(f'{deck_id},{int(time.time())}')
            return deck_id

        else: 
            with open('deck_id.txt', 'r') as file:
                deck_id, timestamp = file.read().split(',')

                #if the deck id is older than 2 weeks, get a new one
                if int(timestamp) < int(time.time()) - 1209600:
                    deck_id = self.get_new_deck_id()
                    with open('deck_id.txt', 'w') as file:
                        file.write(f'{deck_id},{int(time.time())}')

                return deck_id

    def get_new_deck_id(self) -> str:
        url = f'https://deckofcardsapi.com/api/deck/new/shuffle/'
        params = {
            'deck_count': 2, 
            'jokers_enabled': 'true'
        }
        response = requests.get(url, params=params)

        if response.status_code != 200:
            raise Exception(f'Failed to get new deck id: {response.text}')
        if response.json()['success'] is False:
            raise Exception(f'Failed to get new deck id: {response.json()}')

        self.remaining_cards = response.json()['remaining']
        return response.json()['deck_id']

    def draw(self, count: int) -> list:
        if self.remaining_cards < count:
            self.shuffle()
        url = f'https://deckofcardsapi.com/api/deck/{self.deck_id}/draw/'
        params = {
            'count': count
        }
        response = requests.get(url, params=params)

        if response.status_code != 200:
            raise Exception(f'Failed to draw cards: {response.text}')
        if response.json()['success'] is False:
            raise Exception(f'Failed to draw cards: {response.json()}')

        self.remaining_cards = response.json()['remaining']
        cards = response.json()['cards']
        return [Card(card['suit'], card['value']) for card in cards]

    def shuffle(self) -> None:
        url = f'https://deckofcardsapi.com/api/deck/{self.deck_id}/shuffle/'
        response = requests.get(url)

        if response.status_code != 200:
            raise Exception(f'Failed to shuffle deck: {response.text}')
        if response.json()['success'] is False:
            raise Exception(f'Failed to shuffle deck: {response.json()}')

        self.remaining_cards = response.json()['remaining']
        return

class Card:
    def __init__(self, suit: str, value: str) -> None:
        self.suit = suit
        self.value = value

    def __repr__(self) -> str:
        if self.value == 'JOKER':
            return f'{self.suit} {self.value}'
        else:
            return f'{self.value} of {self.suit}'
