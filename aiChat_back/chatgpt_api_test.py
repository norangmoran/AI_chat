import config

from openai import OpenAI
from pprint import pprint

api_key = config.openai_api_key
client = OpenAI(api_key=api_key)

model = "gpt-4o-mini-2024-07-18"

messages = [
  {"role": "system", "content": "You are a helpful assistant."},
  {"role": "user", "content": "who won the world series in 2020?"},
]

response = client.chat.completions.create(model=model, messages=messages).model_dump()

pprint(response)