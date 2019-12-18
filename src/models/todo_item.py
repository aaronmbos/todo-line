import datetime
import item_status

class TodoItem:

    def __init__(self, description):
        self._description = description
        self._date_added = datetime.datetime.now
        self._status = item_status.INCOMPLETE

    @property
    def description(self):
        return self._description

    @description.setter
    def description(self, value):
        self._description = value

    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value

    @property
    def date_added(self):
        return self._date_added

    @date_added.setter
    def date_added(self, value):
        self._date_added = value
    # Date Completed
    @property
    def date_completed(self):
        return self._date_completed

    @date_completed.setter
    def date_completed(self, value):
        self._date_completed = value

        