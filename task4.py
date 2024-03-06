from datetime import datetime, timedelta

users = [
    {"name": "John Doe", "birthday": "1985.09.23"},
    {"name": "Jane Smith", "birthday": "1990.03.08"},
    {"name": "Peter Parker", "birthday": "1991.01.23"},
    {"name": "Lois Lane", "birthday": "1991.03.09"}
]

def get_upcoming_birthdays(users):
    upcoming_birthdays = []
    today = datetime.today().date()
    days = 7

    for user in users:
        birthday_this_year = datetime.strptime(user["birthday"], "%Y.%m.%d").date()\
            .replace(year = today.year)
        if birthday_this_year < today:
            birthday_this_year = birthday_this_year.replace(year = today.year + 1)
        if 0 <= (birthday_this_year - today).days <= days:
            if birthday_this_year.weekday() >= 5:
                birthday_this_year = birthday_this_year + timedelta(days = 1) \
                    if birthday_this_year.weekday() == 6 \
                    else birthday_this_year + timedelta(days = 2)
            upcoming_birthdays.append({
                "name": user["name"], 
                "congratulation_date": birthday_this_year.strftime("%Y.%m.%d")
            })
    return upcoming_birthdays
            
print(get_upcoming_birthdays(users))