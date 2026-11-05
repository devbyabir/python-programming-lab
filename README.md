# Python Programming Labs

Exercises from the fourth-semester Object Oriented Techniques course at Zhengzhou University. The labs progress from input and control flow to file handling, classes, and plotting.

## Exercises

| Lab | Python files | What I practiced |
| --- | --- | --- |
| 1 | [first_program.py](lab01-basics/first_program.py), [calculator.py](lab01-basics/calculator.py), [mad_libs.py](lab01-basics/mad_libs.py) | Output, arithmetic, user input and formatted strings |
| 2 | [functions.py](lab02-functions/functions.py) | Default arguments, return values, lists and tuples |
| 3 | [loops.py](lab03-control-flow/loops.py), [guess_number.py](lab03-control-flow/guess_number.py) | Loops, conditionals and validating guesses |
| 4 | [algorithms.py](lab04-algorithms/algorithms.py) | String reversal, iterative Fibonacci and bubble sort |
| 5 | [file_operations.py](lab05-files/file_operations.py) | Reading, writing and updating a text file with error handling |
| 6 | [person_student.py](lab06-classes/person_student.py), [animal_dog.py](lab06-classes/animal_dog.py), [library.py](lab06-classes/library.py) | Classes, inheritance, method overriding and object lifetime |
| 8 | [shapes.py](lab08-visualization/shapes.py), [sales_chart.py](lab08-visualization/sales_chart.py) | Drawing with Matplotlib and plotting sample sales with Seaborn |

Lab 6 and the Lab 8 sales chart were adapted from submitted code. Labs 1-5 and the Lab 8 shapes exercise were solved from the course prompts while preparing this repository. Lab 7 was absent from the available materials.

## Run locally

Labs 1–6 use the standard library. From the repository root, run an individual file:

```sh
python lab01-basics/calculator.py
python lab03-control-flow/guess_number.py
python lab04-algorithms/algorithms.py
python lab05-files/file_operations.py
python lab06-classes/person_student.py
```

The file example uses a temporary directory. The class examples print messages from `__del__` to illustrate finalization. Their timing can vary, and the code does not rely on them for cleanup.

Lab 8 uses Matplotlib and Seaborn. From the repository root in Windows PowerShell:

```powershell
python -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements-visualization.txt
.\.venv\Scripts\python.exe lab08-visualization/shapes.py shapes.png
.\.venv\Scripts\python.exe lab08-visualization/sales_chart.py sales.png
```

On macOS or Linux, use `.venv/bin/python` in place of `.\.venv\Scripts\python.exe`. Omit the image filename to open a plot window.

## Compare the results

- Try zero as the divisor and compare the result with a normal division.
- Check Fibonacci positions 0 and 1 before trying larger values.
- Compare the original list with the sorted copy returned by bubble sort.
- Call `greet()` on a Person and a Student to see how overriding changes the result.
- Change a sample sales value and check that both its bar and label update.
