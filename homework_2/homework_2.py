from datetime import datetime, date


def get_birthdays_per_week(users:list):
    days_in_week = {"Monday": [], "Tuesday": [], "Wednesday": [], "Thursday": [], "Friday": []}

    today = date.today()

    for user in users:
        name = user["name"].split(" ")[0]
        birthday = user["birthday"]

        birthday_this_year = birthday.replace(year=today.year)

        if birthday_this_year < today:
            birthday_this_year = birthday_this_year.replace(year=today.year + 1)

        delta_days = (birthday_this_year - today).days

        if delta_days < 7:
            day_of_week = birthday_this_year.strftime("%A")

            if day_of_week in ["Saturday", "Sunday"]:
                day_of_week = "Monday"

            if day_of_week in days_in_week:
                days_in_week[day_of_week].append(name)

    filtered_data = {k: v for k, v in days_in_week.items() if v}


    return filtered_data



get_birthdays_per_week([
    {"name": "Bill Gates", "birthday": datetime(1955, 10, 28).date()},
    {"name": "Billy Herrington", "birthday": datetime(1969, 3, 2).date()},
    {"name": "Sam Fingers", "birthday": datetime(1999, 2, 16).date()}
])