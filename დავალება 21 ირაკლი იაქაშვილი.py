import calendar
from datetime import datetime, timedelta


class ShiftCalculator:
    def __init__(self, start_date):
        self.start_date = start_date
        self.holidays = self.get_georgian_holidays()

    def get_georgian_holidays(self):
        holidays = {
            "New Year's Day": (1, 1),
            "Orthodox Christmas Day": (1, 7),
            "Epiphany": (1, 19),
            "Mothers Day": (3, 3),
            "International Women's Day": (3, 8),
            "9 national unity": (4, 9),
            "Orthodox Good Friday": (5, 3),
            "Orthodox big Saturday": (5, 4),
            "Orthodox Easter": (5, 5),
            "Orthodox Easter Monday": (5, 6),
            "St Andrias day": (5, 12),
            "Independence Day": (5, 26),
            "St. Mary's Day": (8, 28),
            "st george day": (11, 23),
            "Day of Svetitskhoveli Cathedral": (10, 14),

        }

        return holidays

    def calculate_shift_dates(self):
        shift_dates = []
        end_date = datetime(datetime.now().year, 12, 31)  # End date of the year

        while self.start_date <= end_date:
            # Add day shift
            shift_dates.append(self.start_date)
            # Add night shift
            night_shift_date = self.start_date + timedelta(days=1)
            shift_dates.append(night_shift_date)

            # Move to the next shift date
            self.start_date += timedelta(days=5)

        return shift_dates

    def print_calendar(self, shift_dates):
        # Convert shift dates to a set
        shift_dates_set = set(shift_dates)

        # Generate calendar using calendar module
        cal = calendar.TextCalendar(calendar.SUNDAY)
        for month in range(1, 13):
            print(calendar.month_name[month])  # Print month name
            print("Mo Tu We Th Fr Sa Su")
            month_days = cal.monthdayscalendar(datetime.now().year, month)
            for week in month_days:
                for day in week:
                    if day == 0:
                        print("  ", end=" ")  # Print empty space for days not in the month
                    else:
                        date = datetime(datetime.now().year, month, day)
                        
                        if self.is_holiday(date):
                            print(f"\033[91m{day:2}\033[0m", end=" ")  # Print holidays in red color
                        elif date in shift_dates_set:
                            print(f"\033[92m{day:2}\033[0m", end=" ")  # Print shift days in green color
                        else:
                            print(f"{day:2}", end=" ")  # Print normal days
                print()  # Move to the next line after each week
            print()  # Add an extra line between months

    def is_holiday(self, date):
        result = False
        for holiday, date_range in self.holidays.items():
            if date_range[0] == date.month and date.day == date_range[1]:
                result = True
                break

        return result


# Input the start date of the shift
input_date = input("Enter the shift start date (YYYY-MM-DD): ")
start_date = datetime.strptime(input_date, "%Y-%m-%d")

# Create an instance of ShiftCalculator
shift_calculator = ShiftCalculator(start_date)

# Calculate shift dates
shift_dates = shift_calculator.calculate_shift_dates()

# Print the calendar with shift days
shift_calculator.print_calendar(shift_dates)