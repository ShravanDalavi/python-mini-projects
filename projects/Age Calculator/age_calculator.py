from datetime import datetime

def calculate_age(birthdate):
    today = datetime.today()
    # Calculate the difference in years
    years = today.year - birthdate.year
    # Adjust if the birthday has not occurred yet this year
    if (today.month, today.day) < (birthdate.month, birthdate.day):
        years -= 1

    # Calculate the difference in months
    months = (today.year - birthdate.year) * 12 + today.month - birthdate.month
    if today.day < birthdate.day:
        months -= 1

    # Calculate the difference in days
    days = (today - birthdate).days

    return years, months, days

def main():
    birthdate_input = input("Enter your birthdate (YYYY-MM-DD): ")
    birthdate = datetime.strptime(birthdate_input, "%Y-%m-%d")

    years, months, days = calculate_age(birthdate)

    print(f"Your age in years: {years}")
    print(f"Your age in months: {months}")
    print(f"Your age in days: {days}")

if __name__ == "__main__":
    main()
