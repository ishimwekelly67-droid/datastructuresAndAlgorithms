from collections import deque

print("\n=== Queue Practical Scenarios (Rwanda) ===")

# Practical (Rwanda): At RSSB, 6 applicants join. After 2 served, who is in front?
queue = deque(["Applicant1", "Applicant2", "Applicant3", "Applicant4", "Applicant5", "Applicant6"])
print("\nInitial queue (RSSB):", list(queue))

# Serve 2 (dequeue)
queue.popleft()
queue.popleft()

print("Queue after 2 served:", list(queue))
print("Person now in front:", queue[0])
