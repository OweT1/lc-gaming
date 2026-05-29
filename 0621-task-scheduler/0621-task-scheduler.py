class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        task_count = Counter(tasks)
        pq = []
        for task, count in task_count.items():
            heapq.heappush(pq, (-count, task))

        cooldown_tasks = {}
        intervals = 0
        while pq or cooldown_tasks:
            intervals += 1
            for t in cooldown_tasks:
                if cooldown_tasks[t] == 0 and t[0]+1 < 0:
                    heapq.heappush(pq, (t[0]+1, t[1]))
                cooldown_tasks[t] -= 1
                
            cooldown_tasks = {k: v for k, v in cooldown_tasks.items() if v >= 0 and k[0] < -1} # only add to cooldown if there is a need to execute the task again

            if pq:
                next_task = heapq.heappop(pq)
                if next_task[0] < 0:
                    cooldown_tasks[next_task] = n
        return intervals-1
        
        