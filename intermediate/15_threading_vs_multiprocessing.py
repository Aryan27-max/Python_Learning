# Threading vs Multiprocessing - the idea, in plain words.
# (This file just prints a summary. The next two files have real code.)

summary = """
PROCESS
  - A whole separate running program with its own memory.
  - Can truly run on different CPU cores at the same time.
  - Heavier to start, and sharing data between them takes extra work.
  - Best for CPU-heavy work, like big calculations.

THREAD
  - A smaller worker that lives INSIDE one process.
  - All threads share the same memory, so sharing data is easy
    (but they can step on each other's toes, so be careful).
  - Light and quick to start.
  - Best for waiting-heavy work, like downloading files or reading from disk.

THE GIL (Global Interpreter Lock)
  - In regular Python, only one thread runs Python code at a time.
  - So threads don't speed up heavy maths - but they're great when
    your program spends most of its time waiting.
  - Multiprocessing gets around the GIL because each process has its own.

QUICK RULE
  - Lots of waiting (network, files)  -> threads
  - Lots of number crunching          -> processes
"""

print(summary)
