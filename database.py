import sqlite3  # import sqlite
from typing import List
import datetime
from habit import Habit
import csv


conn = sqlite3.connect(
    "habits.db"
)  # connect database and set database name to habits.db
c = conn.cursor()  # create cursor

# c.execute('DROP TABLE habits')


# create function to execute table
def create_table():  # create new table if todos doesn't exist yet
    c.execute(
        """CREATE TABLE IF NOT EXISTS habits ( 
            position integer,
            habit_name text,
            category text,
            duration text,
            date_created datetime,
            last_date_checked datetime,
            streak integer,
            status integer
            )"""
    )  # input all stored fields of model class


create_table()


# create function to insert Habit
def insert_habit(habit: Habit):
    habit.position = (
        calculate_position()
    )  # if we have no items we start at 0 otherwise at count

    with (
        conn
    ):  # open connection; as soon as we get out of conn (context manager) everything will be committed
        c.execute(
            "INSERT INTO habits VALUES (:position, :habit_name, :category, :duration, :date_created, :last_date_checked, :streak, :status)",  # insert all fields; uses parameter substitutes
            {
                "position": habit.position,
                "habit_name": habit.habit_name,
                "category": habit.category,
                "duration": habit.duration,
                "date_created": habit.date_created,
                "last_date_checked": habit.last_date_checked,
                "streak": habit.streak,
                "status": habit.status,
            },
        )  # add dictionary and specify each value


# create function to get all Todos
def get_all_habits() -> List[Habit]:
    c.execute("select * from habits")  # select all from todos
    results = c.fetchall()  # fetch all
    habits = []  # convert todos to tuple
    for result in results:  # iterate over all tuples
        habits.append(
            Habit(*result)
        )  # unpacks all arguments and put it to constructor to todoclass & creates the todoobject
    return habits  # returns todos


# create function to delete Todos
def delete_habit_from_db(position):
    c.execute("select count(*) from habits")
    count = c.fetchone()[0]  # get number of items in table

    with conn:
        c.execute(
            "DELETE from habits WHERE position=:position", {"position": position}
        )  # execute deletion command
        for pos in range(position + 1, count):
            change_position(
                pos, pos - 1, False
            )  # shift all remaining items one position down, when left it calls commit


# create function to shift items one position down
def change_position(
    old_position: int, new_position: int, commit=True
):  # optional commit statement
    c.execute(
        "UPDATE habits SET position = :position_new WHERE position = :position_old",
        {"position_old": old_position, "position_new": new_position},
    )  # set position where the old position was, shift all positions one down
    if commit:
        conn.commit()


# create update_todo function
def update_habit_from_db(position: int, new_attributes: []):
    with conn:
        for attribute in new_attributes:
            if attribute["attr_name"] == "habit_name":
                c.execute(
                    "UPDATE habits SET habit_name = :habit_name WHERE position = :position",
                    {"position": position, "habit_name": attribute["attr_value"]},
                )

            elif attribute["attr_name"] == "category":
                c.execute(
                    "UPDATE habits SET category = :category WHERE position = :position",
                    {"position": position, "category": attribute["attr_value"]},
                )
            elif attribute["attr_name"] == "duration":
                c.execute(
                    "UPDATE habits SET duration = :duration WHERE position = :position",
                    {"position": position, "duration": attribute["attr_value"]},
                )
            elif attribute["attr_name"] == "status":
                c.execute(
                    "UPDATE habits SET status = :status WHERE position = :position",
                    {"position": position, "status": attribute["attr_value"]},
                )


# create complete_todo function
def toggle_habit_status_from_db(position: int, new_status: int):
    with conn:
        c.execute(
            "UPDATE habits SET status = :status, last_date_checked = :last_date_checked WHERE position = :position ",
            {
                "position": position,
                "status": new_status,
                "last_date_checked": datetime.datetime.now().replace(
                    second=0, microsecond=0
                ),
            },
        )  # status 2 =completed, get date when completed


def calculate_streak(position: int, streak: int):
    with conn:
        c.execute(
            "UPDATE habits SET streak = :streak WHERE position = :position",
            {"position": position, "streak": streak},
        )


def get_habit_by_position(position: int):
    c.execute(
        "SELECT position, streak, last_date_checked FROM habits WHERE position = :position",
        {"position": position},
    )  # select all from todos
    row = c.fetchone()
    with conn:
        return {
            "position": row[0],
            "streak": row[1],
            "last_date_checked": row[2],
        }


def get_number_of_habits():
    with conn:
        return c.execute("SELECT count(*) FROM habits")


def read_csv():
    # c.execute('DROP TABLE habits')
    with open("sample_data.csv", "r") as file:
        # create the object of csv.reader()
        csv_file_reader = csv.reader(file, delimiter=",")
        # skip the header
        next(csv_file_reader, None)

        position = ""
        habit_name = ""
        category = ""
        duration = ""
        date_created = ""
        last_date_checked = ""
        streak = ""
        status = 1

        table_query = """CREATE TABLE IF NOT EXISTS habits( 
            position integer,
            habit_name text,
            category text,
            duration text,
            date_created datetime,
            last_date_checked datetime,
            streak integer,
            status integer
            )"""

        c.execute(table_query)
        for row in csv_file_reader:
            for i in range(len(row)):
                position = calculate_position()
                habit_name = row[0]
                category = row[1]
                duration = row[2]
                date_created = row[3]
                last_date_checked = row[4]
                streak = row[5]
                status = row[6]

            insert_query = f"INSERT INTO habits VALUES ('{position}', '{habit_name}', '{category}', '{duration}', '{date_created}', '{last_date_checked}', '{streak}', {status})"
            c.execute(insert_query)

            conn.commit()
            # conn.close()


def calculate_position():
    c.execute("SELECT count(*) FROM habits")
    count = c.fetchone()[0]
    if count == 0:
        count = 1
        return count
    else:
        count += 1
        return count
