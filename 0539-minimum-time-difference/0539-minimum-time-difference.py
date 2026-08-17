class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        def convertMinutes(timePoint: str) -> int:
            hours, minutes = timePoint.split(":")
            return int(hours) * 60 + int(minutes)

        timeMinutes = sorted([convertMinutes(p) for p in timePoints])
        minDiff = math.inf

        for i in range(1, len(timeMinutes)):
            minDiff = min(minDiff, timeMinutes[i]-timeMinutes[i-1])
        
        if len(timeMinutes) >= 2:
            lastDiff = 24*60 - (timeMinutes[-1]-timeMinutes[0])
            minDiff = min(minDiff, lastDiff)
        return minDiff

        