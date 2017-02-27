class Clock:
    def __init__(self, hour=0, minutes=0):
        extra, self.minutes = divmod(minutes, 60)
        self.hour = (hour + extra) % 24

    def __str__(self):
        return "{clock.hour:02d}:{clock.minutes:02d}".format(clock=self)

    def __eq__(self, other):
        return self.hour == other.hour and self.minutes == other.minutes

    def add(self, minutes):
        extra, self.minutes = divmod(self.minutes + minutes, 60)
        self.hour = (self.hour + extra) % 24
        return self
