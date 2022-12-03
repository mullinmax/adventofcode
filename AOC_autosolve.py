#import libraries
import requests
from bs4 import BeautifulSoup
import os
import openai
from datetime import datetime
from simple_term_menu import TerminalMenu
from pathlib import Path

class prompt():
    code_starter = '''with open('data.txt') as f:'''

    def __init__(self, date):
        self.change_date(date)

    def change_date(self, date):
        self.date = date
        self.dir = os.path.join(date.strftime("%Y"),date.strftime("%-d"))
        self.raw_text_path = os.path.join(self.dir, 'raw_prompt.html')
        self.gpt_prompt_path = os.path.join(self.dir, 'gpt_prompt.txt')
        self.gpt_program_path = os.path.join(self.dir, 'gpt_program.py')
        self.output_path = os.path.join(self.dir, 'output.txt')

    def scrape_prompt(self):
        url = f'https://adventofcode.com/{self.date.strftime("%Y")}/day/{self.date.strftime("%-d")}'
        page = requests.get(url)
        soup = BeautifulSoup(page.content, 'html.parser')
        desc = soup.find('article', class_='day-desc')
        text = ''.join([str(e) for e in desc.contents])
        self.raw_text(text)

    def raw_text(self, text:str=None)-> str:
        return self.__generic_text__(path=self.raw_text_path, text=text)

    def gpt_prompt(self, text:str=None)-> str:
        return self.__generic_text__(path=self.gpt_prompt_path, text=text)

    def gpt_program(self, text:str=None)-> str:
        return self.__generic_text__(path=self.gpt_program_path, text=text)

    def output(self, text:str=None)-> str:
        return self.__generic_text__(path=self.output_path, text=text)

    def __generic_text__(self, path, text:str=None)-> str:
        Path(self.dir).mkdir(parents=True, exist_ok=True)
        if text is not None:
            with open(path, 'w+') as f:
                f.write(text)
        with open(path, 'r') as f:
            return f.read()

    def refine_prompt(self):
        refined_text = self.raw_text() + f'''Make sure you read the prompt carefully and understand it fully. The program should output a single number as a solution. Write a python 3.10 program with comments that solves the problem:\n{self.code_starter}'''
        self.gpt_prompt(text=refined_text)

    def send_to_gpt(self):
        openai.api_key = os.getenv("OPENAI_API_KEY")
        
        refined_prompt_text = self.gpt_prompt()
        if len(refined_prompt_text) < 10:
            raise Exception('prompt is way too short')

        response = openai.Completion.create(
            model="text-davinci-003",
            prompt= refined_prompt_text,
            temperature=1,
            max_tokens=1000,
            top_p=0.8,
            frequency_penalty=0.1,
            presence_penalty=0.0,
            best_of=5
        )
        program_text = self.code_starter + response['choices'][0]['text']
        self.gpt_program(text=program_text)
    
    def run_solution(self):
        root_wd = os.getcwd()
        os.chdir(self.dir)
        os.system(f'python gpt_program.py > output.txt')
        os.chdir(root_wd)        

    def run_debugged_solution(self):
        root_wd = os.getcwd()
        os.chdir(self.dir)
        os.system(f'python debugged_program.py > output.txt')
        os.chdir(root_wd)

    
def change_prompt_date(p):
    now = datetime.now()
    # get year we want to run
    if now.month == 12:
        options = [str(i) for i in range(2015, now.year+1)]
    else:        
        options = [str(i) for i in range(2015, now.year)]
    options.reverse()
    terminal_menu = TerminalMenu(options)
    menu_entry_index = terminal_menu.show()
    year = int(options[menu_entry_index])
    print('year:',year)

    # get day / prompt number to run
    if now.year == year and now.month == 12:
            options = [str(i) for i in range(1, now.day+1)]
    else:        
        options = [str(i) for i in range(1, 25)]
    options.reverse()
    terminal_menu = TerminalMenu(options)
    menu_entry_index = terminal_menu.show()
    day = int(options[menu_entry_index])
    print('day:',day)

    p.change_date(datetime(year=year,day=day,month=12))

def main():
    p = prompt(datetime(year=2015,day=1,month=12))
    change_prompt_date(p)
    programs = {
        "retreive prompt":lambda:p.scrape_prompt(),
        "refine prompt":lambda:p.refine_prompt(),
        "send to GPT":lambda:p.send_to_gpt(),
        "run solution":lambda:p.run_solution(),
        "run debugged solution":lambda:p.run_debugged_solution(),
        "view output":lambda:print(p.output()),
        "different prompt":lambda:change_prompt_date(p),
        "exit":lambda:exit(),
    }
    all_keys = list(programs.keys())
    terminal_menu = TerminalMenu(all_keys)
    while True:
        menu_entry_index = terminal_menu.show()
        selection = all_keys[menu_entry_index]
        print(selection)
        programs[selection]()
        

if __name__ == "__main__":
    main()