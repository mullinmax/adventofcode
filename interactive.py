from simple_term_menu import TerminalMenu
from datetime import datetime

from prompt import prompt

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

    p.set_date(datetime(year=year,day=day,month=12))

def main():
    p = prompt(datetime(year=2015,day=1,month=12))
    change_prompt_date(p)
    programs = {
        "retreive prompt":lambda:p.scrape_prompt(),
        "retreive data":lambda:p.scrape_data(),
        "refine part one prompt":lambda:p.refine_part_one_prompt(),
        "refine part two prompt":lambda:p.refine_part_two_prompt(),
        "generate part one program":lambda:p.generate_part_one_program(),
        "generate part two program":lambda:p.generate_part_two_program(),
        "run part one program":lambda:p.run_part_one_solution(),
        "run part two program":lambda:p.run_part_two_solution(),
        "view part one output":lambda:print(p.part_one_output()),
        "view part two output":lambda:print(p.part_two_output()),
        "go to different day":lambda:change_prompt_date(p),
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