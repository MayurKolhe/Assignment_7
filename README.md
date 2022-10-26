# Laboratory 7

## Laboratory Objectives
1. Explore and use various tools such as: GitHub, VirtualBox, Tuffix, Linux Terminal, and Atom.
1. Write a Python program using:
     1. datetime built-in module
1. Run and test a Python program.
## Program Instructions
1. Write a Python program that performs as a Tuffy Titan Flight Schedule which contains a list of flight schedule data.
1. Create a `flights` module to meet the following requirements:
     1. Create a file named `flights.py`.
          1. Define a class named `Flights`.  
               1. Define a member function named `__init__` to meet the following requirements:
                    1. Take a self object as a positional parameter.
                    1. Take a filename string as a positional parameter.
                    1. Set a member variable equal to the filename.
                    1. Set a member variable equal to an empty data list.
                    1. Open the filename and load the JSON decoded contents to the empty data list.
                    1. Cleanly manage the `FileNotFoundError` if the filename does not exist.
               1. Define a member function named `add_flight` to meet the following requirements:
                    1. Take a self object as a positional parameter.
                    1. Take a origin string as a positional parameter.
                    1. Take a destination string as a positional parameter.
                    1. Take a flight number string as a positional parameter.
                    1. Take a departure string (as HHMM) as a positional parameter.
                    1. Take a next day string (as Y or N) as a positional parameter.
                    1. Take a arrival string (as HHMM) as a positional parameter.
                    2. If either the departure or arrival string is not in the proper format return a False.
                    1. Append the data to the member variable data list.
                    1. Write the JSON encode contents of the member variable data list to the filename that was set to the member variable.
                    1. Return a True.
               1. Define a member function named `get_flights` to meet the following requirements:
                    1. Take a self object as a positional parameter.
                    1. Return a formatted list of flight schedule data. For each element in the list, reformat the data as follows:
                         1. origin -> (ex: 'LAX') string with no special format.
                         2. destination -> (ex: 'ORD') string with no special format.
                         3. flight number -> (ex: '123') string with no special format.
                         4. departure -> (ex: '2:35pm') string as hours:minutesam. no leading zero on the hours. leading zero on the minutes. am/pm lowercase.
                         5. arrival -> (ex: '+11:35am') string as [+]hours:minutesam. optional plus sign for flights arriving the next day. no leading zero on the hours. leading zero on the minutes. am/pm lowercase.
                         6. duration -> (ex: '2:02') hours:minutes. no leading zero on the hours. leading zero on the minutes.
1. Create a `main` driver program to meet the following requirements:
     1. Create a file named `main.py`.
     1. Import the `flights` module.
     2. Declare a variable to hold a list of flights creating an instance object of the `Flights` class.
     6. Implement a menu within a loop with following choices:
          1. Add fight
          2. Print flight schedule
          3. Set flight schedule filename
          9. Exit the program
     7. Prompt the user for the menu choice.
     8. The Add flight menu selection should prompt the user for the origin, destination, flight number, departure time (HHMM), arrival time (HHMM), and arrival the next day (Y/N). Then call the `add_flight` member function.
     8. The Print flight schedule menu selection should call the `get_flights` member function and print a report as formatted in the below input and output.
1. Run the program using the command below and repeat the steps above until you are satisfied your program output meets the above requirements.

    ```
    python3 main.py
    ```


