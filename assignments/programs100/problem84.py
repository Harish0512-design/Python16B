# Please write a program to generate all sentences where subject is in
# ["I", "You"] and verb is in ["Play", "Love"] and the object is in
# ["Hockey","Football"].
# Hints:
# Use list[index] notation to get a element from a list.

subjects = ["I", "You"]
verbs = ["Play", "Love"]
objects = ["Hockey", "Football"]

for s in range(len(subjects)):
    for v in range(len(verbs)):
        for o in range(len(objects)):
            print(subjects[s] + " " + verbs[v] + " " + objects[o])
