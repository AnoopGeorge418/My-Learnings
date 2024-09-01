# Muliti Threading
# - When to use it?:
#   - I/O Bound Task:
#     - Task that spends more time for I/O operations(eg: file operations, network request)
#   - Concurrent Execution:
#     - When u want to improve the throughput of your application by performing mulltiple operations concurrently.

import threading
import time

def print_number():
    for i in range(5):
        time.sleep(2)
        print(f'Numbers: {i}')
        
def print_letters():
    for letter in 'abcde':
        time.sleep(2)
        print(f'Letters: {letter}')
        
# creating 2 new threads
t1 = threading.Thread(target = print_number)
t2 = threading.Thread(target = print_letters)

t = time.time() 

# Starting the threads
t1.start()
t2.start()

# waiting for the threads to complete
t1.join()
t2.join()

# Time took to complete
finished_time = time.time() - t
print(finished_time)