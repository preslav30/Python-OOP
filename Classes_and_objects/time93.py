class Time:
    max_hours = 23
    max_minutes = 59
    max_seconds = 59

    def __init__(self, hours: int, minutes: int, seconds: int):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    def set_time(self, hours, minutes, seconds):
        if 0 <= hours <= Time.max_hours:
            self.hours = hours
        if 0 <= minutes <= Time.max_minutes:
            self.minutes = minutes
        if 0 <= seconds <= Time.max_seconds:
            self.seconds = seconds

    def get_time(self):
        return f"{self.hours:02d}:{self.minutes:02d}:{self.seconds:02d}"

    def next_second(self):
        if self.seconds + 1 == 60:
            self.seconds = 0
            self.minutes += 1
            if self.minutes == 60:
                self.minutes = 0
                self.hours += 1
                if self.hours == 24:
                    self.hours = 0
        else:
            self.seconds += 1

        return self.get_time()


time = Time(1, 20, 30)
print(time.next_second())
