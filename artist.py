class Artist:
    def __init__(self, name, schedule):
        self.name = name
        self.__schedule = schedule

    def get_schedule(self):
        return self.__schedule

    def get_days_available(self):
        return list(self.__schedule.keys())

    def get_times_for_day(self, day):
        if day in self.__schedule:
            return self.__schedule[day]
        return []

    def remove_slot(self, day, time):
        if day in self.__schedule and time in self.__schedule[day]:
            self.__schedule[day].remove(time)
            
            # Clean up: If no times left for that day, remove the day key
            if not self.__schedule[day]:
                del self.__schedule[day]
            return True
        return False
    
    def __str__(self):
        return self.name
