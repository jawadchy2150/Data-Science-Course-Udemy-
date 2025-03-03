import multiprocessing
import time
import math
import sys

sys.set_int_max_str_digits(100000)

def compute_factorial(number):
    result = math.factorial(number)
    return result

if __name__ == "__main__":
    numbers = [5000, 6000]
    start_time = time.time()

    with multiprocessing.Pool() as pool:
        results = pool.map(compute_factorial, numbers)
    
    end_time = time.time()
    print(f"Result: {results}")
    print(f"time taken: {end_time - start_time}")