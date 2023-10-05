import typer
from rich.console import Console
from rich.table import Table
from habit import Habit
import questionary
import datetime as dt
from database import get_habit_by_position, calculate_streak
import csv


def increment_streak(position: int):
    """
    - increment streak everyday by 1
    - if habit is checked and then unchecked decrease by 1 again
    """

    cur_habit = get_habit_by_position(position)
    print(cur_habit)

    # cur_date = date.today()
    datetime_today = dt.datetime.now().replace(second=0, microsecond=0)
    today = dt.datetime.now().date()

    # print(cur_habit[2])
    if cur_habit["last_date_checked"] is None:
        cur_habit["last_date_checked"] = today
        cur_habit["streak"] = 1
    else:
        datetime_cur_habit = dt.datetime.strptime(
            cur_habit["last_date_checked"], "%Y-%m-%d %H:%M:%S"
        )
        
        date_cur_habit = datetime_cur_habit.date()
        print(datetime_cur_habit)

        if date_cur_habit == today:
            # cur_habit["streak"] = 1
            # cur_habit["last_date_checked"] = datetime_today
            print("if")
            return 
            
        elif  today - date_cur_habit > dt.timedelta(days=1):
            datetime_cur_habit = datetime_today
            cur_habit["streak"] = 1
            cur_habit["last_date_checked"] = datetime_cur_habit
            print("elif 1")
        elif today - date_cur_habit == dt.timedelta(days=1) or date_cur_habit is None:
            cur_habit["last_date_checked"] = datetime_cur_habit
            cur_habit["streak"] += 1
            print("elif 2")
        else:
            print("Error: there is a problem with the last checked date.")
            return

    calculate_streak(cur_habit["position"], cur_habit["streak"])

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
            [
                "Make the bed",
                "Work",
                "Weekly",
                "2023-07-10 11:10:00",
                "2023-08-21 15:10:00",
                "3",
                2,
            ]
        )
        writer.writerow(
            [
                "Cuddle dog",
                "Work",
                "Weekly",
                "2023-07-10 19:10:00",
                "2023-08-21 12:10:00",
                "3",
                2,
            ]
        )
        writer.writerow(
            [
                "Cuddle dog",
                "Work",
                "Weekly",
                "2023-07-10 17:10:00",
                "2023-08-21 17:10:00",
                "3",
                2,
            ]
        )
        writer.writerow(
            [
                "Cuddle dog",
                "Work",
                "Weekly",
                "2023-07-10 13:10:00",
                "2023-10-04 11:10:00",
                "3",
                1,
            ]
        )
