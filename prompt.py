#import libraries
import requests
from bs4 import BeautifulSoup
import os
import openai
from datetime import datetime
from pathlib import Path

class prompt():
    part_one_distilation_str = '\nWrite a distilled version of the prompt. Preserve any examples in the prompt. Then write a detailed outline of how a program should efficiently solve the problem. you may include pseudo code where helpful'
    part_two_distilation_str = f'{part_one_distilation_str}. The program should only solve part 2, use the information from the already competed part 1 for context only'
    code_starter_str = "\nimport sys\nwith open(sys.argv[1]) as f:"
    program_prompt_str = f'''\nWrite a Python 3.10 program that solves the above problem, your code should print just the solution and nothing else:\n{code_starter_str}'''
    def __init__(self, date):
        self.set_date(date)
        self.aoc_cookie = os.environ.get('AOC_COOKIE')
        if self.aoc_cookie is None:
            raise Exception('AOC_COOKIE enviroment variable not set. Please see readme for setup instructions')
        openai.api_key = os.getenv("OPENAI_API_KEY")

    def set_date(self, date:datetime):
        self.date = date
        self.year = date.strftime("%Y")
        self.day = date.strftime("%-d")
        self.base_url = f'https://adventofcode.com/{self.year}/day/{self.day}'
        self.dir = os.path.join('prompts',self.year,self.day)
        self.prompt_part_one_path = os.path.join(self.dir, 'prompt_part_one.html')
        self.prompt_part_two_path = os.path.join(self.dir, 'prompt_part_two.html')
        self.data_path = os.path.join(self.dir, 'data.txt')
        self.refined_prompt_part_one_path = os.path.join(self.dir, 'refined_prompt_part_one.txt')
        self.refined_prompt_part_two_path = os.path.join(self.dir, 'refined_prompt_part_two.txt')
        self.part_one_program_path = os.path.join(self.dir, 'part_one.py')
        self.part_two_program_path = os.path.join(self.dir, 'part_two.py')
        self.part_one_output_path = os.path.join(self.dir, 'part_one_output.txt')
        self.part_two_output_path = os.path.join(self.dir, 'part_two_output.txt')

    def scrape_prompt(self):
        html = self.__generic_scrape_aoc__(self.base_url)
        soup = BeautifulSoup(html, 'html.parser')
        desc = soup.findAll('article', class_='day-desc')
        self.prompt_part_one(str(desc[0]))
        if len(desc) > 1:
            self.prompt_part_two(str(desc[1]))

    def scrape_data(self):
        self.data(self.__generic_scrape_aoc__(self.base_url + '/input'))

    def __generic_scrape_aoc__(self, url):
        return requests.get(url, headers={'Cookie': self.aoc_cookie}).text

    def prompt_part_one(self, text:str=None)-> str:
        return self.__generic_text__(path=self.prompt_part_one_path, text=text)

    def prompt_part_two(self, text:str=None)-> str:
        return self.__generic_text__(path=self.prompt_part_two_path, text=text)

    def data(self, text:str=None)-> str:
        return self.__generic_text__(path=self.data_path, text=text)

    def refined_part_one_prompt(self, text:str=None)-> str:
        return self.__generic_text__(path=self.refined_prompt_part_one_path, text=text)

    def refined_part_two_prompt(self, text:str=None)-> str:
        return self.__generic_text__(path=self.refined_prompt_part_two_path, text=text)

    def part_one_program(self, text:str=None)-> str:
        return self.__generic_text__(path=self.part_one_program_path, text=text)
    
    def part_two_program(self, text:str=None)-> str:
        return self.__generic_text__(path=self.part_two_program_path, text=text)

    def part_one_output(self, text:str=None)-> str:
        return self.__generic_text__(path=self.part_one_output_path, text=text)
    
    def part_two_output(self, text:str=None)-> str:
        return self.__generic_text__(path=self.part_two_output_path, text=text)

    def __generic_text__(self, path, text:str=None)-> str:
        Path(self.dir).mkdir(parents=True, exist_ok=True)
        if text is not None:
            with open(path, 'w+') as f:
                f.write(text)
        with open(path, 'r') as f:
            return f.read()

    def refine_part_one_prompt(self):
        refined_text = self.__generic_gpt__(self.prompt_part_one() + self.part_one_distilation_str) + self.program_prompt_str
        self.refined_part_one_prompt(text=refined_text)

    def refine_part_two_prompt(self):
        refined_text = self.__generic_gpt__(self.prompt_part_one() + self.prompt_part_two() + self.part_two_distilation_str) + self.program_prompt_str
        self.refined_part_two_prompt(text=refined_text)

    def generate_part_one_program(self):
        program_text = self.code_starter_str + self.__generic_gpt__(self.refined_part_one_prompt())
        self.part_one_program(text=program_text)

    def generate_part_two_program(self):
        program_text = self.code_starter_str + self.__generic_gpt__(self.refined_part_two_prompt())
        self.part_two_program(text=program_text)
    
    def __generic_gpt__(self, prompt):
        if len(prompt) < 10:
            raise Exception('prompt seems suspiciously short')

        completion = openai.chat.completions.create(
            model="gpt-4", 
            messages=[
                {"role": "system", "content": "Write code to solve the presented programming problem following the user's instructions"},
                {"role": "user", "content": prompt},
            ]
        )

        return completion.choices[0].message.content

    def run_part_one_solution(self):
        os.system(f'python {self.part_one_program_path} {self.data_path} > {self.part_one_output_path}')

    def run_part_two_solution(self):
        os.system(f'python {self.part_two_program_path} {self.data_path} > {self.part_two_output_path}')