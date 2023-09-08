import sqlite3 #import sqlite
from typing import List
import datetime
from habit import Habit

conn = sqlite3.connect('habits.db') #connect database and set database name to habits.db
c = conn.cursor() #create cursor

#create function to execute table
def create_table(): #create new table if todos doesn't exist yet
    c.execute("""CREATE TABLE IF NOT EXISTS habits ( 
            habit_name text,
            category text,
            duration text,
            time_created text,
            date_completed text,
            status integer,
            position integer
            )""") #input all stored fields of model class

create_table()

#create function to insert Habit
def insert_habit(habit:Habit):
    c.execute('SELECT count(*) FROM habits') #execute select count(*)
    count = c.fetchone()[0] #fetch first item (number of items in table)
    habit.position = count if count else 0 #if we have no items we start at 0 otherwise at count
    with conn: #open connection; as soon as we get out of conn (context manager) everything will be committed
        c.execute('INSERT INTO habits VALUES (:habit_name, :category, :duration, :time_created, :date_completed, :status, :position )', #insert all fields; uses parameter substitutes
                  {'habit_name': habit.habit_name, 'category': habit.category, 'duration': habit.duration, 'time_created': habit.time_created,
                   'date_completed': habit.date_completed, 'status': habit.status, 'position': habit.position}) #add dictionary and specify each value

#create function to get all Todos
def get_all_habits() -> List[Habit]:
    c.execute('select * from habits') #select all from todos
    results = c.fetchall() #fetch all
    habits = [] #convert todos to tuple
    for result in results: #iterate over all tuples
        habits.append(Habit(*result)) #*unpacks all arguments and put it to constructor to todoclass & creates the todoobject
    return habits #returns todos

#create function to delete Todos
def delete_habit_from_db(position):
    c.execute('select count(*) from habits')
    count = c.fetchone() [0] #get number of items in table

    with conn:
        c.execute("DELETE from habits WHERE position=:position", {"position": position}) #execute deletion command
        for pos in range(position+1, count):
            change_position(pos, pos-1, False) #shift all remaining items one position down, when left it calls commit

#create function to shift items one position down
def change_position(old_position: int, new_position: int, commit=True): #optional commit statement
    c.execute('UPDATE habits SET position = :position_new WHERE position = :position_old',
              {'position_old': old_position, 'position_new': new_position}) # set position where the old position was, shift all positions one down
    if commit:
        conn.commit()

#create update_todo function
def update_habit_from_db(position:int, new_attributes:[]):
    with conn:
        for attribute in new_attributes:
            if attribute["attr_name"] == "habit_name":
                c.execute('UPDATE habits SET habit_name = :habit_name WHERE position = :position',
                          {'position': position, 'habit_name': attribute["attr_value"]})
            elif attribute["attr_name"] == "category":
                c.execute('UPDATE habits SET category = :category WHERE position = :position',
                          {'position': position, 'category': attribute["attr_value"]})
            elif attribute["attr_name"] == "duration":
                c.execute('UPDATE habits SET duration = :duration WHERE position = :position',
                          {'position': position, 'duration': attribute["attr_value"]})
            elif attribute["attr_name"] == "status":
                c.execute('UPDATE habits SET status = :status WHERE position = :position',
                          {'position': position, 'status': attribute["attr_value"]})

#create complete_todo function
def toggle_habit_status_from_db(position: int, new_status:int):
    with conn:
        c.execute('UPDATE habits SET status = :status, date_completed = :date_completed WHERE position = :position ',
                  {'position': position, 'status': new_status, 'date_completed': datetime.datetime.now().isoformat()}) #status 2 =completed, get time when completed