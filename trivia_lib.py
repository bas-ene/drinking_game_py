import requests

class Trivia:
    def __init__(self):
        self.api_url = 'https://the-trivia-api.com/v2/questions'
        self.questions = self.__get_questions()


    def __get_questions(self, amount = 10) -> list:
        return requests.get(f'{self.api_url}?amount={amount}').json()

    def serve_question(self) -> dict:
        if len(self.questions) == 0:
            self.questions = self.__get_questions()
        return self.questions.pop(0)
