""""
Gianmarco Folchi
You are tasked with implementing three process scheduling algorithms: FIFO (First In, First Out), Pre-emptive SJF (Shortest Job First), and Round Robin in Python.
The implementation should include the following components:

1. A data structure to represent a process, including its arrival time, execution time, and status.
2. A scheduler function for each algorithm that takes in a list of processes and implements the chosen scheduling algorithm.
3. A time slice parameter (Q-value) for Round Robin, which determines how long each process should be allowed to run before being preempted.
4. A function to calculate our standard metrics: turnaround time, waiting time, and response time for each process.

Input File Format
Example:

processcount 3  # Read 3 processes
runfor 20       # Run for 20 time units
use sjf
process name A arrival 0 burst 5
process name B arrival 1 burst 4
process name C arrival 4 burst 2
end

Output File Format
Example:

3 processes
Using preemptive Shortest Job First
Time   0 : A arrived
Time   0 : A selected (burst   5)
Time   1 : B arrived
Time   4 : C arrived
Time   5 : A finished
Time   5 : C selected (burst   2)
Time   7 : C finished
Time   7 : B selected (burst   4)
Time  11 : B finished
Time  11 : Idle
Time  12 : Idle
Time  13 : Idle
Time  14 : Idle
Time  15 : Idle
Time  16 : Idle
Time  17 : Idle
Time  18 : Idle
Time  19 : Idle
Finished at time  20

A wait   0 turnaround   5  response 0
B wait   6 turnaround  10  response 6
C wait   1 turnaround   3 response 1
"""

class Process:
    def __init__(self, name, arrival_time, burst_time):
        self.name = name
        self.arrival_time = arrival_time
        self.burst_time = burst_time
        self.remaining_time = burst_time
        self.start_time = None
        self.finish_time = None

    def calculate_turnaround_time(self):
        return self.finish_time - self.arrival_time if self.finish_time else None

    def calculate_waiting_time(self):
        return self.calculate_turnaround_time() - self.burst_time if self.finish_time else None

    def calculate_response_time(self):
        return self.start_time - self.arrival_time if self.start_time else None


def fifo_scheduler(processes):
    time = 0
    for process in sorted(processes, key=lambda x: x.arrival_time):
        if time < process.arrival_time:
            time = process.arrival_time
        process.start_time = time
        time += process.burst_time
        process.finish_time = time

def preemptive_sjf_scheduler(processes):
    time = 0
    ready_queue = []
    while processes or ready_queue:
        # Add processes to the ready queue based on arrival time
        # Select process with shortest remaining time
        # Update time and process information
        pass  # This will be filled with the actual logic

def round_robin_scheduler(processes, q):
    time = 0
    ready_queue = []
    while processes or ready_queue:
        # Rotate through processes in ready queue with time slice q
        # Update time and process information
        pass  # This will be filled with the actual logic
