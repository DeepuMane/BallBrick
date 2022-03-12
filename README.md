# Ball Brick

The program is written on Python3.
Q1,Q2,Q3,Q4,Q5 are the solutions to the given questions respectively. 
The combined file is **[game.py](/game.py)** 

# How to run

Since the program is written on Py3 to run the program 

>    `python3 game.py`


## Procedure

The program initially ask the size of the matrix NxN 

    Enter the size of your NxN matrix: 7

Then it asks to add bricks to the matrix 

    Do you want to add bricks? Y/N :  Y
    Enter the brick's position and the brick type : 2 2 1

The block location should be added space separated accompanied by the brick weight.

> Enter the brick's position and the brick type : [i] [j] [ weight]

Then the program prints the current game matrix 

    WWWWWWW
    W     W
    W 111 W
    W     W
    W     W
    W     W
    WGGoGGW
The program asks the ball count

    Enter ball count :

The program ask if we want to traverse the ball 

    Do you want to traverse the ball ? Y/N :  Y
    Enter the direction in which the ball need to traverse : ST

There are three traverse mode

 - Straight -ST  
 - Left Diagonal- LD 
 - Right Diagonal- RD

