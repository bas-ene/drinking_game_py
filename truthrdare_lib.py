import requests 

class TruthOrDare:

    def __init__(self, r_rated = False) -> None:
        self.__truth_endp = f'https://api.truthordarebot.xyz/api/truth?rating=PG&rating=PG13{"&rating=R" if r_rated else ""}'
        self.__dare_endp = f'https://api.truthordarebot.xyz/api/dare?rating=PG&rating=PG13{"&rating=R" if r_rated else ""}'
        self.r_rated = r_rated

    def serve_truth(self) -> str:
        response = requests.get(self.__truth_endp)
        
        if response.status_code == 200:
            return response.json()['question']

        raise Exception("Error while retrieving data from API")

    def serve_dare(self) -> str:
        response = requests.get(self.__dare_endp)
        
        if response.status_code == 200:
            return response.json()['question']

        raise Exception("Error while retrieving data from API")
