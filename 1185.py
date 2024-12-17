class Solution:
    def dayOfTheWeek(self, day: int, month: int, year: int) -> str:
        
        def fn(y, m, d): 
            """Return year-month-day in number format."""
            if m < 3: 
                y -= 1
                m += 12
            return 365*y + y//4 - y//100 + y//400 + (153*m + 8)//5 + d
        
        weekday = ("Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday")
        return weekday[(fn(year, month, day) - fn(2021, 4, 11)) % 7]