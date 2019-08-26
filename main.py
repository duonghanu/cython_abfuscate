import os

from obfuscated_my_precious import brain


print("\n\n\n### BEGIN ###\n\n\n")

brain()

print("\n\n\n### END ###\n\n\n")
print("See the `my_precious.py` is gone and now only we have the compiled version !")

print(*os.listdir("."), sep="\n")
