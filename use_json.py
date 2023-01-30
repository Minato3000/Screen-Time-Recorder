import datetime
import json


class Json:
    def __init__(self, file_name):
        self.file_name = file_name

    def read_json(self):
        with open(self.file_name, 'r') as f:
            data = json.load(f)

        data = data['activities']
        return data

    def show_data(self):
        data = self.read_json()

        for activity in data:
            time_data = self.obtain_time(activity['time_entries'])
            print(activity['name'], "\n Time calculated ->", time_data)

    def convert_seconds(self, seconds):
        minutes = seconds // 60
        seconds = seconds % 60
        return minutes, seconds

    def convert_minutes(self, minutes):
        hours = minutes // 60
        minutes = minutes % 60
        return hours, minutes

    def convert_hours(self, hours):
        days = hours // 24
        hours = hours % 24
        return days, hours

    def obtain_time(self, time_entries):
        days = 0
        hours = 0
        minutes = 0
        seconds = 0
        for i in range(len(time_entries)):
            time_data = time_entries[i]

            days += time_data['days']
            hours += time_data['hours']
            minutes += time_data['minutes']
            seconds += time_data['seconds']

        extra_minutes, seconds = self.convert_seconds(seconds)
        minutes += extra_minutes

        extra_hours, minutes = self.convert_minutes(minutes)
        hours += extra_hours

        extra_days, hours = self.convert_hours(hours)
        days += extra_days

        return [days, hours, minutes, seconds]


our_json = Json('activities.json')
our_json.show_data()
