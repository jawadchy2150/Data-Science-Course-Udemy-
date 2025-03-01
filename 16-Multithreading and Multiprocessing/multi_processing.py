import multiprocessing
import time

def square_numbers():
    for i in range(5):
        time.sleep(1)
        print(f"square: {i*i}")

def cube_numbers():
    for i in range(5):
        time.sleep(1.5)
        print(f"cube: {i * i * i}")

if __name__ == "__main__":

    process1 = multiprocessing.Process(target=square_numbers)
    process2 = multiprocessing.Process(target=cube_numbers)

    t = time.time()

    process1.start()
    process2.start()

    process1.join()
    process2.join()

    finished_time = time.time() -t
    print(finished_time)