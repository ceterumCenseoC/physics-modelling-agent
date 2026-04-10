# run inside the same venv/python you use to create the Agent
import inspect, re
from crewai.utilities import reasoning_handler

print("module file:", inspect.getfile(reasoning_handler))
print("module attrs:", sorted(name for name in dir(reasoning_handler) if "plan" in name.lower() or "reason" in name.lower()))

# search the module source for planning-related tokens
src = inspect.getsource(reasoning_handler)
for m in re.finditer(r"\bplanning_config\b|\bplanning\b|\bcreate_plan\b|\bmake_plan\b|\bplanner\b|\breplan\b", src):
    lineno = src.count("\n", 0, m.start()) + 1
    start = max(0, m.start()-80)
    end = min(len(src), m.end()+80)
    print(f"\nmatch at approx line {lineno}:\n", src[start:end].replace("\n", " "))
