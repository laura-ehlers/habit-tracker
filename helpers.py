import typer
from rich.console import Console
from rich.table import Table
from habit import Habit
import questionary
import datetime as dt
from database import (
    get_all_habits,
    delete_habit_from_db,
    insert_habit,
    toggle_habit_status_from_db,
    update_habit_from_db,
    get_habit_by_position,
)
import csv


def increment_streak(position: int):
    """
    - increment streak everyday by 1
    - if habit is checked and then unchecked decrease by 1 again
    """

    cur_habit = get_habit_by_position(position)

    # cur_date = date.today()
    cur_date = dt.datetime.combine(dt.date.today(), dt.datetime.min.time())

    # print(cur_habit[2])
    if cur_habit["last_date_checked"] is None:
        cur_habit["last_date_checked"]= cur_date
        cur_habit["streak"] += 1

    else:
        date_cur_habit = dt.datetime.strptime(
            cur_habit["last_date_checked"], "%Y-%m-%d"
        )

        if date_cur_habit == cur_date:
            return
        elif date_cur_habit - cur_date > dt.timedelta(days=1):
            date_cur_habit = cur_date
            cur_habit["streak"]  = 0
            cur_habit["last_date_checked"] = date_cur_habit
        elif date_cur_habit - cur_date == dt.timedelta(days=1) or date_cur_habit is None:
            cur_habit["last_date_checked"] = date_cur_habit
            cur_habit["streak"]  += 1
        else:
            print("Error: there is a problem with the last checked date.")
    
    return cur_habit


def write_csv():
    with open("sample_data.csv", "w", newline="") as file:
        writer = csv.writer(file)

        writer.writerow(
            [
                "habit_name",
                "category",
                "duration",
                "date_created",
                "last_date_checked",
                "streak",
                "status",
            ]
        )
        writer.writerow(
            ["Make the bed", "Work", "Weekly", "2023-07-10", "2023-08-21", "3", 2]
        )
        writer.writerow(
            ["Cuddle dog", "Work", "Weekly", "2023-07-10", "2023-08-21", "3", 2]
        )
        writer.writerow(
            ["Cuddle dog", "Work", "Weekly", "2023-07-10", "2023-08-21", "3", 2]
        )
        writer.writerow(
            ["Cuddle dog", "Work", "Weekly", "2023-07-10", "2023-09-10", "3", 1]
        )
