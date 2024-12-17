class Solution:
    def dayOfYear(self, date: str) -> int:

        return datetime.date.fromisoformat(date).timetuple().tm_yday