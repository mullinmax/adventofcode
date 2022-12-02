#import libraries
import requests
from bs4 import BeautifulSoup
import os
import openai
from datetime import datetime

# get prompt for the day
url = 'https://adventofcode.com/2022/day/{day}'.format(day = datetime.now().strftime("%-d"))
page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')
desc = soup.find('article', class_='day-desc')

code_start="with open('data.txt') as f:"
prompt = f'''{''.join(str(desc.contents))}
Make sure you read the prompt carefully and understand it fully. The program should output a single number as a solution. Write a python program with lots of comments to solve the problem:

{code_start}'''

openai.api_key = os.getenv("OPENAI_API_KEY")
response = openai.Completion.create(
  model="text-davinci-003",
  prompt= prompt,
  temperature=.9,
  max_tokens=1000,
  top_p=0.8,
  frequency_penalty=0.1,
  presence_penalty=0.0,
  best_of=5
)

with open('output.py', 'w') as f:
    f.write(code_start + response['choices'][0]['text'])

