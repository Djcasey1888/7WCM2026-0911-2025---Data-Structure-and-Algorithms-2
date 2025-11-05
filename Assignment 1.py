import numpy as np  

def KnightsTourBacktracking(startingPosition: tuple[int, int]) -> tuple[bool, np.ndarray]:  
    possible_moves = np.array([(1,2),(1,-2),(-1,2),(-1,-2),(2,1),(2,-1),(-2,1),(-2,-1)], dtype=int) #all possible moves for the knight
    max_attempts = 10  
    attempts = 0  #to start an attempt counter

    while attempts < max_attempts:
        np.random.shuffle(possible_moves)
        attempts += 1 #will keep looping until max attempts has been reached
        print("Starting attempt ",attempts, "from ",startingPosition)  #prints starting position and attempt number
        board = np.zeros((8,8), dtype=int)#starting co-ordinates
        i, j = startingPosition
        board[i, j] = 1
    

        def move_possible(x, y):  
            return 0 <= x < 8 and 0 <= y < 8 and board[x, y] == 0  #checks to see if move is valid and unvisitied
        

        def solve(x, y, move_num):  #recursive function
                            
            if move_num > 64:  #checks to see if all spaces on the chessboard has been visited
                return True  #sucess
        
            for di, dj in possible_moves:  #tries every possible move for knight at a given time
                new_x, new_y = x + di, y + dj  #new position of knight
                if move_possible(new_x, new_y):  #checks again if move is valid
                    board[new_x, new_y] = move_num  #next move is placed onto the board
                    if solve(new_x, new_y, move_num + 1):  #next move after this
                        return True  #stop if board is full
                    board[new_x, new_y] = 0  #if move fails, backtrack
            return False  #return false if no move moves brings sucess

        success = solve(i, j, 2)  #starts the function solve from move number 2. Move one already done by starting position.

        if success: 
            print("Success on attempt ",attempts)  #shows how many attempts it took
            print(board)  # prints board completed
            return True, board
        else:
            print("Backtracking again")  #attempt failed

    print("No successful tour found after", max_attempts, "attempts.")  #attempts maxed out
    return False, board  #return failure and final board


def KnightsTourLasVegas(startingPosition: tuple[int, int]) -> tuple[bool, np.ndarray]:
    print("Starting position is ", startingPosition)
    attempts = 0  #attempt counter
    max_attempts = 1000000  #maximum tries
    possible_moves = np.array([(1,2),(1,-2),(-1,2),(-1,-2),(2,1),(2,-1),(-2,1),(-2,-1)], dtype=int)  #all possible moves

    while attempts <= max_attempts:
        board = np.zeros((8,8), dtype=int)  #empty chessboard 8x8
        i, j = startingPosition 
        board[i, j] = 1  #starting square=1
        k = 1  # move counter
        complete = True  #tour is complete

        while k < 64:  #if all sqaures visited
            valid_moves = [(i+di, j+dj) for di, dj in possible_moves  #all valid and legal moves
                           if 0 <= i+di < 8 and 0 <= j+dj < 8 and board[i+di, j+dj] == 0]  #checks to see if move is unvisited and on the board

            if not valid_moves:  #not valid moves left
                complete = False  #failed
                break

            random_move = np.random.randint(len(valid_moves))  #chooses a random move in valid moves
            new_i, new_j = valid_moves[random_move]  # new position of i and j

            k += 1  
            board[new_i, new_j] = k  #record new position of the knight
            i, j = new_i, new_j  #upates the new position

        if complete:  #checks to see if tour is done
            print("Tour completed after ", attempts + 1, "attempts")  
            print("Starting position:", startingPosition)
            print(board)  
            return True, board  
        else:  
            attempts += 1  
            if attempts % 100000 == 0:  
                print(attempts, " attempts tried... still searching")  #progress message

    print("Maximum attempts exceeded")  #stops when maxed out attempts
    return False, board 

def main_menu():
    while True:  #keeps running until user exits
        print("Please select an option")  
        print("Type 1 for Backtracking")  
        print("Type 2 for Las Vegas")  
        print("Type 3 to Exit")  
        choice = int(input("Please select now: "))  

        if choice == 1:  
            print("You have chosen Backtracking")
            (start_i, start_j) = (np.random.randint(2,6), np.random.randint(2,6)) #edited so the starting position is more central, more options to move, quicker
            startingPosition=(start_i, start_j)
            KnightsTourBacktracking(startingPosition) 
            

        elif choice == 2:  
            print("You have chosen Las Vegas")  
            (start_i, start_j) = (np.random.randint(2,6), np.random.randint(2,6)) #edited so the starting position is more central, more options to move, quicker
            startingPosition=(start_i, start_j)  
            KnightsTourLasVegas(startingPosition)  

        elif choice == 3:  
            print("Exit confirmed.")
            break  

        else:  
            print("Invalid option, please try again.")  
main_menu()  


