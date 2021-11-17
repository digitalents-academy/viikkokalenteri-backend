"""
database.py: Interface to interact with our database.
Author: Niklas Larsson
Date: November 8, 2021
"""

from pymongo import MongoClient
from sys import exit
from ruamel.yaml import YAML
from datetime import datetime
from secrets import token_hex
from getpass import getuser


ERROR: int = 1


class Calendar:
    """Class that we can use to get, add, edit and delete calendar entries."""
    def __init__(self, connection: str) -> None:
        self.CONNECTION: str = connection
        self.client: object = MongoClient(self.CONNECTION)
        self.database: object = self.client["viikkokalenteri"]
        self.days: object = self.database["days"]
        self.date: str = "datetime.now().strftime(\"%A %-d %B\")"
        self.time: str = "datetime.now().strftime(\"%H:%M:%S\")"

    def _check_if_today(self) -> bool:
        """
        Hepler function for add_entry() to check
        if document for the current day exists.
        """
        for today in self.days.find():
            return eval(self.date) in today.keys()

    def _update_today(self, entry: dict) -> None:
        """
        Helper function for updating today -document.

        Note that this ISN'T used for updating the
        entry itself -- this just adds a new one.

        entry.... The document to make the update to.
        """
        self.days.update_one({}, [entry])

    def _create_today(self) -> None:
        """
        Helper function for creating today -document.

        Note that this just creates a new document
        inside the database -- inside which the
        calendar entries will then go to.
        """
        self.days.insert_one({eval(self.date): {"entries": {}}})

    def _update_entry(self) -> None:
        """Helper function for updating calendar entry."""
        pass

    def add_entry(self, subject: str, owner: str, date: str, time: str,
                  location: str=None, info: str=None) -> None:
        """
        Add new calendar entry.

        subject..... Subject of the entry.
        owner....... Owner / creator of the entry.
        date........ The date of the entry event.
        time........ The time / duration etc. of the entry event.
        location.... Optional location about the entry / event.
        info........ Optional extra information about the entry.
        """
        today_exists: bool = self._check_if_today()

        # Calendar entry body.
        entry_body: dict = {}
        entry_body["subject"] = subject
        entry_body["owner"] = owner
        entry_body["event_date"] = date
        entry_body["event_time"] = time
        entry_body["event_location"] = location
        entry_body["date_created"] = eval(self.date)
        entry_body["time_created"] = eval(self.time)
        entry_body["description"] = info

        # Calendar entry.
        date_entry: dict = {
                "$set": {
                    eval(self.date): {
                        "entries": {
                            token_hex(20): entry_body
                            }
                        }
                    }
                }

        if today_exists:
            self._update_today(date_entry)
        else:
            self._create_today()
            self._update_today(date_entry)

    def edit_entry(self, subject: str, new_subject: str=None,
                   new_date: str=None, new_time: str=None,
                   new_location: str=None, new_desc: str=None) -> None:
        """
        Edit existing calendar entry.

        subject....... Subject that identifies the entry we want to edit.
        new_subject... Optional new subject name for the entry event.
        new_date...... Optional new date for the entry event.
        new_time...... Optional new time for the entry event.
        new_location.. Optional new location for the entry event.
        new_desc...... Optional new description for the entry event.
        """
        entry: dict = None
        entry_id: str = None
        target: str
        for day in self.days.find():
            for index, entries_object in enumerate(day.values()):
                if index == 0: continue
                for calendar_entries in entries_object.values():
                    for cal_entry_id, cal_entry_body in calendar_entries.items():
                        entry_id = cal_entry_id
                        entry = cal_entry_body
                        if cal_entry_body["subject"] == subject:
                            print(subject, "found.")
                            print(f"id for found entry: {entry_id}")
                            print(f"body for found entry: {entry}")
                            break

    def get_entry(self) -> None:
        """Get existing calendar entry."""
        pass

    def delete_entry(self) -> None:
        """Delete existing calendar entry."""
        pass

    def set_working_time(self) -> None:
        """Set day's working time."""
        pass

    def update_working_time(self) -> None:
        """Update day's working time."""
        pass


class ConnectionString:
    """Class to get the connection string."""
    def __init__(self) -> None:
        self.yaml: object = YAML()
        self.connection: str = None
        self._get_connection()

    def _get_connection(self) -> None:
        try:
            with open("connection.yaml", "r") as f:
                self.connection = self.yaml.load(f)["connection"]
        except FileNotFoundError:
            print("Did not find file 'connection.yaml'.")
            print("Create it first the following way and then try again:")
            print("    touch connection.yaml")
            print("    echo \"connection: <connection_string>\" > connection.yaml")
            exit(ERROR)
        except KeyError:
            print("No 'connection' field found in 'connection.yaml'.")
            print("Create it first the following way and then try again:")
            print("    echo \"connection: <connection_string>\" >> connection.yaml")
            exit(ERROR)


if __name__ == "__main__":
    connection: object = ConnectionString()
    calendar: object = Calendar(connection.connection)

    # Test data.
    owner: str = "Test The Tester"
    subject: str = "Test entry"
    info: str = "Btw, this is a test entry..."
    date: str = "November 12 2021"
    time: str = "13.00-14.00"

    # calendar.add_entry(subject, owner, date, time, info=info)
    calendar.edit_entry(subject)
