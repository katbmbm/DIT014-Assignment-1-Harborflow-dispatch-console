HARBORFLOW DISPATCH CONSOLE - TEAM README

Run instructions
----------------
Command: python harborflow_app.py
Python version tested: 3.14.7

Team members and concrete contributions
---------------------------------------
Name: Frida
Contribution: Defined the main(). Wrote the code for task 4 and 7. Contributed to the code for tasks 2, 3 and 5.

Name: Katherine
Contribution: Defined the main(). Wrote the code for tasks 2, 5 and 8. Contributed to the code for tasks 3 and 4. 

Name: Kevi
Contribution: Wrote the code for tasks 3, 6, and 9. Contributed to the code for tasks 4 and 5. 


Design notes
------------
Main function boundaries: The main function drives the program through a menu-based loop. On each iteration, it displays the main menu and prompts the user to select an option. Based on the user's choice, main calls the corresponding function to carry out the requested action. This cycle repeats until the user selects the exit option, at which point the loop ends and the program terminates.
How input validation is organized: We first read the inputs and if they're invalid, the program runs a while loop to repeatedly ask for information until it's valid.
How shared calculations are reused: Reused some split, strip and conversion calculations from task 4 to task 5

Known limitations
-----------------
In some tasks, the program may report an error if the user inputs a string instead of a float or int.