1. Typical input and output for the program:
     ```
           *** TUFFY TITAN FLIGHT SCHEDULE MAIN MENU

     1. Add flight
     2. Print flight schedule
     3. Set flight schedule filename
     9. Exit the program

     Enter menu choice: 1

     Enter origin: LAX
     Enter destination: ORD
     Enter flight number: 545
     Enter departure time (HHMM): 1230
     Enter arrival time (HHMM): 1640
     Is arrival next day (Y/N): N

           *** TUFFY TITAN FLIGHT SCHEDULE MAIN MENU

     1. Add flight
     2. Print flight schedule
     3. Set flight schedule filename
     9. Exit the program

     Enter menu choice: 1

     Enter origin: ORD
     Enter destination: CLE
     Enter flight number: 409
     Enter departure time (HHMM): 1733
     Enter arrival time (HHMM): 1857
     Is arrival next day (Y/N): N

           *** TUFFY TITAN FLIGHT SCHEDULE MAIN MENU

     1. Add flight
     2. Print flight schedule
     3. Set flight schedule filename
     9. Exit the program

     Enter menu choice: 1

     Enter origin: CLE
     Enter destination: IAD
     Enter flight number: 83
     Enter departure time (HHMM): 1953
     Enter arrival time (HHMM): 2119
     Is arrival next day (Y/N): N

           *** TUFFY TITAN FLIGHT SCHEDULE MAIN MENU

     1. Add flight
     2. Print flight schedule
     3. Set flight schedule filename
     9. Exit the program

     Enter menu choice: 1

     Enter origin: IAD
     Enter destination: LHR
     Enter flight number: 1
     Enter departure time (HHMM): 2200
     Enter arrival time (HHMM): 0530
     Is arrival next day (Y/N): Y

           *** TUFFY TITAN FLIGHT SCHEDULE MAIN MENU

     1. Add flight
     2. Print flight schedule
     3. Set flight schedule filename
     9. Exit the program

     Enter menu choice: 1

     Enter origin: LHR
     Enter destination: LAX
     Enter flight number: 2222
     Enter departure time (HHMM): 2355
     Enter arrival time (HHMM): 2201
     Is arrival next day (Y/N): Y

           *** TUFFY TITAN FLIGHT SCHEDULE MAIN MENU

     1. Add flight
     2. Print flight schedule
     3. Set flight schedule filename
     9. Exit the program

     Enter menu choice: 2

     ================== FLIGHT SCHEDULE ==================
     Origin Destination Number Departure  Arrival Duration
     ====== =========== ====== ========= ======== ========
     LAX    ORD            545   12:30pm   4:40pm     4:10
     ORD    CLE            409    5:33pm   6:57pm     1:24
     CLE    IAD             83    7:53pm   9:19pm     1:26
     IAD    LHR              1   10:00pm  +5:30am     7:30
     LHR    LAX           2222   11:55pm +10:01pm    22:06

           *** TUFFY TITAN FLIGHT SCHEDULE MAIN MENU

     1. Add flight
     2. Print flight schedule
     3. Set flight schedule filename
     9. Exit the program

     Enter menu choice: 9
     ```

1. Run the unit testing program to ensure that your program runs as expected.

    ```
    python3 test.py
    ```
       
    The unit testing will output the results of a series of tests using specific input and expected output.  Any error will provide information on where the expected output is different from the actual output.  You will need to edit your source code to fix the error and run ` python3 test.sh` repeatedly until it passes all the test.

## Submission
Periodically throughout the exercise, and when you have completed the exercise, **submit the complete repository to Github**.

   <pre>git add .<br>git commit -m "<i>your comment</i>"<br>git push</pre>

In case it asks you  to configure global variables for an email and name, just copy the commands it provides then replace the dummy text with your email and Github token.

   <pre>git config --global user.email "<i>tuffy@csu.fullerton.edu</i>"<br>git config --global user.name "<i>Tuffy Titan</i>"<br>git commit -m "<i>your comment</i>"<br>git push</pre>

When you completed the final Github push, go back into github.com through the browser interface and ensure all your files have been correctly updated.  You should have the following files:
```
main.py
flights.py
test.txt
```
    
## Grading
1. All points add up to a total of 100 points possible as detailed below.  Partial credit will be given where applicable.

| Points | Description |
| --- | --- |
|50|initial git clone of this repository to your Tuffix machine|
|15|main.py file submitted contains the main driver program and meets the program requirements|
|15|flights.py file submitted contains the flights module and meets the program requirements|
|10|unit testing test.txt file results submitted|
|10|unit testing passes each test|
