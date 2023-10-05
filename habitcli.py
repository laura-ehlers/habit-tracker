import typer
from rich.console import Console
from rich.table import Table
from habit import Habit
import questionary
from base import add_habit, delete_habit, update_habit, show_habit, check_habit, get_sample_data
import helpers

console = Console()
app = typer.Typer()  # create Typer object, Typer=CLI


@app.command(short_help="Start of the application")
def start_app():
    """
    - starting point of the application
    - shows user everything they can do with the app
    - can be repeated as often as wanted
    """
    print(helpers.increment_streak)
    first_run = True
    while first_run == True or end_decision == "Yes":
        start_decision = questionary.select(
            "What do you want to do?",
            choices=[
                "Add a habit",
                "Delete a habit",
                "Update a habit",
                "Show all habits",
                "Check a habit",
                "Add habits from sample data"
            ],
        ).ask()
        match start_decision:
            case "Add a habit":
                add_habit()
            case "Delete a habit":
                delete_habit()
            case "Update a habit":
                update_habit()
            case "Show all habits":
                show_habit()
            case "Check a habit":
                check_habit()
            case "Add habits from sample data":
                get_sample_data()
                
        first_run = False
        end_decision = questionary.select(
            "Do you want to do anything else?", choices=["Yes", "No"]
        ).ask()


if __name__ == "__main__":  # if todocli.py is run as standalone name = main we run app
    app()
