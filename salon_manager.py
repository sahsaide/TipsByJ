import json
import os

from appointment import Appointment
from artist import Artist

from services.manicure import Manicure
from services.pedicure import Pedicure
from services.acrylic import AcrylicSet
from services.polygel import PolygelTips

DATA_FILE = "data.json"


class SalonManager:
    def __init__(self):
        self.artists = self.create_artists()
        self.services = self.create_services()
        self.appointments = []
        self.load_data()

    def create_artists(self):
        return [
            Artist("Jade", ["Mon", "Wed", "Fri"], ["10:00", "12:00", "14:00"]),
            Artist("Mila", ["Tue", "Thu", "Sat"], ["11:00", "13:00", "15:00"])
        ]

    def create_services(self):
        return [Manicure(), Pedicure(), AcrylicSet(), PolygelTips()]

    def load_data(self):
        if os.path.exists(DATA_FILE):
            with open(DATA_FILE, "r") as f:
                self.appointments = [Appointment.from_dict(a) for a in json.load(f)]

    def save_data(self):
        with open(DATA_FILE, "w") as f:
            json.dump([a.to_dict() for a in self.appointments], f, indent=2)

    def show_artists(self):
        for i, a in enumerate(self.artists, 1):
            print(f"{i}. {a.name} | Days: {a.working_days} | Times: {a.working_times}")

    def show_services(self):
        for i, s in enumerate(self.services, 1):
            print(f"{i}. {s.get_details()}")

    def show_appointments(self):
        if not self.appointments:
            print("No appointments saved.")
            return
        for a in self.appointments:
            print(a)

    def book(self):
        name = input("Client name: ")

        self.show_artists()
        artist = self.artists[int(input("Choose artist: ")) - 1]

        day = input("Choose day: ")
        if not artist.works_on(day):
            print("Artist not available.")
            return

        time = input("Choose time: ")
        if not artist.has_time(time):
            print("Time not available.")
            return

        for a in self.appointments:
            if a.artist == artist.name and a.day == day and a.time == time:
                print("Slot already booked.")
                return

        self.show_services()
        service = self.services[int(input("Choose service: ")) - 1]

        self.appointments.append(
            Appointment(name, artist.name, service.name, day, time, service.price)
        )
        print("Appointment booked.")

    def run(self):
        while True:
            print("\n1. View artists")
            print("2. View services")
            print("3. Book appointment")
            print("4. View appointments")
            print("5. Save & exit")

            choice = input("Choose option: ")

            if choice == "1":
                self.show_artists()
            elif choice == "2":
                self.show_services()
            elif choice == "3":
                self.book()
            elif choice == "4":
                self.show_appointments()
            elif choice == "5":
                self.save_data()
                print("Saved. Goodbye.")
                break
