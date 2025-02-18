# ROBOSOC_Chess_AI

Fork of the RoboSoc "Arm Chess Bot" (C.R.A.P) Repository for the current year 2023 - 2024


# Individual Work Structure
As the team expands, it is currently expected of each individual team member to pick a file **not** currently listed in *Individual Documentation* or *Group Documentation* and begin documenting how their chosen file works. This is presently done for the benefit of code literacy, such that further features may be implemented in future. 

  **Group Documentation** is to be worked on by the team within labs or via collaboration over any form of social media. 

During each Wednesday 2:00 PM to 5:00 PM Session the team will collaborate on the work done in the previous session or in their own time, to keep people up to date. 

Working on:

* Documentation 
* Error Handling for Server

Distribution of Work: 
* Multiple people to work on the main.py
* Individual work in spare time

Group Documentation:
* 

Individual Documentation:
* Server.py - Ben - FINISHED 
* ai.py - Santiago 
* Showcase Code/PC/main.py - Ben
* Showcase Code/PC/crap_ai/main.py - Ben

If any individual wishes to be added to another individual's file which is already being worked on, see rudeeyonker (Dylan) or Ciph#6918 (Ben) on Discord such that it may be switched to a group collaboration.  

Main idea:
The GUI displays the board and continuously updates the board state based on the payload of a GET request made to the server on port:5000. It calculates a move based on this board state. It then sends the correct opcode to the microcontroller to make the arm move.
