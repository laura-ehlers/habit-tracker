import sqlite3
from sqlite3 import Error
from unittest import result
from habit import Habit
from typing import Dict, List, Set
# from nanoid import generate

try:
    conn = sqlite3.connect('habits.db')
    c = conn.cursor()
except Error as e:
        print(e)
        
# finally:
#     if conn: 
#         conn.close()

def create_table():
    c.execute("""CREATE TABLE IF NOT EXISTS habits (
        habit_id text PRIMARY KEY,
        habit_name text,
        period text,
        status integer,
        streak integer,
        start_date text
    )""")

create_table()

def add_habit(habit: Habit):
    with conn:
        c.execute('INSERT INTO habits VALUES (:habit_id, :habit_name, :period, :status, :streak, :start_date)',
                  {'habit_id': habit.habit_id, 'habit_name': habit.habit_name, 'period': habit.period, 'status': habit.status, 'streak': habit.streak, 'start_date': habit.start_date})

def delete_habit(habit_id):   
    with conn:
        c.execute("DELETE FROM habits WHERE habit_id =  :habit_id",
                  {'habit_id': habit_id})        
        
def show_habits():
    c.execute('SELECT * FROM habits')
    return c.fetchall()
    
        
def modify_name(habit_id, habit_name):
    with conn:
        c.execute('UPDATE habits SET habit_name = :habit_name WHERE habit_id = :habit_id',
                  {'habit_id': habit_id, 'habit_name': habit_name})

def modify_period(habit_id, period):
    with conn:
        c.execute('UPDATE habits SET period = :period WHERE habit_id = :habit_id',
                  {'habit_id': habit_id, 'period': period})
        
def complete_habit(habit_id):
    with conn:
        c.execute('UPDATE habits SET status = True WHERE habit_id = :habit_id',
                  {'habit_id': habit_id})