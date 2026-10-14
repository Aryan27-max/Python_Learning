# Multithreading - running several things "at once" inside one program.

import threading
import time
from queue import Queue

# --- Basic threads ---
def worker(name):
    print(f"{name} starting")
    time.sleep(0.5)   # pretend we're waiting on something, like a download
    print(f"{name} done")


threads = []
for i in range(3):
    t = threading.Thread(target=worker, args=(f"Thread {i}",))
    threads.append(t)
    t.start()          # off it goes

for t in threads:
    t.join()           # wait for each one to finish

print("All threads finished\n")


# --- Sharing data safely with a Lock ---
# Without a lock, two threads might update the same number at the same time and mess it up.
total = 0
lock = threading.Lock()

def add_one_hundred():
    global total
    for _ in range(100):
        with lock:      # only one thread at a time in here
            total += 1

threads = [threading.Thread(target=add_one_hundred) for _ in range(5)]
for t in threads:
    t.start()
for t in threads:
    t.join()
print("Total:", total, "\n")   # always 500


# --- Queue: a safe way to pass work between threads ---
q = Queue()
for job in range(5):
    q.put(job)

def do_jobs():
    while not q.empty():
        job = q.get()
        print(f"{threading.current_thread().name} handled job {job}")
        q.task_done()

workers = [threading.Thread(target=do_jobs, name=f"Worker-{i}") for i in range(2)]
for w in workers:
    w.start()
q.join()   # wait until every job is marked done
print("Queue empty, all jobs done")
