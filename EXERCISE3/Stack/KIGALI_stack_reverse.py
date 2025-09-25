# Challenge: Reverse "KIGALI" using stack
word = "KIGALI"
stack = list(word)  # push each letter
reversed_word = ""

while stack:
    reversed_word += stack.pop()

print("\nReversed 'KIGALI':", reversed_word)

# Reflection: Why stack models undo for exams?
print("\nReflection (Stack): Stack works on LIFO principle, so the most recent action "
      "is undone first. In exams, if you write something wrong, the last step is the one you erase/undo.")