class Appointment:
    def __init__(self, client_name, artist_name, service_name, day, time):
        self.client_name = client_name
        self.artist_name = artist_name
        self.service_name = service_name
        self.day = day  
        self.time = time

    def to_dict(self):
        return {
            "client": self.client_name,
            "artist": self.artist_name,
            "service": self.service_name,
            "day": self.day,
            "time": self.time
        }