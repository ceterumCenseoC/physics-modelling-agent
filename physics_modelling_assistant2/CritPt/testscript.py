import importlib.metadata as md
for ep in md.entry_points():
    if "inspect" in ep.group or "model" in ep.group or "inspect" in ep.value:
        print(ep.group, ep.name, "->", ep.value)