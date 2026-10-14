# Intermediate Python Notes

These are my code notes from the freeCodeCamp "Intermediate Python Programming Course" video.
Each topic from the video has its own file. Open one, read the comments, run it, and play around.

To run a file:

```
python 01_lists.py
```

Everything here uses Python's built-in modules, so there's nothing to install.

## What's in each file

| File | What it covers |
|---|---|
| `01_lists.py` | Ordered collections you can change: adding, removing, slicing, sorting and copying |
| `02_tuples.py` | Lists you can't change, plus unpacking values into variables |
| `03_dictionaries.py` | key: value pairs, looping over them, merging and copying |
| `04_sets.py` | Collections with no duplicates, plus union, intersection and difference |
| `05_strings.py` | Slicing, handy methods, split and join, and f-string formatting |
| `06_collections.py` | Counter, namedtuple, OrderedDict, defaultdict and deque |
| `07_itertools.py` | product, permutations, combinations, accumulate, groupby and the infinite ones |
| `08_lambda_functions.py` | One-line functions, and using them with sorted, map, filter and reduce |
| `09_exceptions_and_errors.py` | Common errors, try/except/else/finally, raise, assert and custom errors |
| `10_logging.py` | A better print(): log levels, formatting, and writing to a file |
| `11_json.py` | Turning Python data into JSON and back, with strings and files |
| `12_random_numbers.py` | The random module, seeds, and the secrets module for anything security related |
| `13_decorators.py` | Wrapping functions, decorators with arguments, and class decorators |
| `14_generators.py` | yield, saving memory, and generator expressions |
| `15_threading_vs_multiprocessing.py` | The plain-English difference between threads and processes (just prints a summary) |
| `16_multithreading.py` | Starting threads, using a Lock, and passing work with a Queue |
| `17_multiprocessing.py` | Starting processes, sharing a value between them, and using a Pool |
| `18_function_arguments.py` | Positional, keyword, default, *args, **kwargs, and the list-as-default gotcha |
| `19_asterisk_operator.py` | Every job the * does in Python |
| `20_shallow_vs_deep_copy.py` | Assignment vs shallow copy vs deep copy, and why it matters |
| `21_context_managers.py` | The "with" statement, and how to build your own |

## A few heads-ups

- `10_logging.py` creates an `app.log` file, `11_json.py` creates `person.json`, and `21_context_managers.py` creates `notes.txt`. Delete them whenever you like.
- `17_multiprocessing.py` has an `if __name__ == "__main__":` line. Don't remove it, multiprocessing needs it on Windows and macOS.
