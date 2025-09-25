# Practical (Rwanda): In Irembo, push ["Form1", "Form2", "Form3"]. Pop 1.
stack = []
stack.append("Form1")
stack.append("Form2")
stack.append("Form3")

print("\nInitial stack (Irembo):", stack)

stack.pop()  # remove last
print("After popping 1:", stack)