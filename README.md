Project Name: AirBnB clone - The console
Description:
 *How to create a Python package
 *How to create a command interpreter in Python using the cmd module
 *What is Unit testing and how to implement it in a large project
 *How to serialize and deserialize a Class
 *How to write and read a JSON file
 *How to manage datetime
 *What is an UUID
 *What is *args and how to use it
 *What is **kwargs and how to use it
 *How to handle named arguments in a function

Command Interpreter
The command interpreter is a crucial part of your project. It allows users to interact with your application via the command line. Here’s how to get started:

Installation:
Clone this repository to your local machine.
Navigate to the project directory.
Running the Command Interpreter:
Open a terminal or command prompt.
Execute the interpreter script (e.g., my_interpreter.py).
Usage:
The interpreter will display a prompt where you can enter commands.
Type commands and press Enter to execute them.
Examples of commands:
help: Display available commands and their descriptions.
create <object>: Create an object (e.g., create a user, a file, etc.).
show <object_id>: Display details of a specific object.
…
Examples:
Here are some usage examples:
$ ./my_interpreter.py
(my_interpreter) help
Available commands:
  - create <object>
  - show <object_id>
  - ...
(my_interpreter) create user Vicent
User 'Vicent' created successfully.
(my_interpreter) show user 123
User ID: 123
Name: Vicent
