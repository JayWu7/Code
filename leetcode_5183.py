class Solution:
    def dayOfTheWeek(self, day: int, month: int, year: int) -> str:
        start_weekday = 5  # 1.1.1971 is a friday
        start_year = 1971
        dates = {1: "Monday", 2: "Tuesday", 3: "Wednesday", 4: "Thursday", 5: "Friday", 6: "Saturday", 0: "Sunday"}
        months = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}

        leaps = (year - start_year - 2) // 4 + 1
        year_days = 365 * (year - start_year) + leaps
        if month == 1:
            days = year_days + day
        elif month == 2:
            days = year_days + months[1] + day
        else:
            days = year_days + months[1] + months[2] + day
            for i in range(3, month):
                days += months[i]

            if (year - 1972) % 4 == 0:
                days += 1

        return dates[((start_weekday + days - 1) % 7)]  # minus 1 means reduce the one of day.
