todo-line
======
#### What is it?
+ A simple command line todo application written in Python for MacOS and Windows.

#### How to use?
+ __Create a todo list__
  - Command: `todo --new <todo_name>`
  - You can create as many todo lists as you want, but only a single list can be checked out at a time
    * By default, the first list created will be checked out

+ __Add item to list__
  - Command: `todo --add <todo_item_description>`
  - The item will be appended to the items in the currently checked out list

+ __List all todos/todo items__
  - Command: `todo --list item(s)`
    * Executing this command will list all of the items in the checked out todo list
  - Command `todo --list todo(s)`
    * Executing this command will list all todo lists
    * The checked out list will be suffixed with an `*` i.e. `Grocery List*`
