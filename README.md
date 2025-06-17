# hangman-inculcated-revision-game

My project is a revision game that uses the format of hangman. It is divided into three subjects: Physics, Chemistry, and English. After logging in as a player by inputting a username, the player can choose to answer questions from any subject. The basic functioning of the game is that of hangman, where for every wrong answer, the stick figure develops. For every correct answer, the blank spaces get filled. After getting the correct answer, or after 8 wrong inputs, the end screen is displayed. For every correct answer, a point is added in the user’s record.

Besides the player login, there is also the option of logging in as admin to edit the set of questions or to view the files. To add or delete records, the values are entered in IDLE by the admin. To delete, the serial number of the question is inputted. For CSV files, the view option shows the excel sheet format, and for the binary file, it displays in IDLE. 

There is an existing leaderboard named LEADERBOARD that uses SQL connectivity with Python to correct the data of the scores of the players logged in and display the high scoring members. When the player enters the username to log in, it is stored in a variable. There is a list that stores the scores of the player for each game. Once the Quit button is clicked, the data from the list gets stored in the database along with the username of the player and their total score. When Show Leaderboard button is clicked, the database is displayed in IDLE with descending order of total score.

Packages imported-

-> tkinter: Used for the configuration and structure of the game i.e. formats how the game is displayed.

-> csv: Used to work with csv files.

-> pickle: Used to work with binary files.

-> os: Used to remove and rename binary file, as well as view the csv files in Excel format.

-> tabulate: Used to display the leaderboard in grid format.

-> random: Used to select questions from the data files randomly.

-> mysql.connector: Used to connect SQL with Python.

Functions used in Python-

Main program-
1) Next()- proceed ahead.
2) Back()- switch to the previous window.
3) Quit()- exit the game and update changes in the leaderboard.
4) Show()- display the leaderboard in IDLE.
5) Login()- enter a username to store scores.

Player module-
1) Phy(), Chem(), and Eng()- The functions to start the game for the respective subjects; creates a new window and frame.

Contains-
	
a) Phy_play(), chem_play(), eng_game()- Opens the data file and extracts the data to display question and store answer in a variable.
	
b) Phy_yes(), chem_yes(), eng_yes()- Stores the answer that the player enters and if correct, enters the correct letter in the allocated blank space.
	
c) Phy_enter(), chem_enter(), eng_enter()- Checks if the letter inputted is in word, if yes, it executes the previous function, else it adds a tally to the errors and
	proceeds with the creation of the hangman figure.

Admin module-
1) AdPhy(), AdChem(), AdEng()- Appends record with values inputted by the values into the data file.
2) RePhy(), ReChem(), ReEng()- Removes record from the data file with a serial number inputted by the user.
3) VPhy(), VChem(), VEng()- Displays binary file in IDLE and CSV files in MS Excel.

Bibliography
1. Python GUI Programming With Tkinter – Real Python https://realpython.com/python-gui-tkinter/
2. Tabulate function https://pypi.org/project/tabulate/
3. OS Start file function https://python101.pythonlibrary.org/chapter16_os.html#:~:text=startfile()-,The%20os.,it%20opens%20in%20Adobe%20Reader.
4. W3Schools and Stack Overflow for miscellaneous functions and queries
