import csv
from pathlib import Path

path = Path.cwd() / "new_directory" / "consensus.csv"
path.touch()


# assignment
# correction = []


# def decode(string):
#     lst = string.split(",")
    # correction.append([int(num) for num in lst])
    # print([int(num) for num in lst])

    # new_lst = []
    # for i in lst:
    #     new_lst.append(int(i))
    # print(new_lst)


# with open(path, encoding="utf-8", mode="r") as file:
#     lines = file.readlines()
#     for line in lines:
#         decode(line)

# print(correction == numbers)
# with open(path, encoding="utf-8", mode="w") as file:
#     for number in numbers:
#         file.write(f"{number[0]}")
#         for num in number[1:]:
#             file.write(f",{num}")
#         file.write("\n")
# print(list(numbers)[1])

# file = path.open(mode="w", encoding="utf-8")
# with path.open(mode="a", encoding="utf-8v") as file:
# with path.open(encoding="utf-8", mode="r") as file:
#     print(file.readiness()[1])


#   print(file.read())
#     file.write("Hello John,\n")
#     file.write("I really miss you. i will join you during break.\n")

# print(file)
# file.close()
#

# import shutil
#
# path = Path.cwd() / "new_directory" / "ridwan.txt"
# path.touch()
#
# destination = Path.cwd() / "new_directory2" / "ridwan.txt"
# path.replace(destination)
#
# new_path = Path.cwd() / "new_directory2"
# shutil.rmtree(new_path)
# new_path = Path.cwd()/"new_directory3"
# new_path.rmdir()

# path = Path(r"c:/root/media/private/me.jpeg")
# print(Path.is_absolute())
# print(path.exists())
# path2 = Path.home() / "new_dir" / "names.txt"
# Path2 = Path.home()
# Path3 = Path.cwd()
# Patheby = Path(r"C:\Users\Dell\Desktop\New.java")
# print(path2.is_absolute())
# print(Path3.is_absolute())
# print(Path2.exists())
# print(Path3.exists())
# print(path.anchor)
# print(path.name)
# print(path.suffix)
# print(path.stem)
# print(path.parent.parent)
#
# print(list(path.parents))


# Path = Path.cwd() / "see_fifteen" / "elites.txt"
# if not Path.exists():
# Path.mkdir(exist_ok=True)
# Path1 = Path.cwd() / "new_directory" / "dir_1"
# Path2 = Path.cwd() / "new_directory" / "dir_2"/"unknown.txt"
# Path1.mkdir(exist_ok=True, parents=True)
# Path2.parent.mkdir()
# Path2.touch()
# Path.touch()
# print(Path.is_dir())
# print(Path.is_file())

# cwd = Path.cwd()
# dir = [
#     Path.cwd() / "new_directory1",
#     Path.cwd() / "new_directory2",
#     Path.cwd() / "new_directory3",
#     Path.cwd() / "new_directory4"
# ]
#
# for Path in dir:
#     Path.mkdir(exist_ok=True)

# for dir in cwd.iterdir():
#     print(dir)

# for dir in cwd.glob("**/**"):
# for dir in cwd.glob("*.txt"):
# for dir in cwd.rglob("new_directory[1234]"):
#     print(dir)


# source = Path.cwd() / "new_directory" / "dir_2" / "unknown.txt"
# print(source.exists())
#
# destination = Path.cwd()
