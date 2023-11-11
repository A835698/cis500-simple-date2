#######################################################
# LDate
#
# A simple date class for *L*earning to write classes
#
# Name: Avinash 
# Section: 03
#
# Fall 2023
#########################################################

class LDate:
    # Leap year check
    @staticmethod
    def is_leap_year(year: int) -> bool:
        if year % 4 == 0:
            if year % 100 == 0:
                if year % 400 == 0:
                    return True
                else:
                    return False
            else:
                return True
        else:
            return False

    # Days in month
    @staticmethod
    def days_in_month(year: int, month: int) -> int:
        if month in {4, 6, 9, 11}:
            return 30
        elif month == 2:
            return 29 if LDate.is_leap_year(year) else 28
        else:
            return 31

    # Check if valid date
    @staticmethod
    def is_valid_date(year: int, month: int, day: int) -> bool:
        if month < 1 or month > 12:
            return False
        if day < 1 or day > LDate.days_in_month(year, month):
            return False
        return True

    # Initialization
    def __init__(self, year: int, month: int, day: int):
        if not LDate.is_valid_date(year, month, day):
            raise ValueError("Invalid date")
        self.year = year
        self.month = month
        self.day = day

    # Ordinal date
    def ordinal_date(self) -> int:
        days = self.day
        for m in range(1, self.month):
            days += LDate.days_in_month(self.year, m)
        return days

    # Comparisons
    def __eq__(self, other) -> bool:
        return isinstance(other, LDate) and self.year == other.year and self.month == other.month and self.day == other.day

    def __lt__(self, other) -> bool:
        if not isinstance(other, LDate):
            raise ValueError("Comparison with non-LDate object")
        return (self.year, self.month, self.day) < (other.year, other.month, other.day)

    def __le__(self, other) -> bool:
        return self.__lt__(other) or self.__eq__(other)


    def days_since(self, other) -> bool:
        if self > other:
            earlier_date = other
            later_date = self
        else:
            earlier_date = self
            later_date = other

       
        ordinal_date_earlier = earlier_date.ordinal_date()
        ordinal_date_later = later_date.ordinal_date()

        number_of_days = (ordinal_date_later - ordinal_date_earlier) + (365 * (later_date.year - earlier_date.year))

      
        number_of_leap_days = 0
        for year in range(earlier_date.year, later_date.year):
            if LDate.is_leap_year(year):
                number_of_leap_days += 1

        return number_of_days + number_of_leap_days

  
    def day_of_week(self) -> str:
        reference_year = 1753
        reference_month = 1
        reference_day = 1

        days_difference = self.days_since(LDate(reference_year, reference_month, reference_day))


        day_of_week_index = days_difference % 7
        days_of_week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
        day_of_week_name = days_of_week[day_of_week_index]

        return day_of_week_name

    def __str__(self) -> str:
        day_of_week_name = self.day_of_week()
        ordinal_day = self.day
        month_names = [
            '', 'January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October',
            'November', 'December']
        month_name = month_names[self.month]

        return f"{day_of_week_name}, {ordinal_day:02d} {month_name} {self.year}"

 
    def __add__(self, days: int):
        new_date = LDate(self.year, self.month, self.day)
        new_ordinal = new_date.ordinal_date() + days
        new_date = LDate(self.year, 1, 1)  # reset to the start of the year
        while new_ordinal > new_date.ordinal_date():
            new_ordinal -= LDate.days_in_month(self.year, new_date.month)
            new_date.month += 1
        new_date.month -= 1  # step back into the correct month
        new_date.day = new_ordinal
        return new_date



if __name__ == '__main__':
    d1 = LDate(1941, 12, 7)
    d2 = LDate(2023, 11, 1)
    print(d1)
    print(d2)
    print(d2.days_since(d1))
    print(d2 + 10)  # Adds 10 days to d2