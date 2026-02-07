class Appointment:
    def __init__(self, client_name, artist, service, day, time, price):
        self.client_name = client_name
        self.artist = artist
        self.service = service
        self.day = day
        self.time = time
        self.price = price

    def to_dict(self):
        return {
            "client_name": self.client_name,
            "artist": self.artist,
            "service": self.service,
            "day": self.day,
            "time": self.time,
            "price": self.price
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            data["client_name"],
            data["artist"],
            data["service"],
            data["day"],
            data["time"],
            data["price"]
        )

    def __str__(self):
        return f"{self.client_name} | {self.artist} | {self.service} | {self.day} {self.time} | ${self.price}"
