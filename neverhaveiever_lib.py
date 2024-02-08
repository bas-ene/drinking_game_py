import requests

class NeverHaveIEver:
    def __init__(self, r_rated=False) -> None:
        self.__url = f'https://api.truthordarebot.xyz/api/nhie?&rating=PG&rating=PG13{"&rating=R" if r_rated else ""}'
        self.r_rated = r_rated
    

    def serve_nhie(self) -> str:
        response = requests.get(self.__url)

        if response.status_code == 200:
            return response.json()['question']

        raise Exception('Failed to fetch data from the API')

