print("Stack Practical UR")

# Practical (Rwanda): UR pushes ["Assignment1", "Assignment2", "Assignment3"]. Pop all.
stack = []
stack.append("Assignment1")
stack.append("Assignment2")
stack.append("Assignment3")

print("\nInitial stack (UR):", stack)

# Pop all elements
while stack:
    popped = stack.pop()
    print("Popped:", popped)

print("Remaining in stack:", stack)  # empty