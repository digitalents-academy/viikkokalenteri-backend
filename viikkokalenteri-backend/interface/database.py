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

        # Create body for calendar entry.
        self.entry_body: dict = {}
        self.entry_body["subject"] = subject
        self.entry_body["owner"] = owner
        self.entry_body["date"] = date
        self.entry_body["time"] = time
        self.entry_body["location"] = location
        self.entry_body["info"] = info

        # Create entry inside today's document.
        self.date_entry: dict = {
                "$set": {
                    eval(self.date): {
                        "entries": {
                            token_hex(20): self.entry_body
                            }
                        }
                    }
                }

        if self.today_exists:
            self.days.update_one({}, [self.date_entry])
        else:
            self.days.insert_one({eval(self.date): {"entries": {}}})
            self.days.update_one({}, [self.date_entry])

    def edit_entry(self, subject: str) -> None:
        """
        Edit existing calendar entry.

        subject..... Subject that identifies the entry we want to edit.
        """
        entries: dict
        entry: dict
        entry_id: str
        for day in self.days.find():
            for index, entries_object in enumerate(day.values()):
                if index == 0: continue
                for calendar_entries in entries_object.values():
                    for entry_id, entry_body in calendar_entries.items():
                        for field in entry_body:
                            if field["subject"] == subject:
                                print(subject, "found.")
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

    # calendar.add_entry(subject, owner, info=info)
    calendar.edit_entry(subject)
