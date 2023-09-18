import datetime


class Habit:
    def __init__(
        self,
        position,
        habit_name,
        category,
        duration,
        date_created=None,
        last_date_checked=None,  # optional fields
        status=None,
        streak=0,
    ):  # optional fields
        self.position = position  # check if position argument exists
        self.habit_name = habit_name  # initialiize task
        self.category = category  # initialize category
        self.duration = duration  # weekly or daily
        self.date_created = (
            date_created if date_created is not None else datetime.date.today()
        )  # check if date_added argument exists, isoformat outputs string
        self.last_date_checked = (
            last_date_checked if last_date_checked is not None else None
        )  # check if date_completed argument exists
        self.streak = streak if streak != 0 else 0
        self.status = (
            status if status is not None else 1
        )  # 1 = open, 2 = completed , check if status argument exists

    def __repr__(self) -> str:
        return f"({self.position}, {self.habit_name}, {self.category}, {self.duration}, {self.date_created}, {self.last_date_checked}, {self.streak}, {self.status})"  # print everything in consolea

    def __getitem__(self, habit):
        return habit
