from datetime import datetime


class Todo:

    # Attributes
    id = 0
    label = ""
    description = ""
    __date_creation = None
    __date_modification = None
    __items = []

    # Methods
    def add_item(self, item):
        self.__items.append(item)

    def before_save(self):
        now = datetime.now()

        if self.__date_creation is None:
            # Creation
            self.__date_creation = now
        else:
            # Modification
            self.__date_modification = now
