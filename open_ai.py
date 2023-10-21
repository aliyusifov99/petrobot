import openai
from keys import API_KEY
class OpenAI:
    def __init__(self, text) -> None:
        self.text = text
    
    def generate_response(self):
        openai.api_key = API_KEY
        response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo-0301",
        messages=[
            {
            "role": "user",
            "content": self.text
            }
        ],
        temperature=1,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
        )
        return response['choices'][0]['message']['content']
    
    