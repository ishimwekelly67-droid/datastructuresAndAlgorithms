from collections import deque

# Practical (Rwanda): At Airtel, 7 clients queue. Who is served third?
queue = deque(["Client1", "Client2", "Client3", "Client4", "Client5", "Client6", "Client7"])
print("\nInitial queue (Airtel):", list(queue))

# Serve first 3
served = [queue.popleft(), queue.popleft(), queue.popleft()]
print("Served clients:", served)
print("The third client served was:", served[2])