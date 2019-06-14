from Todo import Todo
from Item import Item

todo_de_test = Todo()

item1 = Item(todo_de_test)
item1.id = 1
item1.label = "Je suis l'item 1"

item2 = Item(todo_de_test)
item2.label = "Je suis l'item 2"

for item in todo_de_test.items:
    print(item)
