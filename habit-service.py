import typer
from rich.console import Console
from rich.table import Table
from habit import Habit
from database import add_habit, delete_habit, show_habits, modify_name, modify_period, complete_habit
from simple_term_menu import TerminalMenu 

'''
- add_habit
- modify_habit
- delete_habit
- show_habits
- status
'''

app = typer.Typer()

@app.command(short_help='adds a new habit')
def add(habit_name= None, period=None, habit_id = None, status=None, streak=None, start_date=None, end_date=None):

    # create new Habit from input data from console
    habit = Habit(habit_id, habit_name, period, status, streak, start_date, end_date)
    
    habit.habit_name = typer.prompt('What is the name of your new habit? ')
    
    print('What is the period of your new habit? ')
    period_options = ['Daily', 'Weekly']
    terminal_menu = TerminalMenu(period_options)
    menu_entry_index = terminal_menu.show()
    habit.period = period_options[menu_entry_index]
    print(f"You have selected {habit.period}!")
        
    # TODO add start_date option (if not today when?)
    
    add_habit(habit)
    show()
     #TODO implement simple term menu https://pypi.org/project/simple-term-menu/ 
    
'''
takes habit_id and one additional habit property param (one command per editable property; habit_name, period, status (end_date))
'''
@app.command(short_help= 'modify habit name of an existing habit')
def modify_habit_name (habit_id: str, habit_name: str):
    # get habit from habit_id
    modify_name(habit_id, habit_name)
    show()

@app.command(short_help= 'modify period of an existing habit')
def modify_habit_period (habit_id: str, period: str):
    # get habit from habit_id

    modify_period(habit_id, period)
    # TODO API call to persist data OR persist data inline
    show()
    

@app.command(short_help= 'check habit for today')
def check (habit_id: str):
    # get habit from habit_id
    check_habit = typer.confirm("Do you want to check this habit?", default= True)
    if check_habit:
        complete_habit(habit_id)
        print('Habit checked')
    else:
        print('Not checking habit')

    show()
    # TODO API call to persist data OR persist data inline
    
    
    
'''
takes one param: habit_id
'''
@app.command(short_help='permanently remove habit from habit tracker')
def delete(habit_id: str):
    
    delete_habit(habit_id)
    show()
'''
    show_habit: gets all the rows from data file in some nice typer view
'''
@app.command(short_help= 'show all currently existing habits')
def show():
    tasks = show_habits()
    table = Table()
    table.padding = 1
    table.add_column('habit ID', justify='right', style='bold cyan', no_wrap=True)
    table.add_column('habit name', style='magenta')
    table.add_column('period', style='green')
    table.add_column('status', justify= 'center')
    table.add_column('streak', justify= 'center', style='orange1')
    table.add_column('start date', style='red')
    
    # for num, habit in enumerate(tasks, start =1):
    #     status_style = '✅' if habit.status == True else '❌'
    #     #dt_string = habit.start_date.strptime("%d/%m/%Y")
    #     table.add_row(str(habit.habit_id), habit.habit_name, habit.period, str(status_style), str(habit.streak), habit.start_date)
        
    for num, habit in enumerate(tasks, start =1):
        status_style = '✅' if habit[3] == 1 else '❌'
        table.add_row(str(habit[0]), habit[1], habit[2], str(status_style), str(habit[4]), habit[5])
    console = Console()
    console.print(table)
    
    show_habits()
    
if __name__== '__main__':
    app()