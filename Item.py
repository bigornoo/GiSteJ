from datetime import datetime


class Item:

    # Attributes
    id = 0
    label = ""
    description = ""
    priority = 0
    state = 0
    date_expected = None
    date_delivery = None
    __date_creation = None
    __date_modification = None
    __todo = None

    # Constructor
    def __init__(self, todo):
        self.todo = todo
        todo.add_item(self)

    # Methods
    def before_save(self):
        now = datetime.now()

        if self.__date_creation is None:
            # Creation
            self.__date_creation = now
        else:
            # Modification
            self.__date_modification = now

