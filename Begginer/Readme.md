# Python Course Notes 

Hey! These are my code notes from the freeCodeCamp **"Learn Python – Full Course for Beginners"** video.
Every topic from the video has its own little file, so you can open one, read the comments, and run it.

To run any file:
```
python filename.py
```

---

##  1_rock_paper_scissors
The warm-up project from the start of the video.

- `rock_paper_scissors.py` – You type rock, paper or scissors and the computer picks one at random. Along the way it shows variables, functions, dictionaries, `input()`, the `random` library, lists, if/elif/else, nested ifs and f-strings.

---

##  2_fundamentals
The main chunk of the course. One file per topic, in the same order as the video.

| File | What it's about |
|---|---|
| `01_variables.py` | Naming and storing values |
| `02_expressions_statements.py` | Bits of code that give values vs full instructions |
| `03_comments.py` | Leaving notes in your code |
| `04_data_types.py` | str, int, float, bool and switching between them |
| `05_arithmetic_operators.py` | + - * / % ** // |
| `06_comparison_operators.py` | ==, !=, >, < and friends |
| `07_boolean_operators.py` | and, or, not |
| `08_bitwise_operators.py` | Working with the 1s and 0s (rarely needed) |
| `09_is_and_in_operators.py` | Is it the same object? Is it inside the list? |
| `10_ternary_operator.py` | if/else squeezed onto one line |
| `11_strings.py` | Working with text |
| `12_string_methods.py` | upper, lower, split, replace and more |
| `13_escaping_characters.py` | Using \n, \t, \" inside text |
| `14_string_slicing.py` | Grabbing parts of a string |
| `15_booleans.py` | True/False, plus "truthy" and "falsy" |
| `16_numbers.py` | int, float, complex |
| `17_builtin_functions.py` | len, max, min, sum, round... |
| `18_enums.py` | Named fixed values |
| `19_user_input.py` | Asking the user to type something |
| `20_control_statements.py` | if, elif, else |
| `21_lists.py` | Ordered collections you can change |
| `22_sorting_lists.py` | sort() vs sorted() |
| `23_tuples.py` | Lists you can't change |
| `24_dictionaries.py` | key: value pairs |
| `25_sets.py` | Collections with no duplicates |
| `26_functions.py` | Reusable blocks of code |
| `27_variable_scope.py` | Where a variable can be used |
| `28_nested_functions.py` | Functions inside functions |
| `29_closures.py` | Inner functions that remember things |
| `30_objects.py` | Everything in Python is an object |
| `31_loops.py` | while and for loops |
| `32_break_continue.py` | Stopping or skipping in a loop |
| `33_classes.py` | Making your own objects + inheritance |
| `34_modules.py` | Importing code from other files (uses `dog_helper.py`) |
| `35_command_line_args.py` | Passing values when you run the script |
| `36_lambda_functions.py` | Tiny one-line functions |
| `37_map_filter_reduce.py` | Working on a whole list at once |
| `38_recursion.py` | A function calling itself |
| `39_decorators.py` | Wrapping a function with extra behaviour |
| `40_docstrings.py` | Describing your functions |
| `41_annotations.py` | Type hints |
| `42_exceptions.py` | Catching errors with try/except |
| `43_with.py` | Auto cleanup, mostly for files |
| `44_pip_packages.py` | Installing other people's code |
| `45_list_comprehension.py` | Building lists in one line |
| `46_polymorphism.py` | Same method name, different classes |
| `47_operator_overloading.py` | Making +, > work on your own classes |

---

##  3_blackjack
The final project – a playable Blackjack game in the terminal. It's split into one file per class:

- `card.py` – One playing card (suit + rank).
- `deck.py` – All 52 cards, with shuffle and deal.
- `hand.py` – The cards someone's holding, and their score (handles the Ace being 1 or 11).
- `game.py` – The actual game loop. **Run this one to play!**

```
cd 3_blackjack
python game.py
```

Have fun! 🎉
