# It allows you to create process that runs parallel
# When to use:
    # 1. CPU-Bound Task:
        # - Task that rae heavy on CPU usgae (eg: mathemetical computation, data preprocessing)
    # 2. Parallel execution
        # - Multiple cores of cpu
        
import multiprocessing
import time 

def square_numbers():
    for i in range(5):
        time.sleep(1)
        print(f'Square: {i * i}')
        
def cube_numbers():
    for i in range(5):
        time.sleep(1.5)
        print(f'Cube: {i * i * i}')

if __name__ == "__main__":        
    t = time.time()
            
    # Create 2 Processes
    p1 = multiprocessing.Process(target = square_numbers)
    p2 = multiprocessing.Process(target = cube_numbers)

    # start the process
    p1.start()
    p2. start()

    # wait to complete
    p1.join()
    p2.join()

    # Time took to complete
    finished_time = time.time() - t
    print(finished_time)