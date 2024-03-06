from re import sub

raw_numbers = [
    "067\\t123 4567",
    "(095) 234-5678\\n",
    "+380 44 123 4567",
    "380501234567",
    "    +38(050)123-32-34",
    "     0503451234",
    "(050)8889900",
    "38050-111-22-22   ",
    "38050 111 22 11",
]

def normalize_phone(phone_number):
    pattern = r"\D+"
    replacement = ""
    phone_number = sub(pattern, replacement, phone_number)
    phone_number = '+' + phone_number if phone_number.startswith('38') \
        else '+38' + phone_number
    return phone_number

normalized_numbers = [normalize_phone(num) for num in raw_numbers]

print(normalized_numbers)