from pathlib import Path

Path = Path(r"C:\Users\Dell\Desktop\favzy_folder\my_file.txt")
print(Path.exists())
print(Path.name)
print(Path.parent.name)
print(Path.is_dir())
print(Path.is_file())
