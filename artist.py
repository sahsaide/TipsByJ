class Artist:
    def __init__(self, name, working_days, working_times):
        self.name = name
<<<<<<< HEAD
        self.__schedule = schedule
=======
        self.working_days = working_days
        self.working_times = working_times
>>>>>>> 39ef010 (Organize services into folder and update imports)

    def works_on(self, day):
        return day in self.working_days

<<<<<<< HEAD
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
=======
    def has_time(self, time):
        return time in self.working_times

>>>>>>> 39ef010 (Organize services into folder and update imports)
