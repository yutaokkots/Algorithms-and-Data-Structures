'''
933. Number of Recent Calls
Easy

You have a RecentCounter class which counts the number of recent requests within a certain time frame.

Implement the RecentCounter class:

RecentCounter() Initializes the counter with zero recent requests.
int ping(int t) Adds a new request at time t, where t represents some time in milliseconds, and returns the number of requests that has happened in the past 3000 milliseconds (including the new request). Specifically, return the number of requests that have happened in the inclusive range [t - 3000, t].
It is guaranteed that every call to ping uses a strictly larger value of t than the previous call.


Example 1:

Input
["RecentCounter", "ping", "ping", "ping", "ping"]
[[], [1], [100], [3001], [3002]]
Output
[null, 1, 2, 3, 3]

Explanation
RecentCounter recentCounter = new RecentCounter();
recentCounter.ping(1);     // requests = [1], range is [-2999,1], return 1
recentCounter.ping(100);   // requests = [1, 100], range is [-2900,100], return 2
recentCounter.ping(3001);  // requests = [1, 100, 3001], range is [1,3001], return 3
recentCounter.ping(3002);  // requests = [1, 100, 3001, 3002], range is [2,3002], return 3


'''
from collections import deque
from _0933_numberOfRecentCalls_supplemental import command, value
import time

class RecentCounterStack:
    def __init__(self):
        self.stack = []
        self.temp = []

    def ping(self, t: int) -> int:
        self.stack.append(t)
        counter = 0
        start = t - 3000
        while self.stack:
            popped_time = self.stack.pop()
            if start <= popped_time:
                counter += 1
                self.temp.append(popped_time)
            else:
                break
        while self.temp:
            self.stack.append(self.temp.pop())
        
        return counter
    
class RecentCounterQueue:
    def __init__(self):
        self.q = deque()

    def ping(self, t: int) -> int:
        self.q.append(t)
        if self.q:
            while t - 3000 > self.q[0]:
                self.q.popleft()
        return len(self.q)





rcstack = RecentCounterStack()
rcstack_result = []

start_1 = time.time()
for c in range(1, len(command)):
    res = rcstack.ping(value[c][0])
    #rcstack_result.append(res)
end_1 = time.time()

#print(rcstack_result)
print(end_1 - start_1)

rcqueue = RecentCounterQueue()
rcqueue_result = []

start_2 = time.time()
for c in range(1, len(command)):
    res = rcqueue.ping(value[c][0])
    #rcqueue_result.append(res)
end_2 = time.time()

#print(rcstack_result)
print(end_2 - start_2)


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)