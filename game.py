bcount=0
size=input("Enter the size of your NxN matrix: ")
size=int(size)
game=[]
global mid
mid=int(size//2)
global b
b=0
win=[['W', 'W', 'W', 'W', 'W', 'W', 'W'], ['W', ' ', ' ', ' ', ' ', ' ', 'W'], ['W', ' ', ' ', ' ', ' ', ' ', 'W'], ['W', ' ', ' ', '1', '1', ' ', 'W']]

def array(x):
    
    for i in range(x):
     game.append([])
     if i==0: 
         abc=game[0]
         for h in range(x):
              abc.append("W")  
     elif i==(x-1):

         finalrow=game[x-1]    
         finalrow.append("W")
         for i in range(x-2):
             finalrow.append("G")
         finalrow.append("W")
         game[x-1][mid]="o"
     else:
         asd=game[i]
         asd.append("W")
         for i in range(x-2):
             asd.append(" ")
         asd.append("W")


array(size)


def brick(inpstr):
    splstr=inpstr.split( )
    n=int(splstr[0])
    m=int(splstr[1])
    weight=splstr[2]
    game[n][m]=weight



def destroy(direction):
    global mid
    if direction=="LD":
        if game[size-1][mid-1]=='_':
          game[size-1][mid]="_"
          mid=mid-1
          game[size-1][mid]="o"
        else:
          game[size-1][mid]="G" 
          mid=mid-1
          game[size-1][mid]="o"
    elif direction=="RD":
        if game[size-1][mid+1]=='_':
          game[size-1][mid]="_"
          mid=mid+1
          game[size-1][mid]="o"
        else:
          game[size-1][mid]="G"
          mid=mid+1
          game[size-1][mid]="o"

        
    else:
        print("ST")

    for x in range(size-2,0,-1):
            if game[x][mid]!=" ":
                    if game[x][mid]=="1":
                         game[x][mid]=" "
                         break
                    elif game[x][mid]=="B":
                        game[x][mid]=" "
                        global b
                        if b==0:
                          game[size-1][mid+1]="_"
                          b=b+1
                        else:
                          game[size-1][mid-1]="_"

                    elif game[x][mid]=="DE":
                         for i in range(1,size-1):
                             game[x][i]=" "   
                    elif game[x][mid]=="DS":
                             if mid==1:
                                 game[x][mid]=" "
                                 game[x][mid+1]=" "
                                 game[x-1][mid+1]=" "
                                 game[x-1][mid]=" "
                                 game[x+1][mid+1]=" "
                                 break
                             elif mid==(size-2):
                                 game[x][mid]=" "
                                 game[x][mid-1]=" "
                                 game[x-1][mid-1]=" "
                                 game[x-1][mid]=" "
                                 game[x+1][mid-1]=" " 
                                 break
                             else:
                                 game[x][mid]=" "
                                 game[x][mid-1]=" "
                                 game[x][mid+1]=" "
                                 game[x-1][mid-1]=" "
                                 game[x-1][mid]=" "
                                 game[x-1][mid+1]=" "
                                 game[x+1][mid-1]=" "
                                 game[x+1][mid+1]=" "    
                                 break      
                    else:
                         game[x][mid]=str(int(game[x][mid])-1)
                         break   



def printmat():
    for i in range(0,size):
         row=""
         for j in range(0,size):
             chart=str(game[i][j])
             row=row+chart
         print(row)    



while True:

    if input('Do you want to add bricks? Y/N :  ') == 'n':
        printmat()
        break
    else:
         position=input("Enter the brick's position and the brick type : ")
         brick(position)


ballcount=input("Enter ball count :  ")
ballcount=int(ballcount)


while True:

    if input('Do you want to traverse the ball ? Y/N :  ')=='n':
        printmat()
        del game[size-1]
        if game==win:
             print("HURRAY YOU WON !!")
        break
    else:
         balldir=input("Enter the direction in which the ball need to traverse : ")    
         destroy(balldir) 
         printmat()
         print("The ballcount is ",ballcount)
         
      



