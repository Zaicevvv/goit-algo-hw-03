from datetime import datetime

def get_days_from_today(date):
    try:
        date = datetime.strptime(date, "%Y-%m-%d")
    except ValueError:
        print(f"Date '{date}' does not match format " \
              "YYYY-MM-DD")
    else:
        return (date.date() - datetime.today().date()).days

print(get_days_from_today('2025-03-06'))
