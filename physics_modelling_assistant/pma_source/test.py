import sys, traceback
print("python:", sys.executable)
try:
    import pma_source
    print("OK:", pma_source.__file__)
except Exception:
    traceback.print_exc()
print("sys.path[:8]:")
for p in sys.path[:8]:
    print(" ", p)