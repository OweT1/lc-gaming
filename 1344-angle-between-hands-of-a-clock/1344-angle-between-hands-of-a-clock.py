class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        hour_ind = hour % 12 + minutes / 60
        minutes_ind = minutes / 5
        diff = abs(hour_ind - minutes_ind)
        return min(12 - diff, diff) / 12 * 360