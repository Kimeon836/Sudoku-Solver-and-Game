from django.http import JsonResponse
from django.shortcuts import render
from .solver import empty_cell, solve
from .apps import boards
import random
import copy

# Main page, It chooses a random board from 'boards' and also passes speed options.
# The initial_board is the initial state of board and is a global variable
def home(response):
    global initial_board

    initial_board = random.choice(boards)
    # Copied array so the initial_board doesn't changes 
    # when changes are made into sudoku_board.

    sudoku_board = copy.deepcopy(initial_board)
    speed_options = {
                    "Normal": 0.3,
                    "Fast": 0.2,
                    "GodSpeed": 0,
                    }
    context = {
        "sudoku_board":sudoku_board,
        "speed_options":speed_options,
    }

    return render(response, 'main/index.html', context)

# It is called through a AJAX call when user changes the number in board. 
# It returns a JSONresponse containing a boolean value if it is correct by
# using functions from solver.py and also returns a boolean value whether all cells are solved.
def check(response):
    if response.method == "POST":
        # The data contains x and y coordinates of element in array which is changed,
        # the value which it is changed into.
        data = response.POST
        sudoku_board = copy.deepcopy(initial_board)
        x, y = data.get('pos').split("x")
        x, y = int(x), int(y)
        val = data.get('val')

        # Returns False if value is not digit or if it is 0 or if it has more than one character
        # It can't have more than one character as set in HTML but F12...
        if not str(val).isdigit() or int(val) == 0 or len(str(val)) > 1:
            return JsonResponse({'is_correct': False, 'all_solved':False})

        # Changing that value in copied board and passing it to solve function from solver.py
        sudoku_board[x][y] = int(val)
        
        is_correct, _, _ = solve(sudoku_board, [])

        # Making changes to original board if it's correct
        if is_correct:
            initial_board[x][y] = int(val)
        else:
            initial_board[x][y] = 0

        # Checking if all cells are solved
        all_solved = not bool(empty_cell(initial_board))

        data = {
            'is_correct': is_correct,
            'all_solved':all_solved,
        }
        return JsonResponse(data)
    else:
        return JsonResponse({})

# Returns a JSONresponse containing steps and a boolean value telling if it was solved or not
# Steps is a 2D array containing x and y coordinates, and the value it was changed to
# Called by AJAX call when user clicks solve
def get_steps(response):
    if response.method == "POST":
        sudoku_board = copy.deepcopy(initial_board) # Copying the current instance of initial board
        d = []
        if_solved, steps, _ = solve(sudoku_board, d)
        return JsonResponse({"steps":steps, "if_solved":if_solved})
    else:
        return JsonResponse({})
