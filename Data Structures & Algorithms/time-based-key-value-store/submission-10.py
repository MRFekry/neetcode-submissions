class TimeMap:

    def __init__(self):
        self.items = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.items:
            self.items[key].append((value, timestamp))
        else:
            self.items[key] = [(value, timestamp)]

    def get(self, key: str, timestamp: int) -> str:
        value = ""
        if key in self.items:            
            for tpl in self.items[key]:
                if timestamp == tpl[1]:
                    return tpl[0]
                elif tpl[1] < timestamp:
                    value = tpl[0]
            return value
        return value