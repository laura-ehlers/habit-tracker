import typer
from rich.console import Console
from rich.table import Table
from habit import Habit
import questionary
from base import (
    add_habit,
    delete_habit,
    update_habit,
    show_habit,
    check_habit,
    get_sample_data,
    delete_all_habits,
)
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
        feature_check = questionary.select(
            "What do you want to do?",
            choices=["Go to habits", "Analyze habits", "Admin functionality"],
        ).ask()
        match feature_check:
            case "Go to habits":
                habit_decision = questionary.select(
                    "What do you want to do?",
                    choices=[
                        "Add a habit",
                        "Delete a habit",
                        "Update a habit",
                        "Show all habits",
                        "Check a habit",
                    ],
                ).ask()

                match habit_decision:
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
            case "Analyze habits":
                print("Analyze habits")

            case "Admin functionality":
                admin_decision = questionary.select(
                    "What do you want to do?",
                    choices=["Add habits from sample data", "Delete all habits"],
                ).ask()
                match admin_decision:
                    case "Add habits from sample data":
                        get_sample_data()
                    case "Delete all habits":
                        delete_all_habits()
        first_run = False
        end_decision = questionary.select(
            "Do you want to do anything else?", choices=["Yes", "No"]
        ).ask()


if __name__ == "__main__":  # if todocli.py is run as standalone name = main we run app
    app()
