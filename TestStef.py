#!/usr/bin/env python
from Todo import Todo
from Item import Item

todo_de_test = Todo()

item1 = Item(todo_de_test)
item1.id = 1
item1.label = "Faire cuire du poulet"

item2 = Item(todo_de_test)
item2.label = "Aller voir Daim au cinéma"

for item in todo_de_test.items:
    print(item)
