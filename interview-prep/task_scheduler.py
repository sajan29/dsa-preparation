import heapq
class Task:
    def __init__(self, task_id, execute_at, interval=None):
        self.task_id = task_id
        self.execute_at = execute_at
        self.status = Status.SCHEDULED
        self.interval = interval

class Response:
    OK = "OK"
    ERROR = "ERROR"

class Status:
    SCHEDULED = "SCHEDULED"
    RUNNING = "RUNNING"
    COMPLETED = "COMPLETED"
        
task_queue = []

tasks = {}

def get_task(task_id):
    return tasks.get(task_id)

def schedule_task(task_id, execute_at):
    task = get_task(task_id)
    if task is not None:
        return Response.ERROR
    if execute_at < 0:
        return Response.ERROR
    heapq.heappush(task_queue,(execute_at, task_id, None))
    tasks[task_id] = Task(task_id, execute_at)
    return Response.OK

def schedule_recurring_task(task_id, execute_at, interval):
    task = get_task(task_id)
    if task is not None:
        return Response.ERROR
    if execute_at < 0 or interval <= 0:
        return Response.ERROR
    heapq.heappush(task_queue,(execute_at, task_id, interval))
    tasks[task_id] = Task(task_id, execute_at, interval)
    return Response.OK

def run_task(current_time):
    task_ids = []
    while task_queue:
        if task_queue[0][0] <= current_time:
            execute_at, task_id, interval = heapq.heappop(task_queue)
            task_record = get_task(task_id)
            if task_record:
                if interval is not None:
                    task_record.status = Status.RUNNING
                    task_record.execute_at += interval
                    heapq.heappush(task_queue, (task_record.execute_at, task_id, interval))
                else:
                    task_record.status = Status.COMPLETED
                task_ids.append(task_id)
        else:
            break
    if not task_ids:
        return "NONE"  
    else:
        return ",".join(task_ids)

def cancel_task(task_id):
     task = get_task(task_id)
     if task is None:
         return Response.ERROR
     if task.status == Status.COMPLETED:
         return Response.ERROR
     del tasks[task_id]
     return Response.OK

while True:
    try:
        line = input().strip()
    except EOFError:
        break

    if not line:
        continue

    line = line.split()
    command = line[0]
    if command == "SCHEDULE":
        task_id = line[1]
        execute_at = int(line[2])
        print(schedule_task(task_id, execute_at))
    elif command == "SCHEDULE_RECURRING":
        task_id = line[1]
        execute_at = int(line[2])
        interval = int(line[3])
        print(schedule_recurring_task(task_id, execute_at, interval))
    elif command == "RUN":
        current_time = int(line[1])
        print(run_task(current_time))
    elif command == "CANCEL":
        task_id = line[1]
        print(cancel_task(task_id))