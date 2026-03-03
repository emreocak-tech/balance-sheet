from google import genai
from google.genai import types
from abc import ABC,abstractmethod
from dotenv import load_dotenv
load_dotenv()
import os
import requests
gemini_api=os.getenv("GOOGLE_GEMINI")
exchange_rate_api=os.getenv("EXCHANGE_RATE_API")
class HelpfulUtils(ABC):
    def __init__(self):
        super().__init__()
    @abstractmethod
    def gemini_entegration(self,message):
        pass
    @abstractmethod
    def exchange_rate_api(self):
        pass
class Utils(HelpfulUtils):
    def gemini_entegration(self,message):
        try:
            client=genai.Client(api_key=gemini_api)
            response=client.models.generate_content( model="gemini-3-flash-preview",
            config=types.GenerateContentConfig(system_instruction="You are an quant trader and you want to explain basically what user said."),
            contents=message)
            return response.text
        except ConnectionError as c_error:
            print(f"Internet connection error : {c_error}")
        except Exception as except_error:
            print(f"General Error : {except_error}")
    def exchange_rate_api(self):
        try:
            response = requests.get(url=f"https://v6.exchangerate-api.com/v6/{exchange_rate_api}/latest/USD")
            data = response.json()
            return data['conversion_rates']['TRY']
        except ConnectionError as c_error:
            print(f"Internet connection error : {c_error}")
        except Exception as except_error:
            print(f"General Error : {except_error}")

