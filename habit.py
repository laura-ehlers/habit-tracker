from datetime import datetime
from nanoid import generate

class Habit:
     # id is uniquely created
    def __init__(self, habit_id, habit_name=None, period=None, status=None, streak=None, start_date=None, end_date=None):
        self.habit_id =  generate('1234567890abcdefghijklmnopqrstuvwxyz', 5)
        self.habit_name = habit_name
        self.period = period
        self.status = status if status is not None else False
        self.streak = streak if streak is not None else 0
        self.start_date = start_date if start_date is not None else datetime.today().strftime('%d-%m-%Y')
        self.end_date = end_date if end_date is not None else datetime.now().isoformat()
    
    def __describe__(self) -> str:
        return f'({self.habit_name}, {self.period}, {self.status}, {self.streak}, {self.start_date}, {self.end_date}, {self.habit_id})'