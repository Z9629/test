import os
if os.getuid() == 0:
    print("yes")
else:
    print("no")
