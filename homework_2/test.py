from datetime import datetime
from lib2to3.main import diff_texts


# from homework_2.homework_2 import how_far_birthday


def how_far_birthday(date):

    date = str(date)
    # date = str(date.split("-"))
    # date = date[0], date[1], date[2]
    print(date)
    # date = list(map(int, date.split("-")))
    # d1 = datetime(year=datetime.now().year, month=date[1], day=date[2])
    # difference = d1 - datetime.now()

    # return difference.days

how_far_birthday(1955-2-28)
#
# def get_birthdays_per_week(users:list) -> dict[str, list]:
#     days_in_week = {"Monday": [], "Tuesday": [], "Wednesday": [], "Thursday": [], "Friday": []}
#
#     for user in users:
#         day_in_week = user["birthday"]

        # d = day_in_week.split('-')
        # days_from_birthday = how_far_birthday(d)
        # print(day_in_week)
        # days_from_birthday = how_far_birthday(str(user["birthday"]))

# get_birthdays_per_week([
#     {"name": "Bill Gates", "birthday": datetime(1955, 10, 28).date()},
#     {"name": "Billy Herrington", "birthday": datetime(1969, 3, 2).date()},
#     {"name": "Sam Fingers", "birthday": datetime(1999, 2, 16).date()}
# ])