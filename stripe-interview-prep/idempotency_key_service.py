class IdempotencyKey:
    def __init__(self, fingerprint, response, timestamp, ttl):
        self.fingerprint = fingerprint
        self.response = response
        self.timestamp = timestamp
        self.ttl = ttl

class Response:
    OK = "OK"
    ERROR = "ERROR"

idempotency_keys = {}

def is_expired(timestamp, record):
    return timestamp > (record.timestamp + record.ttl)

def is_identical(original_fingerprint, new_fingerprint):
    return original_fingerprint == new_fingerprint

def create_idempotency_key(key, fingerprint, response, timestamp, ttl):
    if ttl <= 0:
        return Response.ERROR
    record = idempotency_keys.get(key)
    if record:
        if not is_identical(record.fingerprint,fingerprint) and timestamp <= (record.timestamp + record.ttl):
            return Response.ERROR
        if is_expired(timestamp, record):
            del idempotency_keys[key]
        elif is_identical(record.fingerprint,fingerprint):
            return record.response
    idempotency_keys[key] = IdempotencyKey(fingerprint, response, timestamp, ttl)
    return Response.OK
    
def get_idempotency_key(key, timestamp):
    record = idempotency_keys.get(key)
    if record is None:
        return Response.ERROR
    if is_expired(timestamp, record):
        del idempotency_keys[key]
        return Response.ERROR
    return record.response

def cleanup(timestamp):
    count = 0
    eligible_keys = []
    for key, value in idempotency_keys.items():
        if is_expired(timestamp, value):
            eligible_keys.append(key)
            count += 1
    for key in eligible_keys:
        del idempotency_keys[key]
    return count

while True:
    try:
        line = input().strip()
    except EOFError:
        break
    line = line.split()
    if not line:
        continue
    command = line[0]
    key = line[1]
    if command == "CREATE":
        fingerprint = line[2]
        response = line[3]
        timestamp = int(line[4])
        ttl = int(line[5])
        print(create_idempotency_key(key, fingerprint, response, timestamp, ttl))
    elif command == "GET":
        timestamp = int(line[2])
        print(get_idempotency_key(key, timestamp))
    elif command == "CLEANUP":
        timestamp = int(key)
        print(cleanup(timestamp))