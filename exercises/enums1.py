
from enum import Enum
from datetime import date

class Weekday(Enum):
    MONDAY = 1
    TUESDAY = 2
    WEDNESDAY = 3
    THURSDAY = 4
    FRIDAY = 5
    SATURDAY = 6
    SUNDAY = 7
    #
    @classmethod
    def from_date(cls, date):
        return cls(date.isoweekday())

print(Weekday.from_date(date.today()) )

# def show_chores(chores, day):
#     for chore, days in chores.items():
#         if day in days:
#             print(chore)

# chores_for_ethan = {
#     'feed the cat': Weekday.MONDAY | Weekday.WEDNESDAY | Weekday.FRIDAY,
#     'do the dishes': Weekday.TUESDAY | Weekday.THURSDAY,
#     'answer SO questions': Weekday.SATURDAY,
#     }

#print(show_chores(chores_for_ethan, Weekday.SATURDAY))