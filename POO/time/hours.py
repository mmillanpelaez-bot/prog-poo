class Hours:
    def __init__(self, hours: int, minutes: int, seconds: int):
        self.set_hours(hours)
        self.set_minutes(minutes)
        self.set_seconds(seconds)

    def set_hours(self, hours: int) -> None:
        if 0 <= hours < 24:
            self._hours = hours
        else:
            raise ValueError("Enter a valid time format.")

    def get_hours(self) -> int:
        return self._hours

    def set_minutes(self, minutes: int) -> None:
        if 0 <= minutes < 60:
            self._minutes = minutes
        else:
            raise ValueError("Enter a valid time format.")

    def get_minutes(self) -> int:
        return self._minutes

    def set_seconds(self, seconds: int) -> None:
        if 0 <= seconds < 60:
            self._seconds = seconds
        else:
            raise ValueError("Enter a valid time format.")

    def get_seconds(self) -> int:
        return self._seconds

    def increase_hours(self):
        if self._hours == 23:
            self._hours = 0
        else:
            self._hours += 1

    def increase_minutes(self):
        if self._minutes == 23:
            self._minutes = 0
        else:
            self._minutes += 1

    def increase_seconds(self):
        if self._seconds == 23:
            self._seconds = 0
        else:
            self._seconds += 1

    def __str__(self):
        return f"{self._hours:02d}:{self._minutes:02d}:{self._seconds:02d}"