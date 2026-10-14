# Multiprocessing - using several CPU cores for real parallel work.

from multiprocessing import Process, Value, Lock, Pool
import os


def square_numbers():
    for i in range(3):
        print(f"process {os.getpid()} -> {i * i}")


def add_100(number, lock):
    for _ in range(100):
        with lock:
            number.value += 1


def cube(n):
    return n * n * n


# This check is REQUIRED for multiprocessing on Windows and macOS.
# It stops the new processes from re-running this setup code.
if __name__ == "__main__":

    # --- Basic processes ---
    processes = [Process(target=square_numbers) for _ in range(2)]
    for p in processes:
        p.start()
    for p in processes:
        p.join()
    print("Processes done\n")

    # --- Sharing a number between processes ---
    # Processes don't share memory, so we use a special shared Value.
    shared = Value("i", 0)   # "i" means integer, starting at 0
    lock = Lock()
    processes = [Process(target=add_100, args=(shared, lock)) for _ in range(2)]
    for p in processes:
        p.start()
    for p in processes:
        p.join()
    print("Shared value:", shared.value, "\n")   # 200

    # --- Pool: the easy way. Hand it a list and it splits the work up ---
    with Pool() as pool:
        results = pool.map(cube, [1, 2, 3, 4, 5])
    print("Cubes:", results)
