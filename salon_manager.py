import json
from artist import Artist
from service import Manicure, Pedicure, AcrylicSet, PolygelTips
from appointment import Appointment

class SalonManager:
    def __init__(self):
        jenny_sched = {
            "Tuesday": ["09:00", "10:00", "11:00"],
            "Wednesday": ["09:00", "10:00", "11:00"]
        }
        
        lisa_sched = {
            "Thursday": ["13:00", "14:00", "15:00", "16:00"],
            "Friday": ["13:00", "14:00", "15:00"]
        }
        
        jessica_sched = {
            "Tuesday": ["14:00", "15:00", "16:00"],
            "Friday": ["09:00", "10:00", "11:00"]
        }

        self.artists = [
            Artist("Jenny", jenny_sched),
            Artist("Lisa", lisa_sched),
            Artist("Jessica", jessica_sched)
        ]
        
        self.appointments = []
        self.load_data()

    def display_menu(self):
        print("\n--- TipsByJ System ---")
        print("1. View Artists & Schedules")
        print("2. Book Appointment")
        print("3. View Bookings")
        print("4. Exit & Save")

    def show_artists(self):
        print("\n--- Artist Schedules ---")
        for i, artist in enumerate(self.artists):
            print(f"\n{i + 1}. {artist}")
            # Loop through the dictionary to show days/times
            schedule = artist.get_schedule()
            for day, times in schedule.items():
                print(f"   - {day}: {times}")

    def book_appointment(self):
        self.show_artists()
        try:
            a_choice = int(input("\nSelect Artist ID: ")) - 1
            if a_choice < 0 or a_choice >= len(self.artists):
                print("Invalid artist.")
                return
            artist = self.artists[a_choice]

            print(f"\n{artist} is available on: {artist.get_days_available()}")
            day = input("Enter Day (e.g. Tuesday): ").capitalize() # Capitalize fixes 'tuesday' input

            if day not in artist.get_days_available():
                print("Artist is not working on that day.")
                return
                
            available_times = artist.get_times_for_day(day)
            print(f"Available times: {available_times}")
            time = input("Enter Time: ")
            
            if artist.remove_slot(day, time):
                client = input("Client Name: ")
                
                print("\n1. Manicure ($45)\n2. Pedicure ($60)\n3. Acrylic Set ($85)\n4. Polygel Tips ($95)")
                s_choice = input("Select Service: ")
                
                if s_choice == "1": service = Manicure()
                elif s_choice == "2": service = Pedicure()
                elif s_choice == "3": service = AcrylicSet()
                elif s_choice == "4": service = PolygelTips()
                else: service = Manicure() # Default

                new_appt = Appointment(client, artist.name, service.name, day, time)
                self.appointments.append(new_appt)
                print(f"Success! Booked {service.name} on {day} at {time}.")
            else:
                print("Slot unavailable.")

        except ValueError:
            print("Invalid input.")

    def save_data(self):
        data = [appt.to_dict() for appt in self.appointments]
        with open('data.json', 'w') as f:
            json.dump(data, f)
        print("Saved.")

    def load_data(self):
        try:
            with open('data.json', 'r') as f:
                data = json.load(f)
                for x in data:
                    # Note: We now load 'day' as well
                    self.appointments.append(Appointment(x['client'], x['artist'], x['service'], x.get('day', 'Tuesday'), x['time']))
        except FileNotFoundError:
            self.appointments = []

    def run(self):
        while True:
            self.display_menu()
            choice = input("Choice: ")
            if choice == "1": self.show_artists()
            elif choice == "2": self.book_appointment()
            elif choice == "3":
                for a in self.appointments:
                    print(f"{a.client_name}: {a.service_name} with {a.artist_name} on {a.day} @ {a.time}")
            elif choice == "4":
                self.save_data()
                break
