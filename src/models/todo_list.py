import datetime

class TodoList:

    def __init__(self, title, is_active, items):
        self._title = title
        self._items = items
        self._is_active = is_active
        self._creation_date_time = str(datetime.datetime.now())
        self._modified_date_time = str(datetime.datetime.now())

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        self._title = value

    @property
    def items(self):
        return self._items

    @items.setter
    def items(self, value):
        self._items = value

    @property
    def is_active(self):
        return self._is_active

    @is_active.setter
    def is_active(self, value):
        self._is_active = value

    @property
    def creation_date_time(self):
        return self._creation_date_time

    @creation_date_time.setter
    def creation_date_time(self, value):
        self._creation_date_time = value

    @property
    def modified_date_time(self):
        return self._modified_date_time

    @modified_date_time.setter
    def modified_date_time(self, value):
        self._modified_date_time = value