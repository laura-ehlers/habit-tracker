import datetime

class Habit:
    def __init__(self, habit_name, category, duration,
                 time_created=None, date_completed=None, #optional fields
                 status=None, position=None): #optional fields
        self.habit_name = habit_name #initialiize task
        self.category = category #initialize category
        self.duration = duration
        self.time_created = time_created if time_created is not None else datetime.datetime.now().isoformat() #check if date_added argument exists, isoformat outputs string
        self.date_completed = date_completed if date_completed is not None else None #check if date_completed argument exists
        self.status = status if status is not None else 1 #1 = open, 2 = completed , check if status argument exists
        self.position = position if position is not None else None #check if position argument exists

    def __repr__(self) -> str:
        return f"({self.habit_name}, {self.category}, {self.duration} {self.time_created}, {self.date_completed}, {self.status}, {self.position})" #print everything in console