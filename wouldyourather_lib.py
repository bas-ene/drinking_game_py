import requests

class WouldYouRather:
    def __init__(self, r_rated = False):
        self.__url = f'https://api.truthordarebot.xyz/api/wyr?&rating=PG&rating=PG13{"&rating=R" if r_rated else ""}'
        self.r_rated = r_rated
    
    def serve_wyr(self) -> str:
        response = requests.get(self.__url)

        if response.status_code == 200:
            return response.json()['question']

        raise Exception('Failed to fetch data from the API')
