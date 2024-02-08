import requests

class Trivia:
    def __init__(self):
        self.__api_url = 'https://the-trivia-api.com/v2/questions'
        self.__questions = self.__get_questions()


    def __get_questions(self, amount = 10) -> list[dict]:
        response = requests.get(self.__api_url, params={'amount': amount})
        if response.status_code == 200:
            return response.json()

        raise Exception('Failed to fetch data from the API')

    def serve_question(self) -> dict:
        if len(self.__questions) == 0:
            self.__questions = self.__get_questions()
        return self.__questions.pop(0)
