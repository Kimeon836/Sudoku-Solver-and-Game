# Sudoku Solver and Game
Solves any sudoku puzzle using backtracking algorithm while visulazing the whole process. It's a web application made using Django.

It contains a **million** different puzzles to solve or be solved by computer.

Sudoku is 9x9 puzzle game where you solve the puzzle by writing a digit (1-9) in empty spaces making sure that same number ain't in same row, same column or same box.

## Installition and Running
 First install all required  libraries using following command

`pip freeze > requirements.txt`

Make sure you have *sudoku.csv* file in _main/static_. If you face any issues in csv file then you can download it from here

<a href="https://www.kaggle.com/bryanpark/sudoku">*One Million Sudoku Puzzles*</a>

Then run the project by following command:

`python manage.py runserver`

*or*

`python3 manage.py runserver`

If it shows migrations aren't applied then simply run following command:

`python manage.py migrate`

*or*

`python3 manage.py migrate`

and then re-run previous command.





