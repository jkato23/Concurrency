import concurrent.futures
import time

start = time.perf_counter()

def do_something(seconds):
    print(f'Sleeping {seconds} second(s)...')
    time.sleep(seconds)
    return f'Done Sleeping...{seconds}'

executor = concurrent.futures.ThreadPoolExecutor()
secs = [5, 4, 3, 2, 1]
results = executor.map(do_something, secs)

finish = time.perf_counter()

print(f'Finished in {round(finish-start, 2)} second(s)')
