class TimeMap:

    def __init__(self):
        self.mapping = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.mapping:
            self.mapping[key] = []
        self.mapping[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        search_list = self.mapping.get(key, [])
        if not search_list: return ""

        pos = bisect.bisect_right(search_list, timestamp, key=lambda x: x[0])
        if pos == 0: return "" # if no earlier timestamp than query timestamp
        return search_list[pos-1][-1]
