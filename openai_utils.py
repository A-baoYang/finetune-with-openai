import configparser
from time import sleep

import openai


class OpenAIAPI:
    def __init__(self):
        self.openai = openai

    def login(self):
        config = configparser.ConfigParser()
        config.read_file(open("secret.cfg"))
        self.openai.api_key = config.get("OpenAI", "API_KEY")

    def get_embeddings(self, text, model="text-embedding-ada-002"):
        """免費帳戶有時間內之取用上限"""
        text = text.replace("\n", " ")
        success = False
        while not success:
            try:
                res = self.openai.Embedding.create(input=[text], model=model)["data"][
                    0
                ]["embedding"]
                success = True

            except Exception as e:
                print(e)
                sleep(60)
        return res

    def get_text_completion(
        self, prompt, model="text-davinci-003", generation_params=None
    ):
        """generation_params (default)
        - temperature=0.7
        - max_tokens=1024
        """
        if not generation_params:
            generation_params = {"temperature": 0.7, "max_tokens": 1024}
        print(f"\nPrompt: {prompt}\nWith params: {generation_params}")
        response = self.openai.Completion.create(
            model=model, prompt=prompt, **generation_params
        )
        res = response["choices"][0]["text"].strip()
        print(f"\nGPT-3 Reply: {res}\n")
        return res

    def get_chat_completion(
        self, messages, model="gpt-3.5-turbo", generation_params=None
    ):
        """generation_params (default)
        - temperature=0.7
        - max_tokens=1024
        """
        if not generation_params:
            generation_params = {"temperature": 0.7, "max_tokens": 1024}
        print(f"\nMessages: {messages}\nWith params: {generation_params}")

        response = self.openai.ChatCompletion.create(
            model=model, messages=messages, **generation_params
        )
        res = response["choices"][0]["message"]["content"].strip()
        print(f"\nChatGPT Reply: {res}\n")
        return res
