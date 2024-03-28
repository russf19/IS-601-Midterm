# Russell Fong IS601 Spring 2024 Midterm Readme Document

This is my midterm project for IS601. This calculator is a continuation of the previous calculator assignments. In this version of the project, I have edited the history.py script so it now employs Pandas to read from and write to CSV files. Pandas are also used to manage calculation history and use data columns to sort data into a table. The calculator is a fully functional calculator that can perform basic arithmetic, stores history, gets history, deletes history, imports history from a csv file, and exports history from a csv file. The calculator also displays a menu upon booting the app up.

## Design Patterns
### Command Design Pattern
My operation.py utilizes the Command design pattern. All commands in my calculator utilize the Command class. All the commands declare an execute method as shown below. The classes in operation.py are all examples of concrete commands.

![image](https://github.com/russf19/IS-601-Midterm/assets/83291984/ad3ce0a3-cf91-459c-bb3d-9237213e8c56)

Link to code: https://github.com/russf19/IS-601-Midterm/blob/master/app/plugins/operation/operation.py 

### Factory Design Pattern
My main.py uses the factory method design pattern in the CalculatorApp class. load_commands loads plugins from directories and creates instances of their classes without specifying their concrete class. Example from main.py is shown below.

![image](https://github.com/russf19/IS-601-Midterm/assets/83291984/d75ed48d-0944-4121-9580-16495b63a6b9)

Link to code: https://github.com/russf19/IS-601-Midterm/blob/master/main.py

### Facade Design Pattern
My csv_history.py utilizes the façade design pattern. CSVHistoryCommands acts as the façade class and creates an easy to use interface for users. export_to_csv and import_from_csv act as the subsystems that handle the more complicated operations such as writing the data to the specified csv file or importing data from a csv file.

![image](https://github.com/russf19/IS-601-Midterm/assets/83291984/cfc7bba4-d8d1-43f2-b78c-9b796edbd67f)

Link to code: https://github.com/russf19/IS-601-Midterm/blob/master/app/plugins/csv_history/csv_history.py

## Environmental Variables
Environmental Variables are used in my main.py. Environmental variables are loaded from the .env file. Environmental variables are also used in the configure_logging method. logging_conf_path is an environmental variable and is used to determine the path to the logging config file.

![image](https://github.com/russf19/IS-601-Midterm/assets/83291984/ec74545e-b510-4707-8b76-df40f0046c20)

![image](https://github.com/russf19/IS-601-Midterm/assets/83291984/3505f548-a58a-4e25-a106-8d8b703ea38b)

Link to code: https://github.com/russf19/IS-601-Midterm/blob/master/main.py

## Logging
Logging is used in main.py to greet users when they first start up the calculator. I use logging to greet users with an informative message using logging.info letting them know how the calculator works and how to exit. Logging is also used as a warning and sends them an error message if they input an invalid command. Examples are shown below.  

![image](https://github.com/russf19/IS-601-Midterm/assets/83291984/acb41c0f-7847-4739-a8ca-e46a25698476)

![image](https://github.com/russf19/IS-601-Midterm/assets/83291984/b7afa094-058d-4fb0-bf14-5ee96eb37172)

Link to code: https://github.com/russf19/IS-601-Midterm/blob/master/main.py

## EAFP
The code below from my main.py illustrates EAFP through the try and except blocks. Try executes the command without checking for errors and if an error occurs, an exception is raised as shown in except block. The code will execute the command, however, If a user does not type in a valid command, an exception is raised and an error message is printed out.

![image](https://github.com/russf19/IS-601-Midterm/assets/83291984/743f7425-efa4-4c2d-ab75-44186371ee0d)

Link to code: https://github.com/russf19/IS-601-Midterm/blob/master/main.py

## LBYL
The code below from my main.py illustrates LBYL as it first checks to see if the logging configuration file exists before it attempts to load it. If the config file exists, it loads the logging configuration from the fille, If it does not exist, it will default to a basic logging configuration.

![image](https://github.com/russf19/IS-601-Midterm/assets/83291984/88d6cc48-f4e1-4e62-aae5-d3e3da69da22)

Link to code: https://github.com/russf19/IS-601-Midterm/blob/master/main.py
