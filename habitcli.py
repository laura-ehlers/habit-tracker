import typer
from rich.console import Console
from rich.table import Table
from habit import Habit
import questionary
import datetime
from database import get_all_habits, delete_habit_from_db, insert_habit, toggle_habit_status_from_db, update_habit_from_db

console = Console() #create Console object from rich library
app = typer.Typer() #create Typer object, Typer=CLI

@app.command(short_help="Start of the application")
def start_app():
    '''
    - starting point of the application
    - shows user everything they can do with the app
    - can be repeated as often as wanted
    '''
    first_run = True
    while first_run==True or end_decision == "Yes":
        start_decision = questionary.select("What do you want to do?", choices=["Add a habit", "Delete a habit", "Update a habit", "Show all habits"]).ask()
        match start_decision:
            case "Add a habit":
                add_habit()
            case "Delete a habit":
                delete_habit()
            case "Update a habit":
                update_habit()
            case "Show all habits":
                show_habit()
        first_run = False
        end_decision = questionary.select("Do you want to do anything else?", choices=["Yes", "No"]).ask()
    
@app.command(short_help='adds a new habit')
def add_habit():
    habit_name = questionary.text("What is the name of the habit you want to create?").ask()
    category = questionary.select("Choose the category your habit belongs to!",
                                  choices=["Work", "University", "Housework", "Freetime", "Selfcare"]).ask()
    duration = questionary.select("Do you want to do this habit daily or weekly?",
                                  choices=["Daily", "Weekly"]).ask()
    time_created = datetime.datetime.now().isoformat()
    typer.echo(f"adding {habit_name} {category} {duration} {time_created}")
    habit = Habit(habit_name, category, duration, time_created)
    insert_habit(habit)
    show_habit()

@app.command()
def delete_habit():
    show_habit()
    position = int(questionary.text("At which position is the habit you want to delete?").ask())
    typer.echo(f"deleting {position}")
    delete_habit_from_db(position - 1)
    show_habit()

@app.command()
def update_habit ():
    position = int(questionary.text("At which position is the habit you want to update?").ask())
    typer.echo(f"updating {position}")
    changing_attributes = questionary.checkbox("Which attributes do you want to update?",
                                               choices=["habit name", "category", "duration", "state of completion"]).ask()
    new_attributes = []
    for attribute in changing_attributes:
        if attribute == "habit name":
            new_attr = questionary.text(f"{attribute}: ").ask()
            new_attributes.append({'attr_name':'habit_name', 'attr_value':new_attr})
        elif attribute == "category":
            new_attr = questionary.select("Choose the category your habit belongs to!",
                                  choices=["Work", "University", "Housework", "Freetime", "Selfcare"]).ask()
            new_attributes.append({'attr_name': 'category', 'attr_value': new_attr})
        elif attribute == "duration":
            new_attr = questionary.select("Do you want to do this habit daily or weekly?",
                                  choices=["Daily", "Weekly"]).ask()
            new_attributes.append({'attr_name': 'duration', 'attr_value': new_attr})
        elif attribute == "state of completion":
            new_attr = questionary.select("What is the state of the habit?",
                                  choices=["Done", "Unfinished"]).ask()
            new_state = 2 if new_attr else 1
            new_attributes.append({'attr_name': 'status', 'attr_value': new_state})

    update_habit_from_db(position - 1, new_attributes)
    show_habit()

@app.command()
def toggle_habit ():
    position = int(questionary.text("At which position is the habit you want to update?").ask())
    typer.echo(f"at {position}")

    status_query = questionary.select("What is the new status of this habit?",
                                      choices=["Completed", "Not completed"]).ask()
    typer.echo(f"new status: {status_query}")
    new_status = 2 if status_query == "Completed" else 1
    toggle_habit_status_from_db(position-1, new_status)
    show_habit()

@app.command()
def show_habit():
    habits = get_all_habits()
    console.print("[bold magenta]Habits[/bold magenta]!", "💻")  # color styling for printing in console

    table = Table(show_header=True, header_style="bold blue")  # add table header in blue
    table.add_column("#", style="dim", width=6)  # add additional styling in the following 4 lines
    table.add_column("Habits", min_width=20)
    table.add_column("Category", min_width=12, justify="right")
    table.add_column("Duration", min_width=12, justify="right")
    table.add_column("Done", min_width=12, justify="center")

    for idx, habit in enumerate(habits, start=1): #starts at 1 to iterate
        duration_str = habit.duration
        is_done_str = '✅' if habit.status == 2 else '❌' #at the beginning checked and true
        table.add_row(str(idx), habit.habit_name, habit.category, duration_str, is_done_str) #add table row with number, task, category (with styling due to f'[{c}], is done string
    console.print(table) #output table

if __name__ == "__main__": #if todocli.py is run as standalone name = main we run app
    app()