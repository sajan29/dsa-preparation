# value >= start and value <= end
# break
# value > start
# i++
from collections import defaultdict
gateways = defaultdict(list)

class Response:
    OK = "OK"
    ERROR = "ERROR"

def add_gateway(gateway, start, end):

    if start >= end:
        return Response.ERROR
    gateways[gateway].append([start,end])
    gateways[gateway] = normalized_info(sorted(gateways[gateway]))
    return "OK"

def get_gateway(gateway):
    return gateways.get(gateway)

def is_available(gateway, timestamp):
    gateway_info = get_gateway(gateway)
    if gateway_info is None:
        return "NO"
    for i in range(0,len(gateway_info)):
        start , end = gateway_info[i][0], gateway_info[i][1]
        if timestamp >= start and timestamp <= end:
            return "NO"
    return "YES"

def normalized_info(gateway):
    normalized_info = []
    normalized_info.append(gateway[0])
    i = 0
    j = 1
    while j < len(gateway):
        start = normalized_info[i][0]
        end = normalized_info[i][1]
        if gateway[j][0] >= start and gateway[j][0] <= end:
            if gateway[j][1] > normalized_info[i][1]:
                normalized_info[i][1] = gateway[j][1]
        else:
            normalized_info.append(gateway[j])
            i+=1
        j+=1
    return normalized_info

while True:
    try:
        line = input().strip()
    except EOFError:
        break

    if not line:
        continue

    line = line.split()
    command = line[0]
    gateway = line[1]
    if command == "ADD":
        start = int(line[2])
        end = int(line[3])
        print(add_gateway(gateway, start, end))
    elif command == "IS_AVAILABLE":
        timestamp = int(line[2])
        print(is_available(gateway, timestamp))
