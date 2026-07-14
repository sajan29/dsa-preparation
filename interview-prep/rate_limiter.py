from collections import deque
class User:
    def __init__(self, user_id, limit, window_secs):
        self.user_id = user_id
        self.limit = limit
        self.window_secs = window_secs
        # self.request_count = 0
        # self.current_window = 0
        self.requests = deque()

class Response:
    OK = "OK"
    ERROR = "ERROR"

class Status:
    ALLOWED = "ALLOWED"
    REJECTED = "REJECTED"
# Collection of users
users = {}

def get_user(user_id):
    return users.get(user_id)

def register_user(user_id, limit, window_secs):
    if get_user(user_id) is not None:
        return Response.ERROR
    if limit<=0:
        return Response.ERROR
    if window_secs<=0:
        return Response.ERROR
    users[user_id] = User(user_id, limit, window_secs)
    return Response.OK

def address_request_fixed_window(user_id, timestamp):
    user = get_user(user_id)
    if user is None:
        return Response.ERROR
    window = (timestamp // user.window_secs)
    if window != user.current_window:
        user.current_window = window
        user.request_count = 0
    if user.request_count >= user.limit:
        return Status.REJECTED
    user.request_count += 1
    return Status.ALLOWED

def address_request(user_id, timestamp):

    user = get_user(user_id)
    if user is None:
        return Response.ERROR
    # Remove expired requests
    while user.requests and user.requests[0] <= timestamp - user.window_secs:
        user.requests.popleft()

    # Check limit
    if len(user.requests) >= user.limit:
        return Status.REJECTED
    # Accept request
    user.requests.append(timestamp)
    return Status.ALLOWED
    
while True:
    try:
        line = input().strip()
    except EOFError:
        break

    if not line:
        continue

    line = line.split()
    command = line[0]
    user_id = line[1]
    if command == "REGISTER":
        limit = int(line[2])
        window_secs = int(line[3])
        print(register_user(user_id,limit,window_secs))
    elif command == "REQUEST":
        timestamp = int(line[2])
        print(address_request(user_id, timestamp))



