class Time:
    """
    A class to represent a specific time of day (24-hour format).
    It handles arithmetic, comparison, and overflow logic automatically.
    """

    def __init__(self, hour: int = 0, minute: int = 0, second: int = 0):
        """
        Initialize the Time object.
        Inputs are normalized (e.g., 65 seconds becomes 1 minute, 5 seconds).
        """
        # Calculate total seconds to handle overflow logic easily
        total_seconds = hour * 3600 + minute * 60 + second

        # Modulo 86400 (24 * 3600) ensures the time wraps around 24 hours
        self.total_seconds = total_seconds % 86400

        # Derive canonical H, M, S
        self.hour, self.minute, self.second = self._seconds_to_hms(self.total_seconds)

    @staticmethod
    def _seconds_to_hms(seconds: int):
        """Helper to convert total seconds back to (H, M, S)."""
        m, s = divmod(seconds, 60)
        h, m = divmod(m, 60)
        return h, m, s

    def __str__(self):
        """String representation: HH:MM:SS"""
        return f"{self.hour:02d}:{self.minute:02d}:{self.second:02d}"

    def __repr__(self):
        """Official representation for debugging"""
        return f"Time(hour={self.hour}, minute={self.minute}, second={self.second})"

    # --- Arithmetic Operations ---

    def __add__(self, other):
        """
        Add time. Supports adding another Time object or an integer (seconds).
        Example: t1 + t2  OR  t1 + 300 (adds 5 minutes)
        """
        if isinstance(other, Time):
            return Time(second=self.total_seconds + other.total_seconds)
        elif isinstance(other, int):
            return Time(second=self.total_seconds + other)
        else:
            raise TypeError("Operand must be Time or int (seconds)")

    def __sub__(self, other):
        """
        Subtract time. Returns a new Time object representing the difference.
        """
        if isinstance(other, Time):
            return Time(second=self.total_seconds - other.total_seconds)
        elif isinstance(other, int):
            return Time(second=self.total_seconds - other)
        else:
            raise TypeError("Operand must be Time or int (seconds)")

    # --- Comparison Operations ---

    def __eq__(self, other):
        if not isinstance(other, Time):
            return NotImplemented
        return self.total_seconds == other.total_seconds

    def __lt__(self, other):
        if not isinstance(other, Time):
            return NotImplemented
        return self.total_seconds < other.total_seconds

    def __le__(self, other):
        if not isinstance(other, Time):
            return NotImplemented
        return self.total_seconds <= other.total_seconds

    # --- Utility ---

    def to_12_hour_format(self):
        """Returns a string in 12-hour format with AM/PM."""
        suffix = "AM" if self.hour < 12 else "PM"
        display_hour = self.hour % 12
        if display_hour == 0:
            display_hour = 12
        return f"{display_hour:02d}:{self.minute:02d}:{self.second:02d} {suffix}"


# --- Example Usage ---
if __name__ == "__main__":
    # 1. Creation and Normalization
    t1 = Time(23, 59, 59)
    print(f"Start Time: {t1}")

    # 2. Arithmetic (Adding 2 seconds causing a rollover to next day)
    t2 = t1 + 2
    print(f"Added 2 seconds: {t2}")  # Should be 00:00:01

    # 3. Arithmetic (Subtracting time)
    t3 = Time(10, 30, 0)
    t4 = Time(1, 15, 0)
    print(f"Subtraction ({t3} - {t4}): {t3 - t4}")

    # 4. Comparisons
    print(f"Is {t3} > {t4}? {t3 > t4}")

    # 5. Handling overflow in initialization (e.g., 90 minutes)
    weird_time = Time(hour=1, minute=90)
    print(f"Normalized 1:90 to: {weird_time}")  # Should be 02:30:00

    # 6. 12-hour format
    pm_time = Time(14, 45, 0)
    print(f"12-hour format of {pm_time}: {pm_time.to_12_hour_format()}")