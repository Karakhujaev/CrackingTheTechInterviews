import os
file = os.path.join("submissions", "file.py")

with open(file, "w") as f:
    f.write("print(1)")