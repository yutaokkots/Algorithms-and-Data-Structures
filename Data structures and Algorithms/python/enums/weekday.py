from datetime import date
from enum import Enum

class Weekday(Enum):
    MONDAY = 1
    TUESDAY = 2
    WEDNESDAY = 3
    THURSDAY = 4
    FRIDAY = 5
    SATURDAY = 6
    SUNDAY = 7
    @classmethod
    def today(cls):
        print(f"Today is {cls(date.today().isoweekday()).name}")

d = dir(Weekday.SATURDAY)
print(d)
## ['FRIDAY', 'MONDAY', 'SATURDAY', 'SUNDAY', 'THURSDAY', 'TUESDAY', 'WEDNESDAY', '__class__', '__doc__', '__eq__', '__hash__', '__module__', 'name', 'today', 'value']

Weekday.today()
