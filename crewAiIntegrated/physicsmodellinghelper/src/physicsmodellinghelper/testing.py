import importlib, inspect

mod_name = "crewai.utilities"
mod = importlib.import_module(mod_name)

print(f"Module: {mod_name} -> {getattr(mod, '__file__', 'built-in or namespace package')}\n")

for name in sorted(dir(mod)):
    try:
        obj = getattr(mod, name)
    except Exception:
        print(name, "<unreadable>")
        continue
    kind = "module" if inspect.ismodule(obj) else "class" if inspect.isclass(obj) else "function" if inspect.isfunction(obj) else type(obj).__name__
    print(f"{name:40} {kind}")
