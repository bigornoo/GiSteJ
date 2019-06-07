class Item:

    # Attributes
    id = 0
    label = ""
    description = ""
    priority = 0
    state = 0
    date_expected = None
    date_delivery = None
    date_creation = None
    date_modification = None
    __todo = None

    # Constructor
    def __init__(self, todo):
        self.todo = todo
        todo.items.append(self)
