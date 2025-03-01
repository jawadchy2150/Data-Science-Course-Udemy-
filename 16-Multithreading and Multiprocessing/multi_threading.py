import time
import threading

def print_numbers():
    for i in range(5):
        time.sleep(2)
        print(f"Number: {i}")

def print_letter():
    for i in "abcde":
        # time.sleep(2)
        print(f"Letter: {i}")

thread1 = threading.Thread(target=print_numbers)
thread2 = threading.Thread(target=print_letter)

t= time.time()

thread1.start()
thread2.start()
thread1.join()
thread2.join()
total_time = time.time() -t

print(total_time)