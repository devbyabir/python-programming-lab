# Python Programming Labs

Exercises from the fourth-semester Object Oriented Techniques course at Zhengzhou University. The labs progress from input and control flow to file handling, classes, and plotting.

| Lab | Practice | Source |
| --- | --- | --- |
| [01](lab01-basics) | First output, addition, calculator, Mad Libs | Revisited |
| [02](lab02-functions) | Default arguments, return values, lists, tuples | Revisited |
| [03](lab03-control-flow) | Countdown, squares, comparison, number guessing | Revisited |
| [04](lab04-algorithms) | String reversal, Fibonacci, bubble sort | Revisited |
| [05](lab05-files) | Read, write and update a file | Revisited |
| [06](lab06-classes) | Inheritance, overriding, object lifecycle | Adapted from submitted code |
| [08](lab08-visualization) | Drawing shapes and charting sample sales | Shapes revisited, chart adapted from submitted code |

Revisited exercises were implemented for this repository from the course prompts. Lab 7 was absent from the available materials.

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

Install the plotting dependencies in a virtual environment for Lab 8. Omit the image path to display the figure in a window.

```sh
python -m pip install -r requirements-visualization.txt
python lab08-visualization/shapes.py shapes.png
python lab08-visualization/sales_chart.py sales.png
```

## Compare the results

- Try zero as the divisor and compare the result with a normal division.
- Check Fibonacci positions 0 and 1 before trying larger values.
- Compare the original list with the sorted copy returned by bubble sort.
- Call `greet()` on a Person and a Student to see how overriding changes the result.
- Change a sample sales value and check that both its bar and label update.
