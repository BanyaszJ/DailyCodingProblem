'''Implement a job scheduler which takes in a function f and an integer n, and calls f after n milliseconds.'''

# --- config stuff ---
from time import sleep as sleep

n = 2000 #[ms]

def f():
    print("JOB'S DONE!")    
    
def job_scheduler(func, time):
    sleep(time/1000)
    func()
    
    
job_scheduler(f, n)