import time
import sys
import multiprocessing

def print_numbers(num):
    print(f"Number: {num}")
    sys.stdout.flush() 
      # Simulate some delay
    time.sleep(0.1)

def worker_func(iter):
    with multiprocessing.Pool(3) as pool:
        pool.map(print_numbers, iter)

if __name__ == "__main__":
    nums1 = list(range(0,101))
    nums2 = list(range(102,202))
    nums3 = list(range(203, 303))
    iters = [nums1,nums2,nums3]
    processes = []
    for iter in iters:
        p = multiprocessing.Process(target=worker_func,args=(iter,))
        processes.append(p)
        p.start()

    