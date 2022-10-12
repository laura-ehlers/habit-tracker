'''
- analyze habit (other module)
- analyze habits (other module)
'''

'''
    analyze habit: gets position of one specific habit and reads the streak (definition of analytics)
'''

from habit import Habit
from rich.console import Console
from rich.table import Table
from database import show_habits, show_weekly_habits, show_daily_habits
import typer

app = typer.Typer()

@app.command(short_help= 'show all weekly habits')
def weekly_habits():
    tasks = show_weekly_habits()
    table = Table()
    table.padding = 1
    table.add_column('habit ID', justify='right', style='bold cyan', no_wrap=True)
    table.add_column('habit name', style='magenta')
    table.add_column('period', style='green')
    table.add_column('status', justify= 'center')
    table.add_column('streak', justify= 'center', style='orange1')
    table.add_column('start date', style='red')
            
    for num, habit in enumerate(tasks, start =1):
        status_style = '✅' if habit[3] == 1 else '❌'
        table.add_row(str(habit[0]), habit[1], habit[2], str(status_style), str(habit[4]), habit[5])
    console = Console()
    console.print(table)
    
    #show_habits()
    
@app.command(short_help= 'show all daily habits')
def daily_habits():
    tasks = show_daily_habits()
    table = Table()
    table.padding = 1
    table.add_column('habit ID', justify='right', style='bold cyan', no_wrap=True)
    table.add_column('habit name', style='magenta')
    table.add_column('period', style='green')
    table.add_column('status', justify= 'center')
    table.add_column('streak', justify= 'center', style='orange1')
    table.add_column('start date', style='red')
        
    for num, habit in enumerate(tasks, start =1):
        status_style = '✅' if habit[3] == 1 else '❌'
        table.add_row(str(habit[0]), habit[1], habit[2], str(status_style), str(habit[4]), habit[5])
    console = Console()
    console.print(table)
    
    show_habits()
    
def streak():
    if 
    
app()
    #TODO implement https://dateutil.readthedocs.io/en/stable/relativedelta.html#examples to track streak 