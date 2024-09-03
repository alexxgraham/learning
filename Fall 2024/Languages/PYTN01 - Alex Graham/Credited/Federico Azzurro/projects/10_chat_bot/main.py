# ----------------------------------------------------------------------
# |  main.py
# |
# |  by Federico Azzurro
# ----------------------------------------------------------------------
from difflib import SequenceMatcher
from datetime import datetime


class ChatBot:
    def __init__(self, name: str, responses: dict[str, str]) -> None:
        self.name = name
        self.responses = responses

    @staticmethod
    def calculate_similarity(input_sentence: str, response_sentence: str) -> float:
        sequence: SequenceMatcher = SequenceMatcher(a=input_sentence, b=response_sentence)
        return sequence.ratio()

    def get_best_response(self, user_input: str) -> tuple[str, float]:
        highest_similarity: float = 0.0
        best_match: str = 'Sorry, I didn\'t understand that.'

        for response in self.responses:
            similarity: float = self.calculate_similarity(user_input, response)
            if similarity > highest_similarity:
                highest_similarity = similarity
                best_match = self.responses[response]

        return best_match, highest_similarity

    def run(self) -> None:
        print(f'Hello! My name is {self.name}, how can I help you today?')
        while True:
            user_input: str = input('You: ')
            response, similarity = self.get_best_response(user_input)

            if response == 'GET_TIME':
                response = f'The time is: {datetime.now():%H:%M}'

            print(f'{self.name}: {response} (Similarity: {similarity:.2%})')

def main() -> None:
    responses: dict[str, str] = {
        'hello': 'Hello! How are you today?',
        'how are you': 'Great, thanks! What about you?',
        'what time is it': 'GET_TIME',
        'bye': 'Goodbye! Have a great day!'
    }

    chatbot: ChatBot = ChatBot(name='Bob', responses=responses)
    chatbot.run()

if __name__ == '__main__':
    main()

"""
1. Add more responses.
2. Add a way to exit the program through the chat.
3. Add some cool features, like checking for the weather forecast.
4. Make it so that if the accuracy falls below 50%, it returns a default response.

"""
